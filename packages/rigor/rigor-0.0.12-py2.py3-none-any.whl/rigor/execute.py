import asyncio
import aiohttp
import os
import time


def execute(suite):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(async_execute(loop, suite))
    loop.run_until_complete(future)

    success = True
    for result in future.result():
        suite.add_result(result)
        success = success and result.success

    return success

async def async_execute(loop, suite):
    from . import State, Namespace

    tasks = []
    connector = aiohttp.TCPConnector(limit_per_host=suite.concurrency)

    with aiohttp.ClientSession(loop=loop, connector=connector) as session:
        for case in suite.queued.values():
            for scenario in case.scenarios:
                task = asyncio.ensure_future(do_scenario(
                        State(session=session,
                              suite=suite,
                              case=case,
                              scenario=scenario)
                ))

                tasks.append(task)

        results = await asyncio.gather(*tasks, return_exceptions=True)

    return results


async def do_scenario(state):
    from . import Result

    fail_step = None
    fail_validations = None
    start_time = time.time()
    first_step = True
    state.success = True

    state.scenario = state.scenario.evaluate(state)

    for step in state.case.steps:

        # todo: replace with sleep on step
        if first_step:
            first_step = False
        else:
            await asyncio.sleep(0.5)

        try:
            for state.iterate in step.iterate.iterate(state):
                # fetch
                await step.fetch(state)

                # extract response
                state.extract = step.extract.evaluate(state)

                # validate response
                fail_validations = step.validate_response(state)

                # check status
                assert len(fail_validations) == 0

        except Exception as exc:
            state.success = False
            print(type(exc))  # todo: better error handling info for reporting.

        # break if step fails
        if not state.success:
            fail_step = step
            break

    running_time = time.time() - start_time

    return Result(case=state.case,
                  scenario=state.scenario,
                  success=state.success,
                  fail_step=fail_step,
                  fail_validations=fail_validations,
                  running_time=running_time,
                  fetch=state.fetch,
                  response=state.response,
                  status=state.status)

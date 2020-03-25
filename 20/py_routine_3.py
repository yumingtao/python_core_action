import asyncio
import time


async def worker_1():
    print("worker_1 start")
    await asyncio.sleep(1)
    return 1


async def worker_2():
    print("worker_2 start")
    await asyncio.sleep(1)
    return 2/0


async def worker_3():
    print("worker_3 start")
    await asyncio.sleep(3)
    return 3


async def task_main():
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    print("before await")
    await asyncio.sleep(2)
    task_3.cancel()

    # return_exceptions=True 防止错误throw到这个执行层
    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print("res:", res)


start_time = time.perf_counter()
asyncio.run(task_main())
print("time spend:", time.perf_counter() - start_time)


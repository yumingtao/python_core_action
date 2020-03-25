import asyncio
import time

async def worker_1():
    print("worker_1 start")
    await asyncio.sleep(1)
    print("worker_1 done")


async def worker_2():
    print("worker_2 start")
    await asyncio.sleep(1)
    print("worker_2 done")


async def task_main():
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())

    print("before await")
    await task_1
    print("awaited worker_1")
    await task_2
    print("awaited worker_1")


start_time = time.perf_counter()
asyncio.run(task_main())
print("time spend:", time.perf_counter() - start_time)


import asyncio
import random
import time


async def consumer(queue, id):
    while True:
        val = await queue.get()
        print("{} get a val: {}".format(id, val))
        await asyncio.sleep(1)


async def producer(queue, id):
    for i in range(5):
        val = random.randint(1, 10)
        await queue.put(val)
        print("{} put a val: {}".format(id, val))
        await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()

    # asyncio.create_task 来创建任务
    # 任务创建后很快就会被调度执行
    consumer_1 = asyncio.create_task(consumer(queue, "consumer_1"))
    consumer_2 = asyncio.create_task(consumer(queue, "consumer_2"))

    producer_1 = asyncio.create_task(producer(queue, "producer_1"))
    producer_2 = asyncio.create_task(producer(queue, "producer_2"))

    print("before await")
    await asyncio.sleep(10)
    print("after await")

    consumer_1.cancel()
    consumer_2.cancel()

    await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)


start_time = time.perf_counter()
asyncio.run(main())
print("time spend:", time.perf_counter() - start_time)
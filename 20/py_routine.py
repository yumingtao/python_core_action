import asyncio
import time


# 异步函数
# 通过await调用会阻塞协程
async def crawl_page_2(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main_1(urls):
    for url in urls:
        await crawl_page_2(url)


async def main_2(urls):
    for url in urls:
        await crawl_page_2(url)


def await_main():
    start_time = time.perf_counter()
    asyncio.run(main_1(['url_1', 'url_2', 'url_3', 'url_4']))
    print("await_main time spend:", time.perf_counter() - start_time)


async def task_main(urls):
    start_time = time.perf_counter()
    tasks = [asyncio.create_task(crawl_page_2(url)) for url in urls]
    for task in tasks:
        await task
    print("task_main time spend:", time.perf_counter() - start_time)


async def gather_main(urls):
    start_time = time.perf_counter()
    tasks = [asyncio.create_task(crawl_page_2(url)) for url in urls]
    # *tasks 解包列表，将列表变成了函数的参数
    # ** dict 将字典变成了函数的参数
    await asyncio.gather(*tasks)
    print("task_main time spend:", time.perf_counter() - start_time)

await_main()
asyncio.run(task_main(['url_1', 'url_2', 'url_3', 'url_4']))

asyncio.run(gather_main(['url_1', 'url_2', 'url_3', 'url_4']))




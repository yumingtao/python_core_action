import concurrent.futures
import time

import requests


def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 系统自动返回cpu的数量*5作为可以调用的线程数
    # Use this number because ThreadPoolExecutor is often
    # used to overlap I/O instead of CPU work.
    # max_workers = (os.cpu_count() or 1) * 5
    with concurrent.futures.ThreadPoolExecutor() as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)

        for future in concurrent.futures.as_completed(to_do):
            future.result()


def main():
    sites = [
        'https://baidu.com',
        'https://sina.com.cn',
        'https://time.geekbang.org',
        "https://baike.baidu.com/item/2020%E5%B9%B4%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92%E7%96%AB%E6"
        "%83%85",
        "https://baike.baidu.com/item/%E5%8E%95%E7%BA%B8#hotspotmining"
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()

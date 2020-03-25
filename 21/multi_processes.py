import concurrent.futures
import time

import requests


def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    # 系统自动返回cpu的数量作为可以调用的线程数
    # 并行操作一般应用于CPU计算密集型的场景
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # 对sites中的每一个元素，并发的调用download_one函数
        executor.map(download_one, sites)


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


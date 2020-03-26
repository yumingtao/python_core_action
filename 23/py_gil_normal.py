import time


def count_down(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    start_time = time.perf_counter()
    count_down(60000000)
    print("time spend:", time.perf_counter() - start_time)



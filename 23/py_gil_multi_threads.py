import time
from threading import Thread


def count_down(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    start_time = time.perf_counter()
    n = 60000000
    t1 = Thread(target=count_down, args=[n // 2])
    t2 = Thread(target=count_down, args=[n // 2])

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("time spend:", time.perf_counter() - start_time)



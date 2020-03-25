import concurrent.futures
import time


def calculate_one(num):
    square_sum = 0
    for i in range(num):
        square_sum += i * i
    print(num, square_sum)


def calculate_all(l):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(calculate_one, l)


def main():
    l = (10000000 + x for x in range(10))
    start_time = time.perf_counter()
    result = calculate_all(l)
    print("time spend: ", time.perf_counter() - start_time)


if __name__ == '__main__':
    main()

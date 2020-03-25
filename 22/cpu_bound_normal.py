import time


def calculate(l):
    result = dict()
    for num in l:
        square_sum = 0
        for i in range(num):
            square_sum += i * i
        result[num] = square_sum
    return result


def main():
    l = (10000000 + x for x in range(10))
    start_time = time.perf_counter()
    result = calculate(l)

    for k, v in result.items():
        print(k, v)

    print("time spend: ", time.perf_counter() - start_time)


if __name__ == '__main__':
    main()


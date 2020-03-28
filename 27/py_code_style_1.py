
def find_num(arr, target):
    r = len(arr)
    i = 0
    index = -1

    while i < r - 1:
        m = (i + r) // 2
        if arr[m] * arr[m] > target:
            index = m
            r = m - 1
        else:
            i = m + 1

    if index == -1:
        return -1
    else:
        return arr[index]


if __name__ == '__main__':
    arr = [1, 3, 4, 6, 8, 9, 12]
    num = find_num(arr, 20)
    print("the num is : ", num)

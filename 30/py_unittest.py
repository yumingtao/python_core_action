import unittest


def sort(arr):
    l = len(arr)

    for i in range(0, l):
        for j in range(i + 1, l):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp


class TestSort(unittest.TestCase):

    def test_sort(self):
        arr = [3, 4, 2, 6, 7, 1, 9]
        sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 6, 7, 9])


if __name__ == '__main__':
    # 如果是jupyter，运行方式如下
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

    # 命令行运行方式
    # unittest.main()

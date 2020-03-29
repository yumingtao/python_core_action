from unittest.mock import patch
import py_work


# 经测试，多个函数使用注解的方式，貌似会弄混，而使用with的方式没有问题
# @patch('py_work.pre_process')
# @patch('py_work.sort')
# @patch('py_work.post_process')
def test_work():
    with patch('py_work.pre_process') as mock_pre_process, \
            patch('py_work.sort') as mock_sort, \
            patch('py_work.post_process') as mock_post_process:
        mock_pre_process.return_value = [1, 2]
        mock_sort.return_value = [1, 2, 3]
        mock_post_process.return_value = [1, 3, 5]

        result = py_work.work_process([1, 3])
        print(result)

        mock_pre_process.assert_called_with([1, 3])
        mock_sort.assert_called_with([1, 2])
        mock_post_process.assert_called_with([1, 2, 3])

        assert result == [1, 3, 5]


if __name__ == '__main__':
    test_work()

from unittest.mock import patch
import my_module


@patch("my_module.func_1")
def test_func_1(mock_func_1):
    mock_func_1.return_value = 3
    result = my_module.func_1()
    expect = 3
    assert result == expect, "expect {} but {}".format(expect, result)


@patch("my_module.func_2")
def test_func_3(mock_func_2):
    mock_func_2.return_value = 4
    result = my_module.func_3(4)
    mock_func_2.assert_called_with(4)
    print(result)
    assert result == 4


if __name__ == '__main__':
    test_func_1()
    test_func_3()

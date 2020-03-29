from unittest.mock import MagicMock


def foo(arg):
    if arg < 0:
        return 1
    else:
        return 2


def test_foo():
    mock = MagicMock()
    mock.side_effect = foo
    print(mock(-1))
    print(mock(3))


if __name__ == '__main__':
    test_foo()

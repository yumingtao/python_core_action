import sys

a = []
print("after define:", sys.getrefcount(a))  # expect 2


def func(a):
    print("in func:", sys.getrefcount(a))  # expect 4, 函数栈和函数参数


func(a)
print("after invoking func:", sys.getrefcount(a))  # expect 2， func调用已经结束，来自定义和getrefcount




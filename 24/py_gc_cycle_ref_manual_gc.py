import gc
import os

import psutil


def show_mem_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    mem = info.uss / 1024. / 1024

    print("{} memory used: {} MB".format(hint, mem))


def func():
    show_mem_info("initial")
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_mem_info("after a, b created")
    a.append(b)
    b.append(a)


if __name__ == '__main__':
    func()
    # 显示调用GC可以回收循环依赖占用的内存
    # python是用标记清除和分代收集，针对循环引用的自动回收
    # python分三代收集
    gc.collect()
    show_mem_info("finished")

import os

import psutil


def show_mem_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    mem = info.uss / 1024. / 1024

    print("{} memory used: {} MB".format(hint, mem))


def func_global_a():
    show_mem_info("initial")
    global a
    a = [i for i in range(10000000)]
    show_mem_info("after a created")


if __name__ == '__main__':
    func_global_a()
    show_mem_info("finished")

import threading

n = 0
lock = threading.Lock()


def foo_normal():
    global n
    n += 1


def foo_lock():
    global n
    with lock:
        n += 1


if __name__ == '__main__':
    threads = []

    for i in range(100):
        # threads.append(threading.Thread(target=foo_normal))
        threads.append(threading.Thread(target=foo_lock))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(n)

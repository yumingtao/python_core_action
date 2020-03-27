import objgraph


def func():
    a = [1, 2, 3, 4]
    b = [1, 2, 3, 4]
    a.append(b)
    b.append(a)
    objgraph.show_refs([a])
    objgraph.show_backrefs([a])


if __name__ == '__main__':
    func()

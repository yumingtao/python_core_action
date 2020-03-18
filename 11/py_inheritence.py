class A():
    def __init__(self):
        print("A init called ...")
        print("A init end")


class B(A):
    def __init__(self):
        print("B init called ...")
        super().__init__()
        print("B init end")


class C(A):
    def __init__(self):
        print("C init called ...")
        super().__init__()
        print("C init end")


class D(C, B):
    def __init__(self):
        print("D init called ...")
        super().__init__()
        print("D init end")

if __name__ == '__main__':
    d = D()
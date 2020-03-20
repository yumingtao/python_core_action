def get_sum(a, b):
    return a + b


# 封装成模块并让它可以执行，需要把执行代码放到__main__=='__main__'
if __name__ == '__main__':
    print("testing math_utils_3_with_main.get_sum")
    print("{} + {} = {}".format(2, 4, get_sum(2, 4)))

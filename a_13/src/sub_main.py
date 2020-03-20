# sys.path.append("xxxxx")用来改变当前python解释器的位置
# 注意要引入sys.path.append(".."),表示到当前目录的上一级去寻找
# 注意python 包中需要__init___.py文件，表示该目录是一个包，在python3中可以省略，但是本示例中省略之后找不到包

# 经过分析，pycharm会自动把当前工程目录python_core_action根目录添加到virtual environment（可以在创建python工程时看到并设置）
# 而工程下边还有子目录，所以在引用时，加上全路径a_13.utils.class_utils

# import sys
# sys.path.append("..")

# from utils.math_utils import get_sum_1
from a_13.utils.class_utils import *
import a_13.utils.math_utils

# 通过import的方式，需要带上全名utils.math_utils
print(a_13.utils.math_utils.get_sum_1(1, 4))

print(Encoder1.encode("abcde"))
print(Decoder1.decode("abcde"))
# 导入文件时，文件中暴露的代码都会执行一遍

'''
testing math_utils_3.get_sum
2 + 4 = 6
main1.py get_sum :  6
'''

from c_13.math_utils_3 import get_sum

print("main.py get_sum : ", get_sum(2, 4))

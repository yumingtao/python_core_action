# import sys

# sys.path.append("..")


from b_13.proto.mat import Matrix
from b_13.utils.mat_mul import mat_mul

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])
print("result is : ", mat_mul(a, b))

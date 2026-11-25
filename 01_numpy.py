# installing Numpy............................................. 
# pip install numpy


# importing Numpy.............................................
import numpy as np


# Numpay Arrays vs Lists .......................................



# list = [1,2,3,4,5]
# print(type(list))
# my_arr = np.array([1,2,3,4,5])
# print(type(my_arr))


                # Numpy hold only numbers..........................

 
# list = [1,2,"Hi",4,5]
# print((list))
# arr = np.array([1,2,"hi",4,5])
# print(arr)





# Types of arrays .......................................

    # 1. 1D Array (Vector)
# arr = np.array([1,2,3,4,5])
# print(arr)

                
    # 2. 2D Array (Matrix)
arr_2d = np.array([[1,2,3],[4,5,6]])
# print(arr_2d)
              
    # 3. 3D Array (Tensor)
arr_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr_3d)

# Mulitiple ways of creating Numpay arrays .............................


list = [1,2,3,4,5]
arr = np.array(list)
# print(arr)


list_2d = [[1,2,3],[4,5,6]]
arr_2d = np.array(list_2d)
# print(arr_2d)








arr_range = np.arange(1,11,2)
# print(arr_range)


arr_linespace = np.linspace(1,10,5)
# print(arr_linespace)

arr_ones = np.ones((2,3))
# print(arr_ones)

arr_zeros = np.zeros((2,3))
# print(arr_zeros)

arr_full = np.full((2,3),100)
# print(arr_full)


arr_rand = np.random.rand(2,3)
# print(arr_rand)



arr_rand = np.random.rand(2,3,3)
# print(arr_rand)



# Shape, Dimension and Size of Numpy Arrays
x = np.random.rand(2,3)

# Shape 
x_shape = x.shape
# print(x_shape)

# Dimension (Rank)
x_dim = x.ndim
# print(x_dim)

# Size (Total number of elements)
x_size = x.size
# print(x_size)


# Numpay Array Methods .......................................

a = np.ones(5)
# print(a)

b = np.ones((1,5))
# print(b)

c = np.ones((5,1))
# print(c)


# print(x)


# 1. Transpose

x_transpose = x.transpose()
# print(x_transpose)

# 2 Mean

x_mean = x.mean()
# print(x_mean)

# 3 astype
x_astype = x.astype(int)
# print(x_astype)




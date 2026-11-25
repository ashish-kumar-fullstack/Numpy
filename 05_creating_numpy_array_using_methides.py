# Creating NumPy Arrays............................................

import numpy as np


# Learn different methods to create arrays.

# np.array()	Create array
# np.zeros()	Array filled with zeros
# np.ones()	Array filled with ones
# np.empty()	Uninitialized array
# np.full()	Fill with a specific value
# np.arange()	Generate a range
# np.linspace()	Generate evenly spaced values
# np.eye()	Identity matrix
# np.identity()	Identity matrix
# np.random.rand()	Random values
# np.random.randint()	Random integers


arr1 = np.array([1,2,3,4,5])
arr2 = np.zeros((2,3))
arr3 = np.ones((2,3))
arr4 = np.empty((2,3))
arr5 = np.full((2,3),100)
arr6 = np.arange(1,11,2)
arr7 = np.linspace(1,10,5)
arr8 = np.eye(3)
arr9 = np.identity(2)
arr10 = np.random.rand(2,3)
arr11 = np.random.randint(0,10,size=(2,3))
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
print(arr9)
print(arr10)
print(arr11)

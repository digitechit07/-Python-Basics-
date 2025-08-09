# . Creating a NumPy array:
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr)

# creating a 0-D array
arrZero = np.array(80)
print(arrZero)

# cheching dimenstion of the array
print(arr.ndim)
print(arrZero.ndim)

# Creating a two dimenstion array
arr2 = np.array([[1,3,4],[1,2,4]])
print(arr2)


# number of elements
print(arr.size)
print(arr2.size)

# totol menory taken by an array
print(arr2.nbytes)
print(arr.nbytes)
print(arr.size)
print(arrZero.nbytes)

# singe element size
print(arr.itemsize)

# for data type of the array
print(arr.dtype)

# for the specfic element of the array()
print(arr[1])
print(arr2[0,0])

# Creatomg a 3 dimenstion array
arr3d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3d)
# for specific row of the array
print(arr2[1,:])
print(arr[0:5])



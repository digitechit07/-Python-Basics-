import numpy as np
# starting index ending index inclusive exclusstive
arr3 = np.array([1,2,3,4,5,6,7,8,9,10])
arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr4)
print(arr3)

print(arr3[1:5])
print(arr3[:5])
print(arr3[5:])
print(arr3[0:9:2])
# for specfic row 
print(arr4[1:])
print(arr4[1,1:3])
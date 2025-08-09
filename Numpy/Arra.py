import numpy as np

a = np.array([0,1,2,3,4,5,6,7,8,9])
print(a)
b = np.array([[0,1,2,4],[5,6,7,8],[9,10,11,12]])
print(b)

# You can create arrays using different NumPy functions:
#Converts list/tuple to array
c = np.array([[1,2,3,4],[5,6,7,8]])
print(c)

# 	  Creates array of all 0s 
d = np.zeros((2,3))
print(d)

# Create array of ones 1s
e =  np.ones((3,3))
print(e)

# arrage of number 
f = np.arange(2,10,2)
print(f)
g = np.arange(0,20,2)
print(g)

# Evenly spaced numbers	 
h = np.linspace(0,1,6)
print(h)

# Identity matrix	
i = np.eye(5)
print(i)

i = np.random.rand(2,4)
print(i)
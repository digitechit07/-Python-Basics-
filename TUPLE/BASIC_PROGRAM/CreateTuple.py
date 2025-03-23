#Create a tuple with the values 10, 20, 30, 40, 50 and print it.

ThisTuple = (10,20,30,40,50)
print(type(ThisTuple))

"""
In Python, you can create a tuple without using round brackets ()
by simply separating the values with commas. 
This is called tuple packing.
"""

Tuple = 10,20,30,40,50
print(type(Tuple))


"""
Tuple unpacking is the process of extracting values from a 
tuple and assigning them to individual variables.
"""

Thistuple = (60,70,80,90,100)
a,b,c,d,e = Thistuple
print(type(Thistuple))
print(a)
print(b)
print(c)
print(d)
print(e)

'''
Using * for Partial Unpacking
If you want to capture multiple values in a list while unpacking,
you can use *.
'''

thistypetuple = (10,20,30,40,50,60)
a,*b = thistypetuple
print(a)
print(*b)


"""
If you use * in the middle while unpacking a tuple,
the middle variable will capture multiple values as a list,
 while the first and last variables will get single values. 
"""

unpackStar = (10,20,30,40,50)
a,*b,c = unpackStar
print(a)    # print first value 10
print(*b)    # print middle values 20,30,40
print(c)     # print last value 50

# empty tuple 

empty_tuple = ()
print(type(empty_tuple))


# we can create tuple with one item or value
One_tuple =("tuple",)
print(type(One_tuple))

# this is also example of the empty tuple
emptyTuple = tuple()
print(type(emptyTuple))

# tuple can be any data type 
type_tuple =("string",10,False,True)
print(type_tuple)
print(type(type_tuple))


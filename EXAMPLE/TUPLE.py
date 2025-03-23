#tuple is an immutable data type in python 
#We can create empty tuple 
a=()
print(type(a))
b=(2,)
print(type(b))

c = (1,45,45,2,34,54,False,"Rohan","Shivam")
#we can not change in tuple
print(c)
no = c.count(45)
print(no)

i= c.index(2)
print(i)

tuple =(2,4,5,6)
print( 2 in tuple )   #true
print(7 in tuple)    #false

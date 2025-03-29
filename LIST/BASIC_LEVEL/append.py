# Append a new element to a list and print the updated list.

numbers = [10,20,30,40,50]

numbers.append(60)
print("Updated List :",numbers)


basket = ["banana","apple","grapes"]

basket.append("cherry")
print(basket)

 # example of nested list that mean one list have inside of another list 
num = [50,60,70]
num1 = [80,90,100]
num.append(num1)
print(num)


different_data_types = [1,'cherry',35.6,"apple"]
different_data_types.append("50_differnt_types")
print(different_data_types)


num =[] # empty list
for i in range(1,5):
     num.append(i * 10)
print(num)

"""
Difference Between append() and extend()
append(x) adds x as a single element.
extend(iterable) adds multiple elements from
an iterable (like another list).
"""

a = [1,2,3,4,5]
b = [6,7,8,9,10]

a.append(b)
print(a)       # output = [1,2,3,4,5,[6,7,8,9,10]]

a.extend(b)
print(a)      # output = [1,2,3,4,5,6,7,8,9,10]



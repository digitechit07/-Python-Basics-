# PYTHON LISTS ARE CONTAINER TO STORE A SET OF VALUES OF ANY DATA TYPES.
#list are mutable that means we can change the orignal string 

friends = ["Apple",45.3,"seojin","eren","akira",7]
print(friends)
print(friends[0])
# han = friends.find("Apple")
# print(friends.find("Apple"))
# print(han)
print(friends[1])
# print(friends.replace( "Apple","ELEPHANT"))
print(len(friends))
friends.append("harry")
print(friends)

li =[1,3,5,6,75,4]
li.sort()
print(li)
li.reverse()
print(li)
li.insert(3,333)
print(li)
li.append(0)
print(li)
li.pop(3)
print(li)
# print(li.append(64))
print(li.pop(1)) # print the return value at 1
values = li.pop(1)
print(values)
print(li)
# remove1 = li.remove(4)
# print(remove1)
# print(li.remove(4))
"""
some list methods 
sort(),.rever(),append(),.insert(),.pop(),.remove()
"""
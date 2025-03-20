# example of dict
marks = {
    "Harry":100,
    "shubham":200,
    "siddharth":34,
    0 :"sid"
}

# print(marks,type(marks))
# print(marks["Harry"])
# print(marks["siddharth"])
# print(marks[0])
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry" : 99, "sharddha": 89})
# print(marks)
print(marks.get("Harry")) # 100
print(marks.get("jojo")) # print none 
print(marks["harry2"]) # give me error keywError
"""
it is unorderd
it is mutable 
it is indexed
cannot contain duplication key
"""
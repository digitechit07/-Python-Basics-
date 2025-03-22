# Set are unordered collection of unquie objects,there are two types of set : 
# Sets - They are mutable and new elements can be added once sets are defined
"""
A set in Python is an unordered collection of unique elements. It does not allow duplicate
 values and is defined using curly braces {} or the set() function.

"""
basket = { 'apple','orange','apple','pear','orange', 'banana','grapes'}
print(basket) # duplication will be removed

a = set("asddsaasddsa") #The set() function treats the input string as an iterable and extracts unique letters.
print(a)  # # unique letter in a
print(type(a)) #set("asddsaasddsa") → Creates a set of unique characters
a.add("z")
print(a) #  add() this fuction can add element in the set

b ={"adsddfdfsdadf"} #
print(b)

empty = set()
print(empty)
print(type(empty)) # empty set

emp = {}
print(emp)
print(type(emp)) #dict


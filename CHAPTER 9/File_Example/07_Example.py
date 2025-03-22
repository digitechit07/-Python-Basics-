"""  'r'
Used for reading an existing file.
Cannot modify/write to the file.
File pointer starts at the beginning.
Raises an error if the file does not exist.
"""
file = open("08_example.txt","r")
print(file.read())
#file.write("we cannot write when we are using 'r' ")
file.close()

""" 'r+'
Used for both reading and modifying the file.
File pointer starts at the beginning.
Overwrites existing content when writing (does not append).
Raises an error if the file does not exist
"""

file = open("08_example.txt","r+")
file.write("now this content delete the previous content")
file.seek(0)
print(file.read())
file.close()
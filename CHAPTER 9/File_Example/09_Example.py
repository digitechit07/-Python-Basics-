""" 'a'
Used to add (append) content at the end of a file.
Does not allow reading the file (read() will cause an error).
Does not erase existing content; it adds new content.
Creates the file if it does not exist.
"""

file = open("09_Example.txt","a")
file.write("\nthis is example of \"a\"")
# print(file.read()) # ERROR : cannot read the file
file.close()

"""
Used to read and append content to a file.
Does not erase existing content.
Adds new content at the end without modifying the previous content.
Creates the file if it does not exist.
Allows reading (read()) after seeking to the start (seek(0)).

"""
file = open("09_Example.txt","a+")
file.write("\n\"a+\" this can continue the line")
file.seek(0)
print(file.read())
file.close()

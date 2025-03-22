"""
"x" is used to create a new file.
If the file already exists, it will cause an error.
It is mainly used when you want to ensure that you are not overwriting an existing file.
"""

file = open("10_Example.txt","x")
file.write("This can create a new file")
file.close()

"""
Creates a new file.
Raises an error if the file already exists.
Allows both reading (read()) and writing (write()).

"""

file = open("10_Examples.txt","x+")
file.write("this will create a new file ")
file.seek(0)
print(file.read())
file.close()

file = open("world.txt","a")
file.write("hello python world ")
file.close()

file = open("world.txt","a+")
file.write("this is the example of a+ which are in continue form")
file.seek(0)
print(file.read())
file.close() 
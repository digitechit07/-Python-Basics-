file = open("hello.txt","w")
file.write("Hello this is upendra !")
file.close()

file = open("hello.txt","r")
print(file.read())

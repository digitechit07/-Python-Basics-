file = open("08_example.txt","w")
file.write("now you are learning about python programming")
#print(file.read())  # ERROR : w cannot read the file
file.close()

file = open("08_example.txt","w+")
file.write("now this content erase the previous content of file")
file.seek(0)   
print(file.read())
file.close()
string = "python is a  high level programming language "

file = open("file.txt","w+")
content = file.write(string)
print(content)
print(len(string))

file.seek(0)
print(file.read())
file.close()



file = open("Example.txt","w")
file.write("HELLO I AM UPENDRA SINGH ")
file.close()

file = open("Example.txt","r")
content = file.read()
print(content)
file.close()

file = open("Example.txt","a+")
file.write("\n WE ARE CREATER")
file.seek(0)
print(file.read())
file.close()



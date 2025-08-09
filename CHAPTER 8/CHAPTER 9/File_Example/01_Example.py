file = open("example.txt", "w")  # Open file in write mode
file.write("Hello, this is a file!")  # Write data
file.close()  # Close file


file = open("example.txt","r")
content = file.read()
print(content)
file.close

file = open("example.txt", "a+")
file.write("\nAdding new content!")  # Appends text
file.seek(0)  # Move cursor to the beginning
print(file.read())  # Read entire file
file.close()
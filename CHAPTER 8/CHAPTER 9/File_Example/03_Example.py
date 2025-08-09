file = open("example.txt", "w+")  
file.write("Hello, Python!")  # Writing
file.seek(0)  # Move cursor to the beginning
print(file.read())  # ✅ Works because "w+" allows reading
file.close()

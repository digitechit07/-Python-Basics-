file = open("poem.txt","r")
content = file.read()
if "Twinkle" in content:
    print(content)
else:
    print("Twinkle is not present in the poem.txt")

with open("copy.txt") as file:
    content1 = file.read()
with open("copy1.txt") as file:
    content2 = file.read()

    if content1 == content2 :
        print("yes these lines are identical ")
    else:
        print("no these files are not identical ")
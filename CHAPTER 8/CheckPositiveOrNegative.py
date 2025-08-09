def CheckNumber(num):
    if num > 0:
        print("This number is positive ")
    elif num == 0:
        print("This number is zero ")
    else:
        print("This number is negative")

num = int(input("ENTER THE NUMBER: "))
CheckNumber(num)
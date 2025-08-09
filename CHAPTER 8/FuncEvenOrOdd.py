def EvenOrOdd(num):
    if num == 0:
        print("This number is zero")
    elif num % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")

num = int(input("ENTER THE NUMBER: "))

EvenOrOdd(num)
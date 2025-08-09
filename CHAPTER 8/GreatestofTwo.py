def BiggestNum(num1,num2):
    if num1 > num2:
        print(f"{num1} is biggest number")
    elif num1 == num2:
        print(f"both are equal")
    else:
        print(f"{num2} is biggest number")
num1 = int(input("ENTER THE FIRST NUMBER: "))
num2 = int(input("ENTER THE SECOND NUMBER: "))

BiggestNum(num1,num2)
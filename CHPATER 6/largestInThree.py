first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
third_num = int(input("Enter third number: "))

if first_num == second_num == third_num:
    print("ALL THREE NUMBERS ARE EQUAL")
elif first_num == second_num and first_num > third_num:
    print("FIRST AND SECOND NUMBERS ARE THE LARGEST")
elif first_num == third_num and first_num > second_num:
    print("FIRST AND THIRD NUMBERS ARE THE LARGEST")
elif second_num == third_num and second_num > first_num:
    print("SECOND AND THIRD NUMBERS ARE THE LARGEST")
elif first_num > second_num and first_num > third_num:
    print("FIRST NUMBER IS LARGEST")
elif second_num > first_num and second_num > third_num:
    print("SECOND NUMBER IS LARGEST")
else:
    print("THIRD NUMBER IS LARGEST")

def factorial(num):
    fact = 1
    for i in range(1, num + 1):  # Start from 1 to num
        fact *= i
    return fact

num = int(input("ENTER THE NUMBER: "))
factNum = factorial(num)
print(f"Factorial of {num} is {factNum}")

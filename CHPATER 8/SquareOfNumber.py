def square (n):
    result = n * n
    return result

try:
    n = int(input("ENTER A NUMBER "))
    squareOfNumber =square(n)
    print(f"Square of number is :{squareOfNumber}")
except ValueError:
    print("something went wrong ! please enter vaild number ! ")
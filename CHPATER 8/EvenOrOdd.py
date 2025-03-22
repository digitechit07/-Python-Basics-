
def EvenOrOdd (n):
    if n%2 == 0:
         print(f"The number is even : {n}")
    else:
         print(f"The number iso odd : {n}")

try:
    n = int(input("ENTER A NUMBER : "))
    EvenOrOdd(n)

except ValueError:
     print("Something went wrong! Please enter a valid number.")

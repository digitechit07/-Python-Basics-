def Factorial(num):
    result = 1 
    for  i in range (1,num+1):
        result = result * i
    return result

try:
   num = int(input("ENTER A NUMBER : "))
   FactorialOfNumber =  Factorial(num)
   print(f"The factorial of number : {FactorialOfNumber}")

except ValueError :
    print("something went wrong ! please enter vaild numbere : ")
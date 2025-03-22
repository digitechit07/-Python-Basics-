def PrimeOrNot(num):
    if num < 2:  # Prime numbers are greater than 1
        print(f"{num} is NOT a prime number.")
        return
    
    for i in range(2, num):  
        if num % i == 0:  
            print(f"{num} is NOT a prime number.")  
            return  # Exit function if a divisor is found
    
    print(f"{num} is a Prime number.")  # If no divisor is found, it's prime

try:
    num = int(input("Enter a number: "))  
    PrimeOrNot(num)  
except ValueError:
    print("Something went wrong! Please enter a valid number.")

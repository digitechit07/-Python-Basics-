Num = int(input("ENTER A NUMBER : "))
is_prime = True 

for i in range(2,Num):
    if Num % i == 0:
        is_prime = False
        break

if is_prime and Num >1:
    print(f"{Num} is prime Number ")
else: 
    print(f"{Num} ia not prime Number ")
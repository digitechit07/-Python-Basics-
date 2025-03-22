num = int(input("ENTER A NUMBER : "))

Reverse_Number = 0
while num > 0:
    last_digit = num % 10 
    Reverse_Number = (Reverse_Number * 10) + last_digit
    num = num // 10

print(f"reverse number is {Reverse_Number}")
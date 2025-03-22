Num = int(input("ENTER A NUMBER :"))

Reverse_Num = 0
while Num > 0:
    last_digit = Num % 10
    Reverse_Num = (Reverse_Num * 10) + last_digit
    Num = Num // 10

print(f"Reversed Number : {Reverse_Num} ")

 
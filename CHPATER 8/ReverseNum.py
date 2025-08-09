def ReverseNum(Num):
    reverse = 0
    while(Num>0):
     lastdigit = Num %10
     reverse = reverse *10 +lastdigit
     Num //=10
    return reverse

Num = int(input("ENTER THE NUMBER: "))
print(f"The reverse of number: {ReverseNum(Num)}")


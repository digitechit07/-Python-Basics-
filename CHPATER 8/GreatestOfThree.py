def Greatest (a,b,c):
    
    if(a>b and a>c): 
        return a 
    elif(b>a and b>c): 
        return b 
    else: 
        return c

a = int(input("ENTER A FIRST NUMBER : "))
b = int(input("ENTER A SECOND NUMBER : "))
c = int(input("ENTER A THRID NUMBER : "))

laragest_num = Greatest(a,b,c)

print(f"Grestest number is {laragest_num}")
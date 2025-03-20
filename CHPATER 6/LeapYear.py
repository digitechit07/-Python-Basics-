year = int(input("ENTER THE YEAR : "))

if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0): 
    print("THIS YEAR IS LEAP YEAR ")
else:
    print("THIS YEAR IS NOT A LEAP YEAR ")
try:
    age = int(input("ENTER THE AGE : "))

    if(age>=18): 
        print("YOU CAN GIVE VOTE")
    else:
        print("YOU CAN'T GIVE VOTE")

except ValueError:
    print("ERROR: PLEASE ENTER A VALID NUMBER")
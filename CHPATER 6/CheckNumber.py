try:  
    Num = int( input("ENTER THE NUMBER : "))

    if Num > 0 : 
        print("THIS NUMBER IS POSTIVE ")
    elif Num < 0 :
         print("THIS NUMBER IS NEGATIVE ")
    else :
          print("THIS NUMBER IS ZERO ")

except ValueError:  # If input is not a valid integer, handle the error
   print("ERROR : please enter a vaild integer")



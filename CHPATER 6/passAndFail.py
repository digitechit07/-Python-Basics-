marks1 =int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))
marks4 = int(input("Enter marks 4: "))

total_percentage = (100*(marks1 + marks2 + marks3 + marks4))/400

if marks1 >100 or marks2>100 or marks3>100 or marks4>100 :
       print("your give marks are greater than 100 ")
    
elif total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33:
       print("you are passed",total_percentage)

else: 
       print("You failed,try again next year :",total_percentage)
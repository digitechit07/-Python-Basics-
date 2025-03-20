marks1 = int(input("ENTER THE MARKS :"))
marks2 = int(input("ENTER THE MARKS :"))
marks3 = int(input("ENTER THE MARKS :"))
marks4 = int(input("ENTER THE MARKS :"))

#check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3 + marks4))/400

if(total_percentage>=40):
    print("\nyou are pass ")
    print("your totol percentage : ",total_percentage)
else:
    print("you are fail,try again next year!")



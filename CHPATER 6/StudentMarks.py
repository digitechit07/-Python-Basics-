'''
write a program  to calculate the grade 
of a student from his make from the following scheme:
90-100 =>Ex
80-90  =>A

'''

marks = int(input("ENTER YOUR MARKS: "))

if marks >=100 and marks >=90:
    grade = 'A'
elif marks <90  and marks >=80:
    grade = 'B'
elif marks <80 and marks >=70:
    grade = 'C'
elif marks <70 and marks >=60: 
    grade = 'D'
elif marks <=50 :
    grade = 'F'
    
print("YOUR GRADE IS :",grade)

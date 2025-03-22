"""
A function is like a small machine in a program that performs a specific task.

✅ You give input, and it processes it to give output.
✅ It avoids repetition (you don't have to write the same code again and again).


"""
def fun1 ():   #function
    print("Hello")

fun1()

def goodDay (name):  # function with arugements 
    print(f"Hello {name}")

goodDay(name ="siddhath")

def goodDay1( name1,ending ="good morning"):  # function with defult arguments
    print(f"GOOD DAY {name1}")
    print(ending)

name1 = input("ENTER A NAME :")

goodDay1(name1,"good day ")



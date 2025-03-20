"""
A spam comment is defined as a text containg following keywords
make lots of money ,buy now, subscrible this , click this 
write a program to detect these spam
"""
p1 = "Make a lots of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment : ")

if(p1 in message) or (p2 in message) or (p4 in message) or (p3 in message) :
    print("This comment is spam ")
else: 
    print("This comment is not spam")
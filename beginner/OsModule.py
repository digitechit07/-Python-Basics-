"""
WRITE A PYTHON PROGRAM TO PRINT THE CONTENTS OF THE 
DIRECTORY USING THE OS MODULE 
SECARCH ONLINE FOR THE FUNCTION 
WHICH 
DOES 
THAT
"""
import os
# select the directory whose conten you want to list
directory_path = "/video"
# use the os module to list the directory content
constents = os.listdir(directory_path)
# print the contents of the dirctory
for item in constents:
    print(item)
    
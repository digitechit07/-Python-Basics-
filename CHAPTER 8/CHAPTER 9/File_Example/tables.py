"""
write a program to genrate multiplication tables from 2 to 20 and write it to the 
differnt files.place these file in a folder  for a 13 -year old 
"""
import os
def generateTable(n):
    table =""
    for i in range(1,11):
        table += f"{n} X{i} = {n*i}\n"
        # Ensure the 'tables' folder exists
    if not os.path.exists("tables"):
        os.makedirs("tables")  # Create 'tables' folder if it doesn't exist

    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)
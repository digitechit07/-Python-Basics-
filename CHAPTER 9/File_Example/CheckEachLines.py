with open ("log.txt","r") as file:
    lines = file.readlines()

    lineno = 1
    for line in lines:
        if "python" in line :
            print (f"yes, pyton is present line no {lineno}")
            break
        lineno +=1
    else:
         print("not python is not present")
"""
The game() fuction in a program lets a user play a game and return the score as
an integer.you need to read a file 'hi-score.txt which is either blank or contain 
the previous hi-score.you need to write a program to update the hi -score whenever
the game () fuction breaks the hi -score.
"""
import random

def game():
    print("you are playing the game ..")
    score = random.randint(1,62)
    with open("hiscore.txt") as file:
        hiscore = file.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"your score: {score}")
    if(score>hiscore):
        with open("hiscore.txt","w") as file:
            file.write(str(score))
    return score


game()


"""
if hiscore.txt is empty or contains 30, and the
 game generates 40, it updates the file with 40.

If the next game generates 35, it does not update 
the file because 40 is still the highest score.
"""



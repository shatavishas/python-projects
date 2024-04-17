import random
comp_choice = random.randint(1,3)
if comp_choice==1:
    print("computer says ROCK")
elif comp_choice==2:
    print("computer says PAPER")
elif comp_choice==3:
    print("computer says SCISSOR")


player1=int(input("enter 1 for rock 2 for paper or 3 for scissor"))

if player1==comp_choice:
    print("DRAW MATCH")
elif player1==1 and comp_choice==2:
    print("YOU LOST")
elif player1==1 and comp_choice==3:
    print("YOU WIN")
elif player1==2 and comp_choice==3:
    print("YOU LOST")
elif player1==2 and comp_choice==1:
    print("YOU WIN")
elif player1==3 and comp_choice==1:
    print("YOU LOST")
elif player1==3 and comp_choice==2:
    print("YOU WIN") 
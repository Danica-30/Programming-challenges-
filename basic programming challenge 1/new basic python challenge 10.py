import random
choices = [ "rock","paper","scissors"]
computer= random.choice(choices)
player= None
while player not in choices:
     player= input("rock,paper,or scissors?: ").lower()
def results():
    print(player)
    print(computer)
    
if player== computer:
    results()
    print("you drew")

elif player== "rock":
    if computer== "scissors":
        results()
        print("you won")
    if computer=="paper":
        results()
        print("you lost")
elif player== "paper":
    if computer== "rock":
        results()
        print("you won")
    if computer=="scissors":
        results()
        print("you lost")
elif player== "scissors":
    if computer== "paper":
        results()
        print("you won")
    if computer=="rock":
        results()
        print("you lost")
      
    

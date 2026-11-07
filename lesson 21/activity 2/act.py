import random 

print("welcome to rock paper scissors")

while True:
    game = input("choose betwwen rock, paper or scissors").split().lower()

    choices = ["rock", "paper", "scissors"]
    correctOne =random.choice(choices)
    print(f"you chose {game} and computer chose {correctOne} \n\n")

    if game==correctOne:
        print("Its a tie!")

    elif game=="rock":
        if correctOne=="scissor":
            print("rock wins!")
        else:
            print("sorry you lost!")

    elif game=="scissor":
        if correctOne=="paper":
            print("scissor wins!")
        else:
            print("sorry you lost!")

    elif game=="paper":
        if correctOne=="rock":
            print("paper wins!")
        else:
            print("sorry you lost!")

    else:
        print("Invalid Input")

    attemt=input("do you want to continue: ").strip().lower()

    if attemt=="no":
        print("thank you for playing the game")
        break
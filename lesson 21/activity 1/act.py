import random 

ran = random.randint(0,9)

print("The game is about guessing a number beetween 0 to 9 and once you choose the correct anwser the game ends ")

#logic

while True:
    num =int(input("enter a number between 0-9: "))

    if num==ran:
        print("you got it right")

        break


    else:
        print("try again")
        


    
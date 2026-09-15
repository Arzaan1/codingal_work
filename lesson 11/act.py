print("welcome to the chore checklist countdown app!!!")

total =int(input("enter the total chores for the day: "))

print("The are",total,"chores for the day!!! \n lets begin: ")

chore_at_hand =1
comp = chore_at_hand

while comp <= total:   

 if chore_at_hand ==1:
    print("wake up and prepare")
    next ="quickly reach school"

 elif chore_at_hand == 2:
    print("quickly reach school")
    next ="keep looking to do non subjective learing also during school time"

 elif chore_at_hand == 3:
    print("keep looking to do non subjective learing also during school time")
    next ="have space for recration durig breaks or free time"

 elif chore_at_hand == 4:
    print("have space for recration durig breaks or free time")
    next ="come back and relax at home"

 elif chore_at_hand == 5:
    print("come back and relax at home")
    next ="end the day with something meaningful"

 else:
    print("more than 5 chores are not allowed")
    break

 print(f"you have finished {chore_at_hand} and\m\n your next chore is :- {next} \n\n ")
 print("there are", total-chore_at_hand, "remaning chores")

 curr =str(input("have you completed all the chores (yes/no): ")).strip().lower()

 if (curr =="yes"):
     print("well done for completing all the chores!")
     break
 
 elif(curr =="no"):
    print("it will end soon enough!")
    chore_at_hand += 1

 else:
    print("not a valid input") 

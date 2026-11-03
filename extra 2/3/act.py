import keyword

name=input("what is your name: ")
goal=input("what is a skill you want to get even better at: ")
target=input("what is your target over a few weeks: ")

min=input("how many minutes do you want to practice for : ")

start=input("have you started for today yes or no: ")

while True:

 print(f"your name is {name}\n")
 print(f"your goal is {goal}\n")
 print(f"and you target is {target}  \n")
 if start=="no":
    print("goals are to be practiced everyday!")

    break

 else:
    print("well done for starting!")

    break
if start =="yes": 
 print(f"have you practised for {min}? yes or no: ")

 if min=="yes":
   print("your free to go!")

if min=="no":
  print("keep going!")
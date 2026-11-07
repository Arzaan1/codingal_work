print("welcome to the homework tracker")

piece=input("how many sets of homework do you have?\n: ")
classes = []

while True:

 clas=input("what classes do you have: ")
 classes.append(clas)

 print(f"added {clas} to timetable!")

 clas2=input("any more?: ")

 if clas2.lower() =="no":
  break

completed_classes = ", ".join(classes)

time=input("how much time would you like to do homework for\n: ")

print(f"lets get ready for {piece} sets of homework for {time}\n\n\n")
while True:
 
 a=input(f"have you reached your goal for {time}? and have you finished {piece} sets of homework? and have you completed {completed_classes}\n: ")

 if a=="yes":
  print("you free to go bye!\n\n come back soon!")

  break

 else:
  print("keep going!\n or take a break for 5min")

  






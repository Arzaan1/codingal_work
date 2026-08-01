#our objective is to plan the day for our user

print("welcome to smart school day planner")
print("anwser 3 questions to plan the day")

day= input("enter the day(sunday to saturday): ")
weather= input("enter the weather(sunny/rainy/cloudy): ")
homework= input("is your homework done(yes/no): ")

print()
print("#########your plan for the day is the following#########")

#the logic behind the progam will come here
#this part will only focus on if or elifm

if day in ("saturday", "sunday"):
    print("Its a weekend so enjoy your free time !")
elif day in ("monday"):
    print("Ease out because the weekend was/is around")
elif day == "tuesday":
    print("sometimes school is fun!!!")
elif day == "wednesday":
    print("my favourite subject is physical education")
elif day == "thursday":
    print("one of my favourite days")
elif day == "friday":
    print("i am free for the whole day")
    
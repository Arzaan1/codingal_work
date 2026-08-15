#daily planner
temperature = int(input("Temperature: "))

if temperature < 20:
    activity = "indoor reading"
else:
    activity = "outdoor play"

print("Do", activity)

rain = input("Raining? yes/no: ")
if rain == "yes":
    print("Take an umbrella")

homework = int(input("Homework minutes: "))

if homework > 60:
    print("Take a break")

free = input("Free time? yes/no: ")

if free == "yes":
    final_task = "hobby time"
else:
    final_task = "planning time"

print("===== DAILY PLANNER =====")
print("Temperature:", temperature)
print("Activity:", activity)
print("Raining:", rain)
print("Final Task:", final_task)
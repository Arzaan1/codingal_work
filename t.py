#book planner 

weather = input("weather rainy or cloudy: ")
book = input("book returned yes or no: ")
day = input("day: ")

if day == "saturday" or day == "sunday":
    print("its the weekend")
    
if weather == "sunny" and book == "yes":
    print("Return your book!")

if book == "yes":
    print("stay home and relax")

if weather == "rainy" or "cloudy":
    print("stay home")

print("done")

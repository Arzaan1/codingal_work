print("Library Planner")

day = input("Day: ")
weather = input("Weather rainy or cloudy: ")
book = input("Book to return yes/no: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend!")

if weather == "sunny" and book == "yes":
    print("Return your book!")

if weather == "rainy" or weather == "cloudy":
    print("Take an umbrella!")

if not book == "yes":
    print("No book to return!")

print("Done")
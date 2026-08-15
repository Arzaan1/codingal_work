#my grocery list for the day

print("choose your grocery list for today")

print("1 for rice")
print("2 for egg")
print("3 for apple")
print("4 for chicken")
print("5 for milk")

choice = int(input("enter your choice: "))

if choice == 1:
    print("rice price is",2)

if choice == 2:
    print("egg price is", 4)

if choice == 3:
    print("apple price is", 7)

if choice == 4:
    print("chicken price is", 10)

if choice == 5:
    print("milk price is", 3)

choice = input("anything else yes or no: ")

if choice == "yes":
    choice = int(input("enter your choice: "))

else:
    print("thank you for shopping")


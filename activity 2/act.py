print("Holiday Planner")

choice = int(input("1 Beach, 2 Mountain: "))

if choice == 1:
    activity = int(input("1 Swimming, 2 Sandcastle: "))

    if activity == 1:
        print("You picked Swimming")
    else:
        print("You picked Sandcastle")

elif choice == 2:
    activity = int(input("1 Hiking, 2 Camping: "))

    if activity == 1:
        print("You picked Hiking")
    else:
        print("You picked Camping")

else:
    print("Invalid choice")

print("Done")
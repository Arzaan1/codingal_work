#HOLIDAY PLANER
print("Holiday Planner")

choice = int(input("1 Beach, 2 Mountain: "))

if choice == 1:
    activity = int(input("1 swimming, 2 sandcastle: "))

    if activity == 1:
        print("You picked swimming")
    else:
        print("You picked sandcastle")

elif choice == 2:
    activity = int(input("1 hiking, 2 camping: "))

    if activity == 1:
        print("You picked hiking")
    else:
        print("You picked camping")

else:
    print("invalid choice")

print("Done")
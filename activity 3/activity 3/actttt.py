x = int(input("Enter number: "))
y = int(input("Enter number: "))
z = int(input("Enter number: "))

average = (x + y + z) / 3

print("Average:", average)

if average > x and average > y and average > z:
    print("Average is highest")
else:
    print("Average is not highest")
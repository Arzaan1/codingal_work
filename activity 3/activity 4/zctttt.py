x = int(input("Number 1: "))
y = int(input("Number 2: "))
z = int(input("Number 3: "))

avg = (x + y + z) / 3
print("Average:", avg)

if avg > x and avg > y and avg > z:
    print("Average is higher than all")
else:
    print("Average is not higher than all")
rows = int(input("Enter rows "))

print("Star Pyramid")

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()

print("Floyd Triangle")

num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()

print("Diamond")

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
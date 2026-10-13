rows = int(input("Rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
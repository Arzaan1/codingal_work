try:
    num=int(input("enter a number: "))
    print(f"the number entered is {num}")

except ValueError as ex:
    print("exeption",ex)
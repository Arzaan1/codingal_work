print("\n\n\nwelcone to the grocery store\n\n")

pizza = 0
pizza1 = 0
pizza2 = 0
pizza3 = 0
pizza4 = 0
pizza5 = 0
total = 0
extra = ""

while True:
    print("1. eggs $8.00")
    print("2. bread $10.50")
    print("3. milk $11.00")
    print("4. chiken $12.25")
    break


while True:

 
 pizza1 = int(input("please pick food options 1-4: "))




 if pizza1==1:
    print("$8.00")
 elif pizza1==2:
    print("$10.50")
 elif pizza1==3:
    print("$11.00")
 else:
    print("$12.25")

    print("item selected!\n\n")


 extra = input("Would you like anything else? yes or no: ")

 if extra=="yes":
    continue

 if extra=="no":
    print("Thank you for shopping at the grocery store")

    #print(f"your total is {pizza}")
    cash = input("Cash or card: ")
    print("Come back soon!")

    exit()



while True:
 extra1 = input("Would you like anything else? yes or no: ")

 if extra=="no":
    print("Thank you for shopping at pizza factory")
    print(f"your total is {pizza1+pizza2}")
    cash = input("Cash or card: ")
    print("Come back soon!")
    break

 
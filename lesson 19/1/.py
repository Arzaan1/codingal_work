def cal (t,s):
    rem =t-s
    return rem



inserted = 0
total = 0


print("###########WELCOME TO THE SNACK VENDING MACHIENE###########")

snack=50

print("the coins which are allowed are the following\n\n\n30,20,10,1")

while True:
    coins =int(input("insert a coin: "))
    if coins !=1 and coins !=10 and coins !=20 and coins !=30:
        print("invalid coin..try again")
        continue

    print("the following options of snacks are")
    print("chips 10\n juice 5\n choclate 20\n ")


    total =total+coins
    inserted +=1

    print(f"Inserted coin {coins}. total now: {total}")

    if total>snack:
        print("enough coins inserted")
        break

    remaning_coins = cal(total, snack)

    print("giving you the snack in a sec!!!!!!!!!!!")

if remaning_coins ==0:
    pass
else:
    print("here is your remaning coins,remaning_coins")


    print(f"your summary is  {inserted} {total} ")
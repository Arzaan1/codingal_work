def greet():
    print("Welcome to Art Supplies Store!")

def total(price, items):
    return price * items

def change(total, paid):
    return paid - total

greet()
price = float(input("Price: "))
items = int(input("Items: "))
paid = float(input("Paid: "))

bill = total(price, items)
print("Total:", bill)
print("Change:", change(bill, paid))
print("Thank you!")


def calculate_change(paid, price):
    return paid - price

ticket_price = 30
total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input())

    if coin not in [1, 5, 10, 25]:
        print("Invalid coin")
        continue

    total_inserted += coin
    coins_inserted += 1

    if total_inserted >= ticket_price:
        break

change_due = calculate_change(total_inserted, ticket_price)

if change_due == 0:
    pass
else:
    print(change_due)

print(ticket_price)
print(coins_inserted)
print(total_inserted)
print(change_due)




def total_bill(bill_amount, tip_perc):
    final_amount = bill_amount + (bill_amount * tip_perc / 100)
    return final_amount

bill = total_bill(150, 20)
print("Your bill is", bill)


def seating_arrangements(guests):
    """Finds the number of ways guests can sit"""

    if guests == 0:
        return 1

    if guests == 1:
        return 1

    answer = guests * seating_arrangements(guests - 1)
    return answer


print(seating_arrangements.__doc__)

for people in range(1, 6):
    ways = seating_arrangements(people)
    print(people, "guests =", ways)

def total_bill(bill_amount, tip_perc):
    tip = bill_amount * tip_perc / 100
    total = bill_amount + tip
    return total

print(total_bill(150, 20))


def seating_arrangements(guests):
    """Calculates seating arrangements for guests."""

    if guests == 0 or guests == 1:
        return 1
    else:
        return guests * seating_arrangements(guests - 1)


print(seating_arrangements.__doc__)

print("1 guest:", seating_arrangements(1))
print("2 guests:", seating_arrangements(2))
print("3 guests:", seating_arrangements(3))
print("4 guests:", seating_arrangements(4))
print("5 guests:", seating_arrangements(5))
print("========Welcom to the lemonade stand=========\n\n\n")

price_per_cup = int(input("what is the price of the cup: "))

cup_sold =int(input("how many cups were sold"))

def total(price, cups):
  t = price*cups
  return t


print (total(price_per_cup, cup_sold))


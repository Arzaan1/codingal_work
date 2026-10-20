bill =int(input("What is the bill?: "))

def answer(bill, per):
    total = bill +(bill*0.01*per)
    total =round(total,2)
    print(f"The final amount is {total} ")


answer(bill,10)


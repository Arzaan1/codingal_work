print("##### Welcome To The ATM Machine #####\n\n\n")

total500=0
total100=0
total50=0
total20=0
total10=0
total1=0

while True:
    name =int(input("What is your name? : "))
    total =int(input(f"Hello,{name} how much money do you want to withdraw? : "))
    if total <=0:
        print("Invalid Amount")
    else:
        print(f"Giving {total} QR, for {name}:")

    remaning=total
    note=1
    while note<=6:
        if note ==1:
            value=500
        elif note==2:
            value=100
        elif note==3:
            value=50
        elif note==4:
            value=20
        elif note==5:
            value=10
        else:
            value=1

        no_of_cu =remaning//value
        

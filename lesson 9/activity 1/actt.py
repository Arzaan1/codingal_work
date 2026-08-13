print("########################")
print("bikes or car both are fun")
print("########################")

choice = int(input("enter what vehicle do you use bike or car): "))

if choice ==1:
    type=int(input("enter you have chose bike or scooti\nenter 1 if you choose scooti\nenter 2 for bike: "))

    if type ==1:
        print("motor bikes are fun in a long journey")

    if type ==2:
        print("scooti is a relief in small or crowded in small places")

    if type !=1 and type !=2:
        print("thats an invalid number i hope you know what you are doing!")

elif choice ==2:
    print("pick your car type sedan or suv\n")
    print("enter 1 for sedan\nenter 2 for suv")

    car_type = int(input("enter your car type\n1 for sedan\n2 for suv: "))

    if car_type ==1:
        print("sedan is a good choice for a long journey")

    if car_type ==2:
        print("suv is a good choice for a long journey and also for rough roads")

    if car_type !=1 and car_type !=2:
        print("thats an invalid number i hope you know what you are doing!")

else:
    print("thats an invalid number i hope you know what you are doing!")

print()
print("your custom ride is ready for you to ride")
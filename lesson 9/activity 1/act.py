print("#####################")
print("bikes or car both are fun")
print("#####################")

choice = (int(input("enter what vehicle do you use bike or car): ")))

if choice ==1:
   type=int(input("enter you have chose bike or scooti\nenter 1 if you choose scooti\nenter 2 for bike: "))

if type ==1: 
     print("motor bikes are fun in a long jorney")

if type ==2:
    print("scooti is a relief in small or crowded in small places")

if type !=1 and type !=2:
    print("thats an invalid number i hope you know what you are doing!")
    
elif choice ==2: 
  car_type=int(input("enter which type of car ")) 

else:
    print("thats an invalid number i hope you know what you are doing!")

print("pick your car type sedan or suv\n")
print("enter 1 for sedan\nenter 2 for suv")

car_type = int(input("enter your car type\n 1 for sedan\n 2 for suv: "))


if car_type == 1:
    print("sedan is a good choice for a long jorney")

if car_type ==2:
    print("suv is a good choice for a long jorney and also for rough roads")

else:
    print("thats an invalid number i hope you know what you are doing!")
    print("please enter 1 for sedan or 2 for suv")

print()
print("your custom ride is ready for you to ride")
  

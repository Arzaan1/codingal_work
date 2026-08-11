print("#####################")
print("bikes or car both are fun\n")
print("#####################")

choice = int (input("enter what vehicle do you use bike or car):  "))

if choice ==1:
   type=int(input("enter you have chose bike or scooti\nenter 1 if you choose scooti\nenter 2 for bike: "))

if type ==1: 
     print("motor bikes are fun in a long jorney")

if type ==2:
    print("scooti is a relief in small or crowded in small places")

if type !=1 and type !=2:
    print("thats an invalid number i hope you know what you are doing!")
    
elif choice ==2: 
    type_c=int(input("enter which type of car ")) 

else:
    print("thats an invalid number i hope you know what you are doing!")
  

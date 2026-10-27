print("welcome to the last activity section of exeption handlling class!!!")

flag =True

while flag:

    try:

      num =int(input("enter a number"))
      while num%2==0:
         print("bye!")
         num =int(input("enter a number"))
      flag = False
    except ValueError as er:
     print("wrong input, Error msg: ",  er)

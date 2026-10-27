try:
    num1=int(input("enter the first number: "))
    num2=int(input("enter the seconed number: "))

    result = num1/num2

    print("the final anwser is: ", result)

except ZeroDivisionError as z:
    print("divison by zero is error message is: ", z)
except ValueError as v:
    print("only numbers please error message is", v)
except:
    print("wrong input")
else:
    print("no exeption")
finally:
    print("this is so stubborn")

    
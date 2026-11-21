import random
import math

lucky_number = random.randint(1, 10)

fun_choices = ["Sports", "Movies", "Games", "Music"]
activity = random.choice(fun_choices)

print("Lucky Number:", lucky_number)
print("Activity:", activity)

secret = random.randint(1, 5)

while True:
    guess = int(input("Guess a number from 1 to 5: "))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Try again")

number = float(input("Enter a decimal number: "))

print("Ceiling:", math.ceil(number))
print("Floor:", math.floor(number))

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Copied Sign:", math.copysign(x, y))
print("Absolute Value:", math.fabs(x))

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print("GCD:", math.gcd(num1, num2))

print("\nRandom Fun Calculator Summary")
print("Lucky Number:", lucky_number)
print("Activity:", activity)


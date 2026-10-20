def fact():

print("welcome to the program that calculates that factorial for a number")

if n==0 or n==1:
    return 1

return n*fact(n-1)



print(fact(0))
print(fact(1))
print(fact(8))
print(fact(7))
print(fact(15))
print(fact.__doc__)
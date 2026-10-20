print("######################WELCOME TO THE PROGRAM THAT FINDS THE CUBE######################")

def cube(n):
    return n*n*n
def firstcheck(n):
    if n%3==0:
     print(cube(n))
    else:
       print("the number is not divisible by 3")
firstcheck(66)
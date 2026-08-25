print("enter your marks you got in 5 lessons ")

maths =int(input("enter marks you got in maths"))
english =int(input("enter marks you got in english"))
integrated_cirriculm =int(input("enter marks you got inintegrated_cirriculm"))
science =int(input("enter marks you got in science"))
computing =int(input("enter marks you got in computing"))

avg = int((maths+english+integrated_cirriculm+science+computing)/5)

valid =range (0, 101)

if avg not in valid:
    print("wrong subject scores in computation")

if avg in valid(91, 101):
    print("you have gotten A+. congratulation!!!")

if avg in valid(86, 91):
    print("you have gotten A. congratulation!!!")

if avg in valid(81, 86):
    print("you have gotten B+. congratulation!!!")

if avg not in valid(76, 81):
    print("you have gotten B. congratulation!!!")

if avg not in valid(71, 76):
    print("you have gotten C+. try better next time")

if avg not in valid(67, 71):
    print("you have gotten C. try better next time")

if avg not in valid(62, 67):
    print("you have gotten E+. try better next time")

if avg not in valid(57, 62):
    print("you have gotten E. try better next time")

if avg not in valid(52, 57):
    print("you have gotten D+. try better next time")

if avg not in valid(47, 52):
    print("you have gotten D. try better next time")

if avg not in valid(42, 47):
    print("you have gotten F+. try better next time")

if avg not in valid(0-42):
    print("you have gotten F. try better next time")
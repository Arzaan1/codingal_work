print("=== Power Calculator ===")

base = int(input("Enter the base: "))
exponent = int(input("Enter the power: "))

result = 1

for i in range(1, exponent + 1):
    result = result * base
    print("Step", i, ":", result)

print(base, "to the power of", exponent, "=", result)
temperature = int(input("Temperature: "))

if temperature < 20:
    outfit = "jacket"
else:
    outfit = "t-shirt"

print("Wear:", outfit)

rain = input("Raining? yes/no: ")

if rain == "yes":
    print("Bring an umbrella!")

wind = int(input("Wind speed: "))

if wind > 30:
    print("Wear a windbreaker!")

puddles = input("Puddles? yes/no: ")

if puddles == "yes":
    shoes = "boots"
else:
    shoes = "sneakers"

print("Wear:", shoes)
print("Weather check complete!")
name = input("Name: ")
gadget = input("Gadget: ")

number = 7
speed = 9.5
missions = 12
active = True

print(name, type(name))
print(gadget, type(gadget))
print(number, type(number))
print(speed, type(speed))
print(missions, type(missions))
print(active, type(active))

number = str(number)
speed = str(speed)
missions = str(missions)
active = str(active)

code = name[:3] + name[-1]
reverse = gadget[::-1]

print("Code:", code)
print("Gadget:", reverse)

print("===== AGENT =====")
print("AGENT", code.upper())
print("ID:", number)
print("MISSIONS:", missions)
print("SPEED:", speed)
print("ACTIVE:", active)

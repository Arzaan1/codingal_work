apps = ["coding", "math", "reading"]

name = input("Name: ")
app = input("App: ")

print(type(name))

if app in apps:
    print("Allowed")
else:
    print("Not allowed")

camera = 1
mic = 2

permissions = camera | mic

print(permissions)

if permissions & camera:
    print("Camera ON")

next = camera << 1
print(next)
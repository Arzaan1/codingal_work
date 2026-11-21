from ursina import *
import random
import math

app = Ursina()

window.title = "VICE CITY 3D"
window.borderless = False
window.fullscreen = False
window.color = color.rgb(100, 170, 220)

random.seed(8)

# WORLD
Sky()
ground = Entity(
    model="plane",
    scale=300,
    texture="white_cube",
    texture_scale=(100, 100),
    color=color.rgb(65, 145, 85),
    collider="box"
)

water = Entity(
    model="cube",
    position=(0, -1, 135),
    scale=(300, 1, 60),
    color=color.rgb(20, 130, 190)
)

# ROADS
for x in range(-120, 121, 40):
    Entity(
        model="cube",
        position=(x, 0.02, 0),
        scale=(10, 0.1, 260),
        color=color.dark_gray
    )

for z in range(-120, 121, 40):
    Entity(
        model="cube",
        position=(0, 0.03, z),
        scale=(260, 0.1, 10),
        color=color.dark_gray
    )

# ROAD LINES
for x in range(-120, 121, 40):
    for z in range(-120, 121, 8):
        Entity(
            model="cube",
            position=(x, 0.1, z),
            scale=(0.25, 0.04, 3),
            color=color.yellow
        )

for z in range(-120, 121, 40):
    for x in range(-120, 121, 8):
        Entity(
            model="cube",
            position=(x, 0.1, z),
            scale=(3, 0.04, 0.25),
            color=color.yellow
        )

# CITY BUILDINGS
building_areas = []

for x in range(-100, 101, 20):
    for z in range(-100, 101, 20):

        if abs(x % 40) < 9 or abs(z % 40) < 9:
            continue

        height = random.randint(10, 35)
        width = random.randint(8, 13)

        building = Entity(
            model="cube",
            position=(x, height / 2, z),
            scale=(width, height, width),
            color=random.choice([
                color.rgb(190, 170, 145),
                color.rgb(150, 160, 175),
                color.rgb(210, 190, 160),
                color.rgb(125, 135, 155),
                color.rgb(180, 145, 145)
            ]),
            collider="box"
        )

        building_areas.append((x, z, width / 2 + 1))

        # ROOFTOP
        Entity(
            model="cube",
            parent=building,
            position=(0, 0.51, 0),
            scale=(0.8, 0.03, 0.8),
            color=color.dark_gray
        )

        # WINDOWS
        for row in range(1, int(height laptop hack =true / 4)):
            for side in [-1, 1 hack info]:
                Entity(
                    model="cube",
                    parent=building,
                    position=(side * 0.505, -0.5 + row * 0.13, 0),
                    scale=(0.01, 0.08, 0.45),
                    color=color.azure
                )

# PALM TREES
for i in range(75):
    x = random.randint(-125, 125)
    z = random.randint(-125, 125)

    if abs(x % 40) < 8 or abs(z % 40) < 8:
        continue

    trunk = Entity(
        model="cylinder",
        position=(x, 2, z),
        scale=(0.35, 4, 0.35),
        color=color.rgb(110, 75, 40)
    )

    for angle in range(0, 360, 60):
        leaf = Entity(
            model="sphere",
            position=(
                x + math.sin(math.radians(angle)) * 2,
                4,
                z + math.cos(math.radians(angle)) * 2
            ),
            scale=(2, 0.3, 0.7),
            color=color.rgb(30, 125, 55)
        )
        leaf.rotation_y = angle

# PLAYER
player = Entity(
    position=(0, 1, -8),
    rotation_y=0
)

body = Entity(
    parent=player,
    model="cube",
    position=(0, 1, 0),
    scale=(0.8, 1.4, 0.45),
    color=color.rgb(30, 70, 190)
)

head = Entity(
    parent=player,
    model="sphere",
    position=(0, 1.95, 0),
    scale=(0.55, 0.55, 0.55),
    color=color.rgb(220, 175, 135)
)

leg1 = Entity(
    parent=player,
    model="cube",
    position=(-0.2, 0.25, 0),
    scale=(0.25, 0.6, 0.3),
    color=color.black
)

leg2 = Entity(
    parent=player,
    model="cube",
    position=(0.2, 0.25, 0),
    scale=(0.25, 0.6, 0.3),
    color=color.black
)

# CARS
cars = []

def make_car(position, car_color, police=False):

    car = Entity(
        model="cube",
        position=position,
        scale=(2, 0.8, 4),
        color=car_color
    )

    car.speed = 0
    car.police = police
    car.driver = False

    Entity(
        parent=car,
        model="cube",
        position=(0, 0.65, -0.2),
        scale=(0.8, 0.7, 0.5),
        color=color.rgb(80, 160, 210)
    )

    for x in [-0.85, 0.85]:
        for z in [-1.2, 1.2]:
            Entity(
                parent=car,
                model="cylinder",
                position=(x, -0.25, z),
                rotation_z=90,
                scale=(0.35, 0.2, 0.35),
                color=color.black
            )

    if police:
        Entity(
            parent=car,
            model="cube",
            position=(0, 0.9, 0),
            scale=(0.7, 0.15, 0.3),
            color=color.red
        )

    cars.append(car)
    return car


# PARKED CARS
for i in range(18):
    car = make_car(
        (random.randint(-110, 110), 0.6, random.randint(-110, 110)),
        random.choice([
            color.red,
            color.blue,
            color.white,
            color.orange,
            color.black,
            color.yellow
        ])
    )

# TRAFFIC
traffic = []

for i in range(8):
    car = make_car(
        (random.choice([-120, 120]), 0.6, random.randint(-100, 100)),
        random.choice([color.red, color.blue, color.white])
    )
    car.traffic = True
    car.speed = random.uniform(5, 10)
    traffic.append(car)

# POLICE
police_cars = []

for i in range(3):
    police = make_car(
        (random.randint(-100, 100), 0.6, random.randint(-100, 100)),
        color.rgb(20, 40, 100),
        True
    )
    police_cars.append(police)

# PEOPLE
people = []

for i in range(25):
    person = Entity(
        model="cube",
        position=(
            random.randint(-110, 110),
            1,
            random.randint(-110, 110)
        ),
        scale=(0.5, 1.8, 0.5),
        color=random.choice([
            color.orange,
            color.azure,
            color.lime,
            color.pink,
            color.white
        ])
    )

    person.direction = random.uniform(0, 360)
    person.timer = 0
    people.append(person)

# GAME DATA
money = 500
wanted = 0
in_car = False
current_car = None
mission_active = False
mission_target = None
mission_reward = 0
day_time = 0
game_over = False

# MISSION MARKER
mission_marker = Entity(
    model="sphere",
    position=(60, 2, 60),
    scale=2,
    color=color.yellow,
    enabled=False
)

# UI
title = Text(
    text="VICE CITY",
    position=(-0.85, 0.45),
    scale=2,
    color=color.yellow
)

money_text = Text(
    text="MONEY: $500",
    position=(-0.85, 0.38),
    scale=1.2
)

wanted_text = Text(
    text="WANTED: 0",
    position=(-0.85, 0.32),
    scale=1.2,
    color=color.red
)

mission_text = Text(
    text="MISSION: Press M to start",
    position=(-0.85, 0.25),
    scale=1
)

controls = Text(
    text="WASD Move | E Enter/Exit Car | M Mission | SHIFT Run",
    position=(-0.85, -0.46),
    scale=0.8
)

speed_text = Text(
    text="",
    position=(0.65, -0.43),
    scale=1
)

# CAMERA
camera.position = (0, 8, -15)
camera.fov = 90

def close_to_building(position):
    for x, z, radius in building_areas:
        if abs(position.x - x) < radius and abs(position.z - z) < radius:
            return True
    return False

def nearest_car():
    closest = None
    distance = 999

    for car in cars:
        d = distance_xz(player.position, car.position)
        if d < distance:
            distance = d
            closest = car

    if distance < 5:
        return closest

    return None

def distance_xz(a, b):
    return math.sqrt(
        (a.x - b.x) ** 2 +
        (a.z - b.z) ** 2
    )

def start_mission():
    global mission_active, mission_target, mission_reward

    mission_active = True
    mission_target = Vec3(
        random.randint(-100, 100),
        2,
        random.randint(-100, 100)
    )
    mission_reward = random.randint(300, 1000)

    mission_marker.position = mission_target
    mission_marker.enabled = True
    mission_text.text = "MISSION: Reach the yellow marker!"

def input(key):
    global in_car, current_car, wanted, money

    if key == "e":

        if not in_car:
            car = nearest_car()

            if car and not car.police:
                current_car = car
                in_car = True
                car.driver = True
                player.visible = False

        else:
            in_car = False
            current_car.driver = False
            player.position = current_car.position + Vec3(3, 0, 0)
            player.visible = True
            current_car.speed = 0
            current_car = None

    if key == "m" and not mission_active:
        start_mission()

    if key == "f":
        wanted = min(wanted + 1, 5)

    if key == "escape":
        application.quit()

# MAIN GAME LOOP
def update():

    global money, wanted, mission_active, day_time

    dt = time.dt
    day_time += dt * 0.015

    # DAY AND NIGHT
    brightness = (math.sin(day_time) + 1) / 2
    window.color = color.rgb(
        int(25 + brightness * 75),
        int(35 + brightness * 140),
        int(65 + brightness * 160)
    )

    # PLAYER MOVEMENT
    if not in_car:

        movement = Vec3(0, 0, 0)

        if held_keys["w"]:
            movement.z += 1
        if held_keys["s"]:
            movement.z -= 1
        if held_keys["a"]:
            movement.x -= 1
        if held_keys["d"]:
            movement.x += 1

        if movement.length() > 0:
            movement = movement.normalized()

            speed = 12

            if held_keys["shift"]:
                speed = 19

            new_position = player.position + movement * speed * dt

            if not close_to_building(new_position):
                player.position = new_position

            player.rotation_y = math.degrees(
                math.atan2(movement.x, movement.z)
            )

    # CAR DRIVING
    if in_car and current_car:

        if held_keys["w"]:
            current_car.speed += 20 * dt

        if held_keys["s"]:
            current_car.speed -= 25 * dt

        current_car.speed *= 0.985
        current_car.speed = max(-12, min(35, current_car.speed))

        if held_keys["a"]:
            current_car.rotation_y -= 75 * dt

        if held_keys["d"]:
            current_car.rotation_y += 75 * dt

        current_car.position += (
            current_car.forward * current_car.speed * dt
        )

        speed_text.text = "SPEED: " + str(int(abs(current_car.speed)))

        if abs(current_car.speed) > 22:
            wanted = max(wanted, 1)

    else:
        speed_text.text = ""

    # TRAFFIC
    for car in traffic:
        if not car.driver:
            car.position += car.forward * car.speed * dt

            if car.position.z > 125:
                car.position.z = -125
            if car.position.z < -125:
                car.position.z = 125

    # PEDESTRIANS
    for person in people:

        person.timer += dt

        if person.timer > 3:
            person.direction += random.randint(-90, 90)
            person.timer = 0

        direction = Vec3(
            math.sin(math.radians(person.direction)),
            0,
            math.cos(math.radians(person.direction))
        )

        person.position += direction * 2 * dt

        if abs(person.position.x) > 125:
            person.direction += 180

        if abs(person.position.z) > 125:
            person.direction += 180

    # POLICE CHASE
    for police in police_cars:

        if wanted > 0:

            target = current_car.position if in_car else player.position

            direction = target - police.position
            direction.y = 0

            if direction.length() > 1:
                direction = direction.normalized()
                police.position += direction * (5 + wanted * 2) * dt
                police.rotation_y = math.degrees(
                    math.atan2(direction.x, direction.z)
                )

            if distance_xz(police.position, target) < 4:
                if in_car:
                    current_car.speed *= 0.9

        else:
            police.position += Vec3(
                math.sin(time.time() + police.x),
                0,
                math.cos(time.time() + police.z)
            ) * dt

    # MISSION CHECK
    if mission_active:

        target = current_car.position if in_car else player.position

        if distance_xz(target, mission_target) < 5:

            money += mission_reward
            mission_active = False
            mission_marker.enabled = False
            mission_text.text = "MISSION COMPLETE! +$" + str(mission_reward)

    # WANTED LEVEL
    wanted_text.text = "WANTED: " + "★" * wanted

    # MONEY
    money_text.text = "MONEY: $" + str(money)

    # CAMERA
    if in_car and current_car:
        target_position = current_car.position + Vec3(0, 8, -15)
        camera.position = lerp(camera.position, target_position, dt * 4)
        camera.look_at(current_car.position + Vec3(0, 1, 0))

    else:
        target_position = player.position + Vec3(0, 7, -13)
        camera.position = lerp(camera.position, target_position, dt * 4)
        camera.look_at(player.position + Vec3(0, 1, 0))

    # MARKER ANIMATION
    if mission_marker.enabled:
        mission_marker.y = 2 + math.sin(time.time() * 3) * 0.5
        mission_marker.rotation_y += 60 * dt

app.run()


from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import math
import json
import os

app = Ursina()

window.title = "Minecraft Python Edition"
window.borderless = False
window.fps_counter.enabled = True
window.exit_button.visible = False

SEED = 2026
random.seed(SEED)

world_blocks = {}
particles = []

BLOCKS = {
    "grass": color.rgb(75, 175, 65),
    "dirt": color.rgb(120, 75, 40),
    "stone": color.rgb(120, 120, 130),
    "wood": color.rgb(115, 75, 35),
    "leaves": color.rgb(35, 125, 45),
    "sand": color.rgb(225, 205, 135),
    "planks": color.rgb(180, 125, 65),
    "brick": color.rgb(155, 75, 65)
}

HOTBAR = list(BLOCKS.keys())

inventory = {name: 64 for name in BLOCKS}
selected = 0
world_time = 0
day_length = 180
world_name = "My World"

class Block(Entity):

    def __init__(self, position, kind):

        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            texture="white_cube",
            color=BLOCKS[kind],
            collider="box"
        )

        self.kind = kind
        self.position = tuple(int(v) for v in position)

        world_blocks[self.position] = self

def create_block(position, kind):

    position = tuple(int(round(v)) for v in position)

    if position not in world_blocks:
        Block(position, kind)

def remove_block(position):

    block = world_blocks.pop(position, None)

    if block:
        inventory[block.kind] += 1
        destroy(block)

def terrain_height(x, z):

    hills = (
        math.sin(x * 0.3) * 2
        + math.cos(z * 0.25) * 2
        + math.sin((x + z) * 0.15) * 2
    )

    return int(3 + hills)

def generate_tree(x, y, z):

    for height in range(1, 5):
        create_block(
            (x, y + height, z),
            "wood"
        )

    for dx in range(-2, 3):
        for dz in range(-2, 3):
            for dy in range(3, 6):

                if abs(dx) + abs(dz) < 4:
                    create_block(
                        (x + dx, y + dy, z + dz),
                        "leaves"
                    )

def generate_world():

    print("Generating world...")

    for x in range(-15, 16):
        for z in range(-15, 16):

            height = terrain_height(x, z)

            desert = x > 7

            for y in range(-3, height + 1):

                if y == height:
                    kind = "sand" if desert else "grass"

                elif y > height - 3:
                    kind = "sand" if desert else "dirt"

                else:
                    kind = "stone"

                create_block((x, y, z), kind)

            if not desert and random.random() < 0.055:
                generate_tree(x, height, z)

    print("World generated!")

def save_world():

    data = {
        "seed": SEED,
        "time": world_time,
        "blocks": [
            {
                "position": list(position),
                "kind": block.kind
            }
            for position, block in world_blocks.items()
        ],
        "inventory": inventory,
        "player": [
            player.x,
            player.y,
            player.z
        ]
    }

    with open("minecraft_world.json", "w") as file:
        json.dump(data, file, indent=2)

    print("WORLD SAVED!")

def load_world():

    if not os.path.exists("minecraft_world.json"):
        print("No saved world found!")
        return

    with open("minecraft_world.json", "r") as file:
        data = json.load(file)

    for block in list(world_blocks.values()):
        destroy(block)

    world_blocks.clear()

    for block in data["blocks"]:
        create_block(
            block["position"],
            block["kind"]
        )

    inventory.update(data["inventory"])

    player.position = data["player"]

    global world_time
    world_time = data["time"]

    print("WORLD LOADED!")

generate_world()

player = FirstPersonController(
    position=(0, 14, 0),
    speed=6,
    jump_height=1.5,
    gravity=1
)

player.cursor.visible = False

Sky()

sun = DirectionalLight()
sun.rotation = (45, -45, 45)

AmbientLight(color=color.rgba(120, 120, 120, 255))

hotbar_text = Text(
    text="",
    position=(-0.85, -0.45),
    scale=1.2
)

info_text = Text(
    text="",
    position=(-0.85, 0.45),
    scale=1
)

craft_text = Text(
    text="",
    position=(0.35, 0.35),
    scale=0.8
)

def update_hotbar():

    display = "HOTBAR\n"

    for i, name in enumerate(HOTBAR):

        marker = " > " if i == selected else "   "

        display += (
            marker
            + str(i + 1)
            + " "
            + name
            + " x"
            + str(inventory[name])
            + "\n"
        )

    hotbar_text.text = display

def update():

    global world_time

    if not player:
        return

    world_time += time.dt

    sun.rotation_x = (world_time * 2) % 360

    darkness = (
        math.sin(world_time * 2 * math.pi / day_length)
        + 1
    ) / 2

    sun.color = color.rgb(
        int(100 + darkness * 155),
        int(100 + darkness * 155),
        int(130 + darkness * 125)
    )

    info_text.text = (
        "MINECRAFT PYTHON EDITION\n"
        + "POSITION: "
        + str(tuple(int(v) for v in player.position))
        + "\nBLOCKS: "
        + str(len(world_blocks))
        + "\nWORLD TIME: "
        + str(int(world_time))
    )

    update_hotbar()

def input(key):

    global selected

    if key in [str(i) for i in range(1, 9)]:
        selected = int(key) - 1

    if key == "scroll up":
        selected = (selected - 1) % len(HOTBAR)

    if key == "scroll down":
        selected = (selected + 1) % len(HOTBAR)

    if key == "left mouse down":

        target = mouse.hovered_entity

        if isinstance(target, Block):
            remove_block(target.position)

    if key == "right mouse down":

        target = mouse.hovered_entity

        if isinstance(target, Block):

            new_position = target.position + mouse.normal

            position = tuple(
                int(round(v)) for v in new_position
            )

            if inventory[HOTBAR[selected]] > 0:
                if position not in world_blocks:

                    create_block(
                        position,
                        HOTBAR[selected]
                    )

                    inventory[HOTBAR[selected]] -= 1

    if key == "f5":
        save_world()

    if key == "f9":
        load_world()

    if key == "c":
        craft_planks()

    if key == "b":
        craft_bricks()

    if key == "escape":
        mouse.locked = not mouse.locked

def craft_planks():

    if inventory["wood"] >= 1:

        inventory["wood"] -= 1
        inventory["planks"] += 4

        print("CRAFTED 4 PLANKS!")

    else:
        print("You need wood!")

def craft_bricks():

    if inventory["stone"] >= 4:

        inventory["stone"] -= 4
        inventory["brick"] += 4

        print("CRAFTED 4 BRICKS!")

    else:
        print("You need 4 stone!")

update_hotbar()

print("================================")
print("     MINECRAFT PYTHON EDITION")
print("================================")
print("World:", world_name)
print("Seed:", SEED)
print("Press F5 to save your world!")

app.run()

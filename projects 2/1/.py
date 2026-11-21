
import importlib
import random
import json
import math
import os

try:
    pygame = importlib.import_module("pygame")
except ModuleNotFoundError as error:
    if error.name != "pygame":
        raise
    raise SystemExit("pygame is required. Install it with: python -m pip install pygame") from error

pygame.init()

WIDTH = 1000
HEIGHT = 650
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHADOW PROTOCOL")

clock = pygame.time.Clock()

FONT = pygame.font.SysFont("consolas", 22)
BIG = pygame.font.SysFont("consolas", 48)

BLACK = (10, 10, 18)
WHITE = (240, 240, 255)
BLUE = (30, 180, 255)
RED = (240, 55, 65)
GREEN = (50, 230, 130)
PURPLE = (160, 70, 255)
YELLOW = (255, 220, 60)

def text(message, x, y, color=WHITE, font=FONT):
    image = font.render(str(message), True, color)
    screen.blit(image, (x, y))

class Particle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.uniform(-3, 3)
        self.dy = random.uniform(-3, 3)
        self.life = random.randint(15, 35)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.life -= 1

    def draw(self):
        if self.life > 0:
            pygame.draw.circle(
                screen, BLUE,
                (int(self.x), int(self.y)), 3
            )

class Player:

    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = 4
        self.health = 100
        self.max_health = 100
        self.damage = 25
        self.coins = 0
        self.level = 1
        self.xp = 0
        self.score = 0
        self.cooldown = 0
        self.weapon = "Energy Blade"

    def move(self, keys):

        dx = 0
        dy = 0

        if keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_s]:
            dy += 1
        if keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_d]:
            dx += 1

        if dx and dy:
            dx *= 0.707
            dy *= 0.707

        self.x += dx * self.speed
        self.y += dy * self.speed

        self.x = max(20, min(WIDTH - 20, self.x))
        self.y = max(20, min(HEIGHT - 20, self.y))

        if self.cooldown > 0:
            self.cooldown -= 1

    def attack(self):

        if self.cooldown == 0:
            self.cooldown = 25

            for enemy in enemies[:]:

                distance = math.hypot(
                    self.x - enemy.x,
                    self.y - enemy.y
                )

                if distance < 110:
                    enemy.health -= self.damage

                    for _ in range(12):
                        particles.append(
                            Particle(enemy.x, enemy.y)
                        )

                    if enemy.health <= 0:
                        enemies.remove(enemy)
                        self.coins += 10
                        self.xp += 20
                        self.score += 100

    def upgrade(self):

        if self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level += 1
            self.damage += 10
            self.max_health += 20
            self.health = self.max_health

    def draw(self):

        pygame.draw.circle(
            screen, BLUE,
            (int(self.x), int(self.y)), 17
        )

        pygame.draw.circle(
            screen, WHITE,
            (int(self.x), int(self.y)), 17, 2
        )

        pygame.draw.circle(
            screen, WHITE,
            (int(self.x), int(self.y)), 5
        )

class Enemy:

    def __init__(self, x, y, kind="Drone"):

        self.x = x
        self.y = y
        self.kind = kind

        self.health = 50
        self.speed = 1.5
        self.damage = 0.2
        self.size = 15

        if kind == "Hunter":
            self.health = 90
            self.speed = 2.5
            self.damage = 0.35
            self.size = 20

        if kind == "Titan":
            self.health = 250
            self.speed = 0.8
            self.damage = 0.7
            self.size = 30

    def update(self):

        dx = player.x - self.x
        dy = player.y - self.y

        distance = math.hypot(dx, dy)

        if distance > 1:

            self.x += dx / distance * self.speed
            self.y += dy / distance * self.speed

        if distance < 30:
            player.health -= self.damage

    def draw(self):

        color = RED

        if self.kind == "Hunter":
            color = PURPLE

        if self.kind == "Titan":
            color = YELLOW

        pygame.draw.circle(
            screen, color,
            (int(self.x), int(self.y)),
            self.size
        )

        pygame.draw.rect(
            screen, RED,
            (self.x - 20, self.y - self.size - 12, 40, 5)
        )

        pygame.draw.rect(
            screen, GREEN,
            (self.x - 20, self.y - self.size - 12,
             max(0, 40 * self.health / 250), 5)
        )

class Mission:

    def __init__(self):
        self.target = random.randint(5, 15)
        self.progress = 0
        self.reward = random.randint(100, 300)
        self.completed = False

    def update(self):
        if self.progress >= self.target:
            self.completed = True

def save_game():

    data = {
        "health": player.health,
        "coins": player.coins,
        "level": player.level,
        "xp": player.xp,
        "score": player.score,
        "damage": player.damage
    }

    with open("shadow_save.json", "w") as file:
        json.dump(data, file, indent=4)

def load_game():

    if os.path.exists("shadow_save.json"):

        with open("shadow_save.json", "r") as file:
            data = json.load(file)

        player.health = data["health"]
        player.coins = data["coins"]
        player.level = data["level"]
        player.xp = data["xp"]
        player.score = data["score"]
        player.damage = data["damage"]

def spawn_enemy():

    side = random.choice(["top", "bottom", "left", "right"])

    if side == "top":
        x, y = random.randint(0, WIDTH), -30

    elif side == "bottom":
        x, y = random.randint(0, WIDTH), HEIGHT + 30

    elif side == "left":
        x, y = -30, random.randint(0, HEIGHT)

    else:
        x, y = WIDTH + 30, random.randint(0, HEIGHT)

    kind = random.choices(
        ["Drone", "Hunter", "Titan"],
        weights=[65, 25, 10]
    )[0]

    enemies.append(Enemy(x, y, kind))

player = Player()

enemies = []
particles = []

mission = Mission()

load_game()

spawn_timer = 0
running = True
game_over = False

while running:

    clock.tick(FPS)

    screen.fill(BLACK)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            save_game()
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                player.attack()

            if event.key == pygame.K_F5:
                save_game()

            if event.key == pygame.K_F9:
                load_game()

            if event.key == pygame.K_e:
                if player.coins >= 50:
                    player.coins -= 50
                    player.damage += 10

            if event.key == pygame.K_r and game_over:
                player = Player()
                enemies.clear()
                particles.clear()
                game_over = False

    if not game_over:

        keys = pygame.key.get_pressed()

        player.move(keys)

        spawn_timer += 1

        if spawn_timer >= 100:
            spawn_enemy()
            spawn_timer = 0

        for enemy in enemies[:]:
            enemy.update()
            enemy.draw()

        for particle in particles[:]:
            particle.update()
            particle.draw()

            if particle.life <= 0:
                particles.remove(particle)

        player.upgrade()
        player.draw()

        if player.health <= 0:
            game_over = True

    pygame.draw.rect(screen, RED, (20, 20, 200, 18))

    pygame.draw.rect(
        screen, GREEN,
        (20, 20, max(0, 200 * player.health /
        player.max_health), 18)
    )

    text("SHADOW PROTOCOL", 20, 55, BLUE)
    text("LEVEL: " + str(player.level), 20, 90)
    text("XP: " + str(player.xp), 20, 120)
    text("COINS: " + str(player.coins), 20, 150)
    text("SCORE: " + str(player.score), 20, 180)

    text("WASD = MOVE", 750, 20)
    text("SPACE = ATTACK", 750, 50)
    text("E = UPGRADE (50)", 750, 80)
    text("F5 = SAVE", 750, 110)
    text("F9 = LOAD", 750, 140)

    if game_over:

        text(
            "SYSTEM FAILURE",
            330, 260, RED, BIG
        )

        text(
            "PRESS R TO RESTART",
            350, 330, WHITE
        )

    pygame.display.flip()

pygame.quit()

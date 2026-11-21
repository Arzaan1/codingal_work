import math
import random
import sys

import pygame

pygame.init()

# -------------------- Setup --------------------

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rivals Arena")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("arial", 22)
SMALL_FONT = pygame.font.SysFont("arial", 16)
TITLE_FONT = pygame.font.SysFont("arialblack", 58)

BACKGROUND = (13, 17, 30)
GRID = (24, 31, 49)
WHITE = (240, 244, 255)
CYAN = (73, 220, 255)
BLUE = (65, 135, 255)
RED = (255, 82, 100)
ORANGE = (255, 170, 72)
GREEN = (83, 230, 150)
PURPLE = (180, 110, 255)
YELLOW = (255, 225, 100)

Vec = pygame.Vector2


def draw_text(surface, text, font, color, x, y, center=False):
    image = font.render(text, True, color)
    rect = image.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(image, rect)


def limit_to_arena(position, radius):
    position.x = max(radius + 12, min(WIDTH - radius - 12, position.x))
    position.y = max(radius + 55, min(HEIGHT - radius - 12, position.y))


# -------------------- Game objects --------------------

class Bullet:
    def __init__(self, position, direction, speed, damage, team, radius=5):
        self.position = Vec(position)
        self.velocity = Vec(direction) * speed
        self.damage = damage
        self.team = team
        self.radius = radius
        self.life = 1.8

    def update(self, dt):
        self.position += self.velocity * dt
        self.life -= dt

    def draw(self, surface):
        color = CYAN if self.team == "player" else RED
        pygame.draw.circle(surface, color, self.position, self.radius)
        pygame.draw.circle(surface, WHITE, self.position, max(1, self.radius // 2))


class Particle:
    def __init__(self, position, color):
        angle = random.uniform(0, math.tau)
        speed = random.uniform(40, 250)
        self.position = Vec(position)
        self.velocity = Vec(math.cos(angle), math.sin(angle)) * speed
        self.color = color
        self.life = random.uniform(0.2, 0.6)
        self.max_life = self.life
        self.size = random.randint(2, 5)

    def update(self, dt):
        self.position += self.velocity * dt
        self.velocity *= 0.92
        self.life -= dt

    def draw(self, surface):
        if self.life > 0:
            radius = max(1, int(self.size * self.life / self.max_life))
            pygame.draw.circle(surface, self.color, self.position, radius)


class Pickup:
    TYPES = ("heal", "shield", "rapid")

    def __init__(self, position):
        self.position = Vec(position)
        self.kind = random.choice(self.TYPES)
        self.radius = 13
        self.bob = random.random() * math.tau

    def update(self, dt):
        self.bob += dt * 4

    def draw(self, surface):
        colors = {"heal": GREEN, "shield": PURPLE, "rapid": YELLOW}
        color = colors[self.kind]
        y = self.position.y + math.sin(self.bob) * 4
        pygame.draw.circle(surface, color, (int(self.position.x), int(y)), self.radius)
        pygame.draw.circle(surface, WHITE, (int(self.position.x), int(y)), self.radius, 2)

        label = {"heal": "+", "shield": "S", "rapid": "R"}[self.kind]
        draw_text(surface, label, SMALL_FONT, BACKGROUND,
                  self.position.x, y - 1, center=True)


class Player:
    def __init__(self):
        self.position = Vec(WIDTH / 2, HEIGHT / 2)
        self.radius = 17
        self.speed = 280
        self.health = 100
        self.max_health = 100
        self.fire_cooldown = 0
        self.fire_rate = 0.18
        self.invulnerable = 0
        self.dash_cooldown = 0
        self.shield_time = 0
        self.rapid_time = 0
        self.damage = 25

    def update(self, dt, keys):
        move = Vec(0, 0)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            move.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            move.x += 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            move.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            move.y += 1

        if move.length_squared() > 0:
            move = move.normalize()
            self.position += move * self.speed * dt

        limit_to_arena(self.position, self.radius)
        self.fire_cooldown = max(0, self.fire_cooldown - dt)
        self.dash_cooldown = max(0, self.dash_cooldown - dt)
        self.invulnerable = max(0, self.invulnerable - dt)
        self.shield_time = max(0, self.shield_time - dt)
        self.rapid_time = max(0, self.rapid_time - dt)

    def dash(self, keys):
        if self.dash_cooldown > 0:
            return

        direction = Vec(0, 0)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            direction.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            direction.x += 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            direction.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            direction.y += 1

        if direction.length_squared() == 0:
            direction = Vec(pygame.mouse.get_pos()) - self.position
        if direction.length_squared() == 0:
            return

        self.position += direction.normalize() * 145
        limit_to_arena(self.position, self.radius)
        self.invulnerable = 0.35
        self.dash_cooldown = 1.4

    def shoot(self, target):
        if self.fire_cooldown > 0:
            return None

        direction = Vec(target) - self.position
        if direction.length_squared() == 0:
            return None

        direction = direction.normalize()
        rate = self.fire_rate * (0.55 if self.rapid_time > 0 else 1)
        self.fire_cooldown = rate

        muzzle = self.position + direction * (self.radius + 8)
        return Bullet(muzzle, direction, 650, self.damage, "player", 5)

    def take_damage(self, amount):
        if self.invulnerable > 0:
            return False

        if self.shield_time > 0:
            self.shield_time = max(0, self.shield_time - 1.2)
            self.invulnerable = 0.25
            return False

        self.health -= amount
        self.invulnerable = 0.55
        return self.health <= 0

    def draw(self, surface):
        mouse = Vec(pygame.mouse.get_pos())
        direction = mouse - self.position
        if direction.length_squared() == 0:
            direction = Vec(1, 0)
        direction = direction.normalize()
        side = Vec(-direction.y, direction.x)

        tip = self.position + direction * 24
        left = self.position - direction * 15 + side * 14
        right = self.position - direction * 15 - side * 14

        if self.invulnerable > 0 and int(self.invulnerable * 20) % 2 == 0:
            return

        pygame.draw.polygon(surface, CYAN, (tip, left, right))
        pygame.draw.polygon(surface, WHITE, (tip, left, right), 2)

        if self.shield_time > 0:
            pygame.draw.circle(surface, PURPLE, self.position, 27, 2)


class Enemy:
    def __init__(self, position, kind="chaser", boss=False):
        self.position = Vec(position)
        self.kind = kind
        self.boss = boss
        self.radius = 33 if boss else (19 if kind == "tank" else 15)
        self.health = 260 if boss else (90 if kind == "tank" else 45)
        self.max_health = self.health
        self.speed = 90 if boss else (65 if kind == "tank" else 130)
        self.shoot_cooldown = random.uniform(0.5, 1.5)
        self.contact_cooldown = 0
        self.wiggle = random.random() * math.tau

    def update(self, dt, player, enemy_bullets):
        to_player = player.position - self.position
        distance = max(1, to_player.length())
        direction = to_player / distance

        if self.kind == "shooter" and not self.boss:
            if distance > 270:
                self.position += direction * self.speed * dt
            elif distance < 190:
                self.position -= direction * self.speed * dt
            else:
                strafe = Vec(-direction.y, direction.x)
                self.position += strafe * math.sin(pygame.time.get_ticks() / 400) * self.speed * dt
        else:
            self.position += direction * self.speed * dt

        self.shoot_cooldown -= dt
        self.contact_cooldown = max(0, self.contact_cooldown - dt)

        if (self.kind == "shooter" or self.boss) and self.shoot_cooldown <= 0:
            self.shoot_cooldown = 1.5 if self.boss else 1.8

            if self.boss:
                for offset in (-0.28, 0, 0.28):
                    rotated = Vec(direction).rotate_rad(offset)
                    enemy_bullets.append(
                        Bullet(self.position + rotated * self.radius,
                               rotated, 300, 12, "enemy", 7)
                    )
            else:
                enemy_bullets.append(
                    Bullet(self.position + direction * self.radius,
                           direction, 270, 10, "enemy", 6)
                )

        limit_to_arena(self.position, self.radius)

    def draw(self, surface):
        color = RED if self.kind == "chaser" else ORANGE
        if self.boss:
            color = PURPLE

        pygame.draw.circle(surface, color, self.position, self.radius)
        pygame.draw.circle(surface, WHITE, self.position, self.radius, 2)

        if self.kind == "shooter" or self.boss:
            pygame.draw.circle(surface, BACKGROUND, self.position, self.radius // 3)

        if self.health < self.max_health:
            bar_width = self.radius * 2
            bar_x = self.position.x - self.radius
            bar_y = self.position.y - self.radius - 9
            pygame.draw.rect(surface, (55, 60, 75),
                             (bar_x, bar_y, bar_width, 5), border_radius=3)
            fill = bar_width * max(0, self.health / self.max_health)
            pygame.draw.rect(surface, GREEN if not self.boss else PURPLE,
                             (bar_x, bar_y, fill, 5), border_radius=3)


# -------------------- Game setup and helpers --------------------

def random_spawn():
    side = random.randrange(4)
    if side == 0:
        return Vec(random.randint(30, WIDTH - 30), 65)
    if side == 1:
        return Vec(random.randint(30, WIDTH - 30), HEIGHT - 30)
    if side == 2:
        return Vec(30, random.randint(70, HEIGHT - 30))
    return Vec(WIDTH - 30, random.randint(70, HEIGHT - 30))


def new_game():
    return {
        "player": Player(),
        "enemies": [],
        "player_bullets": [],
        "enemy_bullets": [],
        "pickups": [],
        "particles": [],
        "score": 0,
        "wave": 1,
        "spawn_left": 5,
        "spawn_timer": 0.6,
        "intermission": 0,
        "state": "playing",
        "shake": 0,
    }


def add_explosion(game, position, color):
    for _ in range(14):
        game["particles"].append(Particle(position, color))


def spawn_enemy_for_wave(game):
    wave = game["wave"]
    if wave % 5 == 0 and game["spawn_left"] == 1:
        enemy = Enemy(random_spawn(), "shooter", boss=True)
    else:
        kind = random.choices(
            ["chaser", "shooter", "tank"],
            weights=[65, 22, 13],
            k=1
        )[0]
        enemy = Enemy(random_spawn(), kind)

    game["enemies"].append(enemy)


def draw_background(surface):
    surface.fill(BACKGROUND)
    for x in range(0, WIDTH, 50):
        pygame.draw.line(surface, GRID, (x, 50), (x, HEIGHT), 1)
    for y in range(50, HEIGHT, 50):
        pygame.draw.line(surface, GRID, (0, y), (WIDTH, y), 1)

    pygame.draw.rect(surface, (31, 39, 58), (0, 0, WIDTH, 48))
    pygame.draw.line(surface, (65, 78, 105), (0, 48), (WIDTH, 48), 2)


def draw_hud(surface, game):
    player = game["player"]

    # Health bar
    pygame.draw.rect(surface, (55, 60, 75), (20, 17, 220, 18), border_radius=8)
    health_width = 220 * max(0, player.health / player.max_health)
    pygame.draw.rect(surface, GREEN if player.health > 30 else RED,
                     (20, 17, health_width, 18), border_radius=8)
    draw_text(surface, f"HP {max(0, int(player.health))}", SMALL_FONT, WHITE, 25, 16)

    draw_text(surface, f"SCORE  {game['score']}", FONT, WHITE, 280, 12)
    draw_text(surface, f"WAVE  {game['wave']}", FONT, CYAN, WIDTH - 155, 12)

    dash_label = "DASH READY" if player.dash_cooldown <= 0 else f"DASH {player.dash_cooldown:.1f}s"
    dash_color = CYAN if player.dash_cooldown <= 0 else (150, 155, 170)
    draw_text(surface, dash_label, SMALL_FONT, dash_color, 20, HEIGHT - 28)

    if player.shield_time > 0:
        draw_text(surface, f"SHIELD {player.shield_time:.0f}s",
                  SMALL_FONT, PURPLE, 150, HEIGHT - 28)
    if player.rapid_time > 0:
        draw_text(surface, f"RAPID FIRE {player.rapid_time:.0f}s",
                  SMALL_FONT, YELLOW, 270, HEIGHT - 28)


def draw_overlay(surface, title, subtitle):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((3, 5, 12, 190))
    surface.blit(overlay, (0, 0))
    draw_text(surface, title, TITLE_FONT, CYAN, WIDTH // 2, HEIGHT // 2 - 60, True)
    draw_text(surface, subtitle, FONT, WHITE, WIDTH // 2, HEIGHT // 2 + 15, True)


# -------------------- Main loop --------------------

game = new_game()
running = True

while running:
    dt = min(clock.tick(60) / 1000, 0.033)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN and game["state"] in ("menu", "gameover"):
                game = new_game()
            elif event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT) and game["state"] == "playing":
                game["player"].dash(pygame.key.get_pressed())

    keys = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()

    if game["state"] == "menu":
        draw_background(screen)
        draw_overlay(screen, "RIVALS ARENA", "Press ENTER to play")
        draw_text(screen, "WASD: Move    Mouse: Aim    Left click: Fire    SHIFT: Dash",
                  SMALL_FONT, WHITE, WIDTH // 2, HEIGHT // 2 + 65, True)
        pygame.display.flip()
        continue

    if game["state"] == "gameover":
        draw_background(screen)
        draw_overlay(screen, "ELIMINATED", f"Score: {game['score']}    Press ENTER to retry")
        pygame.display.flip()
        continue

    player = game["player"]
    player.update(dt, keys)

    if mouse_buttons[0]:
        bullet = player.shoot(pygame.mouse.get_pos())
        if bullet:
            game["player_bullets"].append(bullet)

    # Spawn enemies throughout the wave.
    if game["spawn_left"] > 0:
        game["spawn_timer"] -= dt
        if game["spawn_timer"] <= 0:
            spawn_enemy_for_wave(game)
            game["spawn_left"] -= 1
            game["spawn_timer"] = max(0.35, 1.05 - game["wave"] * 0.035)

    # Start the next wave when the arena is clear.
    if game["spawn_left"] == 0 and not game["enemies"]:
        if game["intermission"] <= 0:
            game["intermission"] = 2.0
        else:
            game["intermission"] -= dt
            if game["intermission"] <= 0:
                game["wave"] += 1
                game["spawn_left"] = min(5 + game["wave"] * 2, 24)
                game["spawn_timer"] = 0.8

    # Update enemies and enemy bullets.
    for enemy in game["enemies"]:
        enemy.update(dt, player, game["enemy_bullets"])

        if enemy.position.distance_to(player.position) < enemy.radius + player.radius:
            if enemy.contact_cooldown <= 0:
                enemy.contact_cooldown = 0.8
                if player.take_damage(18):
                    game["state"] = "gameover"
                game["shake"] = 0.15

    # Move and collide player bullets.
    for bullet in game["player_bullets"][:]:
        bullet.update(dt)
        hit_enemy = None

        for enemy in game["enemies"]:
            if bullet.position.distance_to(enemy.position) < bullet.radius + enemy.radius:
                hit_enemy = enemy
                break

        if hit_enemy:
            hit_enemy.health -= bullet.damage
            if bullet in game["player_bullets"]:
                game["player_bullets"].remove(bullet)

            if hit_enemy.health <= 0:
                game["score"] += 500 if hit_enemy.boss else 100
                color = PURPLE if hit_enemy.boss else RED
                add_explosion(game, hit_enemy.position, color)
                if random.random() < 0.22 and not hit_enemy.boss:
                    game["pickups"].append(Pickup(hit_enemy.position))
                game["enemies"].remove(hit_enemy)
        elif bullet.life <= 0:
            game["player_bullets"].remove(bullet)

    # Move and collide enemy bullets.
    for bullet in game["enemy_bullets"][:]:
        bullet.update(dt)
        if bullet.position.distance_to(player.position) < bullet.radius + player.radius:
            game["enemy_bullets"].remove(bullet)
            if player.take_damage(bullet.damage):
                game["state"] = "gameover"
            game["shake"] = 0.12
        elif bullet.life <= 0:
            game["enemy_bullets"].remove(bullet)

    # Pickups.
    for pickup in game["pickups"][:]:
        pickup.update(dt)
        if pickup.position.distance_to(player.position) < pickup.radius + player.radius:
            if pickup.kind == "heal":
                player.health = min(player.max_health, player.health + 30)
            elif pickup.kind == "shield":
                player.shield_time = 6
            else:
                player.rapid_time = 8
            game["pickups"].remove(pickup)

    # Particles.
    for particle in game["particles"][:]:
        particle.update(dt)
        if particle.life <= 0:
            game["particles"].remove(particle)

    # Draw scene with a small hit shake.
    offset = (0, 0)
    if game["shake"] > 0:
        game["shake"] = max(0, game["shake"] - dt)
        offset = (random.randint(-4, 4), random.randint(-4, 4))

    scene = pygame.Surface((WIDTH, HEIGHT))
    draw_background(scene)

    for pickup in game["pickups"]:
        pickup.draw(scene)
    for bullet in game["player_bullets"]:
        bullet.draw(scene)
    for bullet in game["enemy_bullets"]:
        bullet.draw(scene)
    for enemy in game["enemies"]:
        enemy.draw(scene)
    for particle in game["particles"]:
        particle.draw(scene)

    player.draw(scene)
    draw_hud(scene, game)

    screen.fill(BACKGROUND)
    screen.blit(scene, offset)

    if game["spawn_left"] == 0 and not game["enemies"] and game["intermission"] > 0:
        draw_text(screen, f"Wave {game['wave'] + 1} incoming...",
                  FONT, YELLOW, WIDTH // 2, HEIGHT // 2, True)

    pygame.display.flip()

pygame.quit()
sys.exit()
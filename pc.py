import pygame
import random

# Initialize Pygame
pygame.init()
i = 10

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
player_size = 50
player_color = WHITE
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]

# Enemy settings
enemy_size = 50
enemy_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]

# Bullet settings
bullet_size = 20
bullet_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
bullet_list = []

# Speed settings
SPEED = 10
enemy_speed = 10

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("monospace", 35)

# Game Over
game_over = False

# Score
score = 0

def set_level(score, enemy_speed):
    if score < 20:
        enemy_speed = 5
    elif score < 40:
        enemy_speed = 7
    elif score < 60:
        enemy_speed = 9
    else:
        enemy_speed = 12
    return enemy_speed

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, enemy_color, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += enemy_speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

def fire_bullet(bullet_list, player_pos):
    bullet_pos = [player_pos[0] + player_size // 2, player_pos[1]]
    bullet_list.append(bullet_pos)

def update_bullet_positions(bullet_list):
    for bullet_pos in bullet_list:
        if bullet_pos[1] > 0:
            bullet_pos[1] -= SPEED
        else:
            bullet_list.remove(bullet_pos)

def draw_bullets(bullet_list):
    for bullet_pos in bullet_list:
        pygame.draw.rect(screen, bullet_color, (bullet_pos[0], bullet_pos[1], bullet_size, bullet_size))

def bullet_collision_check(bullet_list, enemy_list):
    for bullet_pos in bullet_list:
        for enemy_pos in enemy_list:
            if detect_collision(bullet_pos, enemy_pos):
                bullet_list.remove(bullet_pos)
                enemy_list.remove(enemy_pos)
                return True
    return False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_size
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += player_size
            elif event.key == pygame.K_SPACE:
                fire_bullet(bullet_list, player_pos)

    screen.fill(BLACK)

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    enemy_speed = set_level(score, enemy_speed)

    text = font.render("Score: {0}".format(score), True, WHITE)
    screen.blit(text, (10, 10))

    if collision_check(enemy_list, player_pos):
        game_over = True
        break

    update_bullet_positions(bullet_list)
    bullet_collision_check(bullet_list, enemy_list)

    draw_enemies(enemy_list)
    draw_bullets(bullet_list)

    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(i)
    i = i + 0.05 
    pygame.display.update()

pygame.quit()
print("Your score is: {0}".format(score))
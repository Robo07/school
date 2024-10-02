import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Car settings
CAR_WIDTH = 50
CAR_HEIGHT = 60
CAR_SPEED = 5

# Cat settings
CAT_WIDTH = 50
CAT_HEIGHT = 50
CAT_SPEED = 3

# Bullet settings
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BULLET_SPEED = 7

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Shooting Game")

# Load images
car_image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_image.fill(RED)
cat_image = pygame.Surface((CAT_WIDTH, CAT_HEIGHT))
cat_image.fill(BLACK)

# Car class
class Car:
    def __init__(self):
        self.image = car_image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed = CAR_SPEED

    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - CAR_HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Cat class
class Cat:
    def __init__(self):
        self.image = cat_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - CAT_HEIGHT)
        self.speed = CAT_SPEED

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -CAT_WIDTH:
            self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - CAT_HEIGHT)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BULLET_WIDTH, BULLET_HEIGHT)
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

# Main game loop
def main():
    clock = pygame.time.Clock()
    car = Car()
    cats = [Cat() for _ in range(5)]
    bullets = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(car.rect.x + CAR_WIDTH, car.rect.y + CAR_HEIGHT // 2))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            car.move_up()
        if keys[pygame.K_DOWN]:
            car.move_down()

        screen.fill(BLACK)

        car.draw(screen)

        for cat in cats:
            cat.update()
            cat.draw(screen)

        for bullet in bullets:
            bullet.update()
            bullet.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
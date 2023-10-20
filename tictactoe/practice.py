import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Moving Circle')

clock = pygame.time.Clock()
circle_x, circle_y = WIDTH // 2, HEIGHT // 2
circle_radius = 30
circle_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_UP] and circle_y - circle_speed > circle_radius:
        circle_y -= circle_speed
    if keys[K_DOWN] and circle_y + circle_speed < HEIGHT - circle_radius:
        circle_y += circle_speed
    if keys[K_LEFT] and circle_x - circle_speed > circle_radius:
        circle_x -= circle_speed
    if keys[K_RIGHT] and circle_x + circle_speed < WIDTH - circle_radius:
        circle_x += circle_speed

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

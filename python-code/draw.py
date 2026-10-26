import pygame
import os

# pygame setup
pygame.init()

# Set the original low resolution
low_res_width, low_res_height = 200, 200
low_res_screen = pygame.Surface((low_res_width, low_res_height))

# Set the window size for the final display
window_width, window_height = 800, 800
screen = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock()
running = True

pos = pygame.Vector2(0, 0)

low_res_screen.fill("white")

os.system("cls")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Convert pos to integers before using in set_at
    low_res_screen.set_at((int(pos.x), int(pos.y)), (20, 20, 20))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_i]:
        pos.y -= 1
    if keys[pygame.K_k]:
        pos.y += 1
    if keys[pygame.K_a]:
        pos.x -= 1
    if keys[pygame.K_d]:
        pos.x += 1
    if keys[pygame.K_SPACE]:
        low_res_screen.fill("white")

    # Scale the low resolution screen to fit the window
    scaled_screen = pygame.transform.scale(low_res_screen, (window_width, window_height))
    screen.blit(scaled_screen, (0, 0))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()

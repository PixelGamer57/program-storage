import pygame
import os
import random

pygame.init()
os.system("cls")

screen_size = 700

screen = pygame.display.set_mode((screen_size, screen_size))

clock = pygame.time.Clock()
running = True
paused = False

size = 70
scale = screen_size / size

state = []
next = []

for i in range(size):
    state.append([])
    next.append([])
    for j in range(size):
        state[i].append(random.randint(0,1))
        next[i].append(0)

def rule(x, y):
    sum = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0) and state[(x + i) % size][(y + j) % size] == 1:
                sum += 1

    if sum < 2 or sum > 3:
        next[x][y] = 0
    else:
        if state[x][y] == 0 and sum == 3:
            next[x][y] = 1
        elif state[x][y] == 1:
            next[x][y] = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x = int(mouse_pos[0] // scale)
            y = int(mouse_pos[1] // scale)
            state[x][y] = 1 - state[x][y]


    for x in range(size):
        for y in range(size):
            pygame.draw.rect(screen, (state[x][y]*255,state[x][y]*255,state[x][y]*255) ,pygame.Rect(x * scale, y * scale, scale, scale))

    if not paused:
        for x in range(size):
            for y in range(size):
                rule(x, y)

        state = [row[:] for row in next]

    pygame.display.flip()
    clock.tick(20)

pygame.quit()

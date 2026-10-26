import pygame, math
pygame.init()

size = int(input("Box size (px): "))

data = ""
bin_data = []

with open(input("File: "),"rb") as file:
    data = file.read()

for i in data:
    bin_data.append(int(i))

scale = math.ceil(math.sqrt(len(bin_data)))
screen_size = scale * size

screen = pygame.display.set_mode((screen_size, screen_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    for i in range(len(bin_data)):
        x = i % scale
        y = math.floor(i/scale)
        pygame.draw.rect(screen, (bin_data[i],bin_data[i],bin_data[i]) ,pygame.Rect(x * size, y * size, size, size))


    pygame.display.flip()

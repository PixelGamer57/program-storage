import pygame, os, math, random

pygame.init()
os.system("cls")

screen_size = 700
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()
running = True

v2 = pygame.Vector2
v3 = pygame.Vector3

cam = v2(0, 0)
zoom = 100

w = []

G = 0.01

class Planet:
    def __init__(self, x, y, size=20):
        self.pos = v2(x, y)
        self.size = size
        self.vel = v2(0, 0)
        self.acc = v2(0, 0)
        self.col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def show(self):
        self.pos += self.vel
        pygame.draw.circle(screen, self.col, self.pos * 100 / zoom + cam, self.size * 100 / zoom)
    
    def update(self):
        self.acc = v2(0, 0)
        for i in w:
            if i != self:
                distance = self.pos.distance_to(i.pos)
                if distance > self.size + i.size:
                    self.acc += (i.pos - self.pos) * (G * i.size / self.pos.distance_squared_to(i.pos))
                else:
                    if self.size > 10 and i.size > 10:
                        self.size -= 1
                        p = (self.pos + i.pos) / 2
                        for _ in range(5):  # Create 5 smaller particles
                            w.append(Planet(p.x, p.y, 1))
                            w[-1].acc = v2(random.random() - 0.5, random.random() - 0.5) * 100
                        i.destroy()
                    elif self.size > i.size:
                        self.size += i.size
                        i.destroy()
                        
        self.vel += self.acc


    def destroy(self):
        w.pop(w.index(self))

for i in range(30):
    w.append(Planet(random.randint(0, screen_size), random.randint(0, screen_size), random.randint(10, 100)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cam.y += 10
    if keys[pygame.K_s]:
        cam.y -= 10
    if keys[pygame.K_a]:
        cam.x += 10
    if keys[pygame.K_d]:
        cam.x -= 10
    if keys[pygame.K_q]:
        zoom += 1
    if keys[pygame.K_e]:
        zoom -= 1
    
    zoom = max(1, zoom)

    for i in w:
        i.update()
        i.show()
    
    pygame.display.flip()
    clock.tick(200)

pygame.quit()

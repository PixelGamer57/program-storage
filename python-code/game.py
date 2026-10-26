import pygame, random, math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

mid_scrn = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos = mid_scrn.copy()
world_pos = pygame.Vector2(0,0)

def lerp(a, b, t):
    return a + (b-a)*t

class danger():
    def __init__(self):
        self.x = random.randint(0,screen.get_width())
        self.y = random.randint(0,screen.get_height())
        self.color = [140,80,20]
        self.size = 20

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x+world_pos.x,self.y+world_pos.y], self.size)


enemies = []

for i in range(0,1):
    enemies.append(danger())


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Genre:Fighting
    # Rule: Death Is Good
    # Setting: Fairy Tale
    # Theme: Addiction

    # you, a young lich, feed of the life force of your enemies. you must kill to grow stronger, until you run out of foe


    screen.fill("green")


    pygame.draw.circle(screen, "red", player_pos, 40)

    for bad in enemies:
        bad.draw(screen)
        if math.dist((bad.x+world_pos.x,bad.y+world_pos.y),player_pos)-bad.size-40 <= 0:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y = lerp(player_pos.y, mid_scrn.y - 10, 0.2)
        world_pos.y += 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y = lerp(player_pos.y, mid_scrn.y + 10, 0.2)
        world_pos.y -= 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x = lerp(player_pos.x, mid_scrn.x - 10, 0.2)
        world_pos.x += 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x = lerp(player_pos.x, mid_scrn.x + 10, 0.2)
        world_pos.x -= 300 * dt


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

import pygame, random, os

# pygame setup
pygame.init()

os.system("cls")

screen_size = 700

screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()
running = True

v2 = pygame.Vector2
v3 = pygame.Vector3

size = 17
scale = screen_size/size

head = v2(int(size/2),int(size/2))

move = v2(0,0)

apple = v2(random.randint(0,size-1),random.randint(0,size-1))

length = 4

body = []

pause = False

while running:
    can_press = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and can_press:
          if event.key == pygame.K_w and move != v2(0,1):
            move = v2(0,-1)
          if event.key == pygame.K_s and move != v2(0,-1):
            move = v2(0,1)
          if event.key == pygame.K_a and move != v2(1,0):
            move = v2(-1,0)
          if event.key == pygame.K_d and move != v2(-1,0):
            move = v2(1,0)
          can_press = False
          if event.key == pygame.K_SPACE and pause == True:
            head = v2(int(size/2),int(size/2))
            move = v2(0,0)
            apple = v2(random.randint(0,size-1),random.randint(0,size-1))
            length = 4

    
    screen.fill("black")
    
    if pause == False:

      body.append(v2(head.x,head.y))
      if len(body) >= length:
        body = body[1:length]

      head += move
      
      if move != v2(0,0) and head in body:
        pause = True
      
      if head.x != head.x%size or head.y != head.y%size:
        pause = True
      
      if apple == head or apple in body:
        if apple == head:
          if apple == (0,0) or apple == (size,0) or apple == (0,size) or apple == (size,size):
            length += 2
          length += 1
        apple = v2(random.randint(0,size-1),random.randint(0,size-1))

      
      pygame.draw.rect(screen, (200,50,50), pygame.Rect(apple.x*scale,apple.y*scale,scale,scale))
      
      for i in body:
        pygame.draw.rect(screen, (50,150,50), pygame.Rect(i.x*scale,i.y*scale,scale,scale))
      
      pygame.draw.rect(screen, (50,200,50), pygame.Rect(head.x*scale,head.y*scale,scale,scale))
    else:
      
    
    pygame.display.flip()

    clock.tick(8)

pygame.quit()
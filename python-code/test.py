import pygame as pg, sys

pg.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 12

window = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("SANDBOX")

clock = pg.time.Clock()

cells = [[None for _ in range(HEIGHT//CELL_SIZE)] for _ in range(WIDTH//CELL_SIZE)]

cell_type = 1

colors = [(0,0,0),(160,160,40)]

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    buttons = pg.mouse.get_pressed()
    if buttons[0]:
        pos = pg.mouse.get_pos()
        cells[pos[0]//CELL_SIZE][pos[1]//CELL_SIZE] = cell_type

    window.fill((30,30,30))

    for i in range(WIDTH//CELL_SIZE):
        for j in range(HEIGHT//CELL_SIZE):

            if cells[i][j] == 1 and j < HEIGHT//CELL_SIZE-1:
                if cells[i][j+1] == None:
                    cells [i][j+1] = 1
                    cells[i][j] = None
                elif cells [i+1]

            color = (60,60,60)
            if cells[i][j] != None:
                color = colors[cells[i][j]]
            pg.draw.rect(
                window,
                color,
                (i*CELL_SIZE, j*CELL_SIZE,
                CELL_SIZE - 1, CELL_SIZE - 1)
            )

    pg.display.flip()
    clock.tick(FPS)
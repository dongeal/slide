import pygame as pg # 1. 파이게임 불러오기
from random import randint, shuffle

pg.init()           # 2. 초기화




BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128,128,128)
CELL_SIZE = 200
COLUMN_COUNT =3
ROW_COUNT = 3
SCREEN_WIDTH = CELL_SIZE * ROW_COUNT
SCREEN_HEIGHT = CELL_SIZE * COLUMN_COUNT

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
pg.display.set_caption('Slide')
clock = pg.time.Clock() 

done = False


class Tiles :
    def __init__(self):
        
        pass
    def draw(self):
        pass
    
    def move(row_pos, col_pos, tile_no):
        print (row_pos, col_pos, tile_no)    
        
        


def draw_grid():
        for x in range(ROW_COUNT):
            for y in range(COLUMN_COUNT):
                pg.draw.rect(screen, GRAY,
                        (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE,CELL_SIZE), 1)
                

def runGame():
    global done
   
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pg.event.get():        
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                row_pos = event.pos[0] // CELL_SIZE
                col_pos = event.pos[1] // CELL_SIZE
                tile_no = row_pos + col_pos * COLUMN_COUNT
                Tiles.move(row_pos, col_pos, tile_no)
                # print (row_pos, col_pos)

        draw_grid()
        
        pg.display.update()
            
runGame()
pg.quit()
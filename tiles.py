import pygame as pg # 1. 파이게임 불러오기
from random import  shuffle

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

# 타일 랜덤 작업
# tiles = []
# for index in range(0, COLUMN_COUNT * ROW_COUNT):
#     tiles.append(index)

tiles =[x for x in range(COLUMN_COUNT * ROW_COUNT)] 
tile_colors = {0:BLACK}
for index in range(0, COLUMN_COUNT * ROW_COUNT):
    tile_colors[index]= WHITE




print(tiles)
shuffle(tiles)
print(tiles)

class Tiles :
    def __init__(self,tile_no, row_pos, col_pos):
        self.tile_no = tile_no
        self.row_pos = row_pos
        self.col_pos = col_pos
       
    def draw_black(self):
        if self.tile_no ==0 :
            pg.draw.rect(screen, BLACK,
                        (self.row_pos * CELL_SIZE, self.col_pos * CELL_SIZE,
                          CELL_SIZE,CELL_SIZE))
    def draw(self,color):
        pg.draw.rect(screen, color , pg.Rect
                     (self.row_pos * CELL_SIZE+1, self.col_pos * CELL_SIZE+1,
                       CELL_SIZE-1, CELL_SIZE-1))
            
    def move(self):
       
        print (self.tile_no, self.row_pos, self.col_pos)    
        
        


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
                tile_no = tiles[row_pos + col_pos * COLUMN_COUNT]
                tile= Tiles(tile_no, row_pos, col_pos)
                tile.draw_black()
                tile.move()

            for x in range(len(tiles)):
              
                tile_no= tiles[x]
                color = tiles[tile_no]
                row_pos = x *  CELL_SIZE % ROW_COUNT
                col_pos = x * CELL_SIZE // COLUMN_COUNT
                tile= Tiles(tile_no, row_pos, col_pos)
                tile.draw(color) 
                # print (row_pos, col_pos)

        draw_grid()
       
        pg.display.update()
            
runGame()
pg.quit()
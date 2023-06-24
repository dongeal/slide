import pygame as pg # 1. 파이게임 불러오기
from random import  shuffle

pg.init()           # 2. 초기화


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128,128,128)
CELL_SIZE = 100
BOARD_SIZE_X = 3
BOARD_SIZE_Y = 3

SCREEN_WIDTH = CELL_SIZE * BOARD_SIZE_X
SCREEN_HEIGHT = CELL_SIZE * BOARD_SIZE_Y
# 폰트 정의
game_font = pg.font.Font(None, CELL_SIZE) # 폰트 객체 생성 (폰트, 크기)



screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
pg.display.set_caption('Slide')
clock = pg.time.Clock() 

done = False

# 타일 랜덤 작업
tiles = []
for index in range(0, BOARD_SIZE_X * BOARD_SIZE_Y):
    tiles.append(index)  # [0, 1, 2, ....., 15]

# tiles =[x for x in range(COLUMN_COUNT * BOARD_SIZE_X)] 
# tile_colors = {0:BLACK}
# for index in range(0, COLUMN_COUNT * BOARD_SIZE_X):
#     tile_colors[index]= WHITE
shuffle(tiles)

class Tiles :
    def __init__(self, tile_no, x_pos, y_pos):
        self.tile_no = tile_no
        self.x_pos = x_pos
        self.y_pos = y_pos
       
    def draw(self, color):
        # print(color, self.tile_no, self.x_pos, self.y_pos)
        pg.draw.rect(screen, color,
                 (self.x_pos * CELL_SIZE, self.y_pos * CELL_SIZE,
                   CELL_SIZE,CELL_SIZE))    
        NO_TAG = game_font.render(str(tiles[self.tile_no]), True, BLACK)
                    # 출력할 글자, 안티 알리아스  True, 글자 색상
        screen.blit(NO_TAG, (int((self.x_pos +0.2) * CELL_SIZE),int((self.y_pos+0.2) * CELL_SIZE)))
        # # print(NO_TAG, self.x_pos,self.y_pos)
            
    def move(self, tile_no):

        if tiles[tile_no] != 0 : 
            #top left
            if self.x_pos == 0 and self.y_pos == 0 :     
                if tiles[tile_no+1] == 0:                     # 오른쪽 0  
                    tiles[tile_no],tiles[tile_no+1]= tiles[tile_no+1],tiles[tile_no] 
                elif tiles[tile_no + BOARD_SIZE_X] == 0 :           # 아래 0
                    tiles[tile_no], tiles[tile_no + BOARD_SIZE_X] = tiles[tile_no + BOARD_SIZE_X], tiles[tile_no]
            #top
            elif self.x_pos > 0 and self.x_pos < BOARD_SIZE_X -1 and self.y_pos == 0:
                if tiles[tile_no-1] == 0:        # 왼쪽   0
                     tiles[tile_no],tiles[tile_no-1]= tiles[tile_no-1],tiles[tile_no]
                elif tiles[tile_no+BOARD_SIZE_X] == 0 :           # 아래 0
                    tiles[tile_no],tiles[tile_no+BOARD_SIZE_X]= tiles[tile_no+BOARD_SIZE_X],tiles[tile_no]
                elif tiles[tile_no+1] == 0:                     # 오른쪽 0  
                    tiles[tile_no],tiles[tile_no+1]= tiles[tile_no+1],tiles[tile_no]
            #top right
            if self.x_pos == BOARD_SIZE_X-1 and self.y_pos == 0 :     
                if tiles[tile_no-1] == 0:                     # 왼쪽 0  
                    tiles[tile_no],tiles[tile_no-1]= tiles[tile_no-1],tiles[tile_no]
                elif tiles[tile_no+BOARD_SIZE_X] == 0 :           # 아래 0
                    tiles[tile_no],tiles[tile_no+BOARD_SIZE_X]= tiles[tile_no+BOARD_SIZE_X],tiles[tile_no]
            #left
            elif self.x_pos == 0  and self.y_pos > 0 and self.y_pos < BOARD_SIZE_Y -1:
                if tiles[tile_no-BOARD_SIZE_X] == 0:        # 위쪽   0
                     tiles[tile_no],tiles[tile_no-BOARD_SIZE_X]= tiles[tile_no-BOARD_SIZE_X],tiles[tile_no]
                elif tiles[tile_no+BOARD_SIZE_X] == 0 :           # 아래 0
                    tiles[tile_no],tiles[tile_no+BOARD_SIZE_X]= tiles[tile_no+BOARD_SIZE_X],tiles[tile_no]
                elif tiles[tile_no+1] == 0:                     # 오른쪽 0  
                    tiles[tile_no],tiles[tile_no+1]= tiles[tile_no+1],tiles[tile_no]
            #center
            elif self.x_pos > 0 and self.x_pos < BOARD_SIZE_X -1 and self.y_pos > 0 and self.y_pos < BOARD_SIZE_Y-1 :
                if tiles[tile_no-BOARD_SIZE_X] == 0:        # 위쪽   0
                     tiles[tile_no],tiles[tile_no-BOARD_SIZE_X]= tiles[tile_no-BOARD_SIZE_X],tiles[tile_no]
                elif tiles[tile_no+BOARD_SIZE_X] == 0 :           # 아래 0
                    tiles[tile_no],tiles[tile_no+BOARD_SIZE_X]= tiles[tile_no+BOARD_SIZE_X],tiles[tile_no]
                elif tiles[tile_no+1] == 0:                     # 오른쪽 0  
                    tiles[tile_no],tiles[tile_no+1]= tiles[tile_no+1],tiles[tile_no]    
                elif tiles[tile_no-1] == 0:                     # 왼쪽 0  
                    tiles[tile_no],tiles[tile_no-1]= tiles[tile_no-1],tiles[tile_no]    
            #right
            elif self.x_pos == BOARD_SIZE_X -1 and self.y_pos > 0 and self.y_pos < BOARD_SIZE_Y-1 :
                if tiles[tile_no-BOARD_SIZE_X] == 0:        # 위쪽   0
                     tiles[tile_no],tiles[tile_no-BOARD_SIZE_X]= tiles[tile_no-BOARD_SIZE_X],tiles[tile_no]
                elif tiles[tile_no+BOARD_SIZE_X] == 0 :           # 아래 0
                    tiles[tile_no],tiles[tile_no+BOARD_SIZE_X]= tiles[tile_no+BOARD_SIZE_X],tiles[tile_no]
                elif tiles[tile_no-1] == 0:                     # 왼쪽 0  
                    tiles[tile_no],tiles[tile_no-1]= tiles[tile_no-1],tiles[tile_no]    
            #bottom left
            elif self.x_pos  ==0  and self.y_pos == BOARD_SIZE_Y-1 :
                if tiles[tile_no-BOARD_SIZE_X] == 0:        # 위쪽   0
                     tiles[tile_no],tiles[tile_no-BOARD_SIZE_X]= tiles[tile_no-BOARD_SIZE_X],tiles[tile_no]
                elif tiles[tile_no+1] == 0:                     # 오른쪽 0  
                    tiles[tile_no],tiles[tile_no+1]= tiles[tile_no+1],tiles[tile_no]     
            #bottom
            elif self.x_pos > 0 and self.x_pos < BOARD_SIZE_X -1 and self.y_pos == BOARD_SIZE_Y-1 :
                if tiles[tile_no-BOARD_SIZE_X] == 0:        # 위쪽   0
                     tiles[tile_no],tiles[tile_no-BOARD_SIZE_X]= tiles[tile_no-BOARD_SIZE_X],tiles[tile_no]
                elif tiles[tile_no+1] == 0:                     # 오른쪽 0  
                    tiles[tile_no],tiles[tile_no+1]= tiles[tile_no+1],tiles[tile_no]    
                elif tiles[tile_no-1] == 0:                     # 왼쪽 0  
                    tiles[tile_no],tiles[tile_no-1]= tiles[tile_no-1],tiles[tile_no]
            #bottom right
            elif self.x_pos== BOARD_SIZE_X -1 and self.y_pos == BOARD_SIZE_Y-1 :
                if tiles[tile_no-BOARD_SIZE_X] == 0:        # 위쪽   0
                     tiles[tile_no],tiles[tile_no-BOARD_SIZE_X]= tiles[tile_no-BOARD_SIZE_X],tiles[tile_no]
                elif tiles[tile_no-1] == 0:                     # 왼쪽 0  
                    tiles[tile_no],tiles[tile_no-1]= tiles[tile_no-1],tiles[tile_no]    
          

def draw_grid():
        for x in range(BOARD_SIZE_X):
            for y in range(BOARD_SIZE_Y):
                pg.draw.rect(screen, GRAY,
                        (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE,CELL_SIZE), 2)
                

def runGame():
    global done
   
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pg.event.get():        
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                x_pos = event.pos[0] // CELL_SIZE
                y_pos = event.pos[1] // CELL_SIZE
                tile_no = x_pos + y_pos * BOARD_SIZE_Y
                tile= Tiles(tile_no, x_pos, y_pos)
                
                # print (tiles)

                tile.move(tile_no)
                
                # print (tiles)

                for index in range(len(tiles)):
                
                    tile_no= tiles[index]
                    # print( tile_no)
                    x_pos = index  % BOARD_SIZE_X
                    y_pos = index  // BOARD_SIZE_Y
                    tile= Tiles(index, x_pos, y_pos)
                    if tile_no == 0:
                        color = BLACK
                    else :
                        color = WHITE    
                    tile.draw(color) 
               
                # print (x_pos, y_pos)
            # print('////////////////') 
            # print(tiles)   
            # print(len(tiles))
                    draw_grid()
                pg.display.update()
            
if __name__ == '__main__':                  
    runGame()
    pg.quit()
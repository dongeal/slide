import pygame as pg # 1. 파이게임 불러오기
from random import  randint

pg.init()           # 2. 초기화

SCRAMBLE_NO= 100
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128,128,128)
RED = (255,0,0)
CELL_SIZE = 100
BOARD_SIZE_X = 4
BOARD_SIZE_Y = 4

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
for index in range(1, BOARD_SIZE_X * BOARD_SIZE_Y ):
    tiles.append(index)  # [1, 2, ....., 15]
tiles.append(0)         # [1, 2, ....., 15,0]
print(tiles)
# tiles =[x for x in range(COLUMN_COUNT * BOARD_SIZE_X)] 
# tile_colors = {0:BLACK}
# for index in range(0, COLUMN_COUNT * BOARD_SIZE_X):
#     tile_colors[index]= WHITE
# shuffle(tiles)

class Tiles :
    def __init__(self, tile_no, x_pos, y_pos, color):
        self.tile_no = tile_no
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
    
    def scramble(self):
        for index in range(1,SCRAMBLE_NO):
            x_pos = randint(0, BOARD_SIZE_X-1)
            y_pos = randint(0, BOARD_SIZE_Y-1)
            tile_no = x_pos + y_pos * BOARD_SIZE_Y
            if tile_no == 0:
                    color = BLACK
            else :
                    color = WHITE    
            tile= Tiles(tile_no, x_pos, y_pos, color)
            tile.move()
            
            for index in range(len(tiles)):               
                tile_no= tiles[index]
                # print( self.tile_no)
                x_pos = index  % BOARD_SIZE_X
                y_pos = index  // BOARD_SIZE_Y
                if tile_no == 0:
                    color = BLACK
                else :
                    color = WHITE    

                tile= Tiles(index, x_pos, y_pos, color)
                tile.draw() 
                draw_grid()
          
                pg.display.update()
            clock.tick(30)
    def check_win(self):
        global check, poor
        check = False
        poor = False
        check_data= 0
        check_poor= 0
        for index in range(1,BOARD_SIZE_X * BOARD_SIZE_Y):
            if index == tiles[index-1]:
                check_data += 1
            print (index, tiles[index-1])    
        if check_data == BOARD_SIZE_X * BOARD_SIZE_Y -1 :
            check = True  
        for index in range(1,BOARD_SIZE_X * BOARD_SIZE_Y-2):
            if index == tiles[index-1]:
                check_poor += 1
        if check_poor == BOARD_SIZE_X * BOARD_SIZE_Y -3 and \
            BOARD_SIZE_X * BOARD_SIZE_Y-2 == tiles[BOARD_SIZE_X * BOARD_SIZE_Y-2] and \
            BOARD_SIZE_X * BOARD_SIZE_Y-1 == tiles[BOARD_SIZE_X * BOARD_SIZE_Y-3]:
            poor = True
            
        print (check_data,check_poor, BOARD_SIZE_X * BOARD_SIZE_Y -2,tiles[BOARD_SIZE_X * BOARD_SIZE_Y-2] \
                 ,BOARD_SIZE_X * BOARD_SIZE_Y -1,tiles[BOARD_SIZE_X * BOARD_SIZE_Y-3])

        return check, poor

    def draw(self):
        # print(color, self.self.tile_no, self.x_pos, self.y_pos)
        pg.draw.rect(screen, self.color,
                 (self.x_pos * CELL_SIZE, self.y_pos * CELL_SIZE,
                   CELL_SIZE,CELL_SIZE))    
        NO_TAG = game_font.render(str(tiles[self.tile_no]), True, BLACK)
                    # 출력할 글자, 안티 알리아스  True, 글자 색상
        screen.blit(NO_TAG, (int((self.x_pos +0.2) * CELL_SIZE),int((self.y_pos+0.2) * CELL_SIZE)))
       
            
    def move(self):

        if tiles[self.tile_no] != 0 : 

            if self.tile_no-BOARD_SIZE_X >= 0:        
                if tiles[self.tile_no-BOARD_SIZE_X] == 0:        # 위쪽   0
                    tiles[self.tile_no],tiles[self.tile_no-BOARD_SIZE_X]= tiles[self.tile_no-BOARD_SIZE_X],tiles[self.tile_no]
            if self.tile_no+BOARD_SIZE_X < len(tiles) :
                if tiles[self.tile_no+BOARD_SIZE_X] == 0 :           # 아래 0
                    tiles[self.tile_no],tiles[self.tile_no+BOARD_SIZE_X]= tiles[self.tile_no+BOARD_SIZE_X],tiles[self.tile_no]
            if self.tile_no+1 < len(tiles):    
                if tiles[self.tile_no+1] == 0:                     # 오른쪽 0  
                    tiles[self.tile_no],tiles[self.tile_no+1]= tiles[self.tile_no+1],tiles[self.tile_no]    
            if self.tile_no-1 >= 0:     
                if tiles[self.tile_no-1] == 0:                     # 왼쪽 0  
                    tiles[self.tile_no],tiles[self.tile_no-1]= tiles[self.tile_no-1],tiles[self.tile_no]    
        
def draw_grid():
        for x in range(BOARD_SIZE_X):
            for y in range(BOARD_SIZE_Y):
                pg.draw.rect(screen, GRAY,
                        (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE,CELL_SIZE), 2)
                

def runGame():
    global done

    for index in range(len(tiles)):               
        tile_no= tiles[index]
        # print( self.tile_no)
        x_pos = index  % BOARD_SIZE_X
        y_pos = index  // BOARD_SIZE_Y
        if tile_no == 0:
            color = BLACK
        else :
            color = WHITE    

        tile= Tiles(index, x_pos, y_pos, color)
        tile.draw() 
        draw_grid()
    pg.display.update()
    tile.scramble()

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
                if tile_no == 0:
                        color = BLACK
                else :
                        color = WHITE    
                tile= Tiles(tile_no, x_pos, y_pos, color)
                
                # print (tiles)

                tile.move()
                tile.check_win()
                print(check)
                print(poor)

                for index in range(len(tiles)):               
                    tile_no= tiles[index]
                    # print( self.tile_no)
                    x_pos = index  % BOARD_SIZE_X
                    y_pos = index  // BOARD_SIZE_Y
                    if tile_no == 0:
                        color = BLACK
                    else :
                        color = WHITE    

                    tile= Tiles(index, x_pos, y_pos, color)
                    tile.draw() 
                    draw_grid()

                    if check :
                        win_msg = game_font.render('Good!', True, RED)
                    # 출력할 글자, 안티 알리아스  True, 글자 색상
                        screen.blit(win_msg, (SCREEN_WIDTH // 5,SCREEN_HEIGHT //3 ))
                        # print (tiles)
                    elif poor:
                        win_msg = game_font.render('Oh No!', True, RED)
                    # 출력할 글자, 안티 알리아스  True, 글자 색상
                        screen.blit(win_msg, (SCREEN_WIDTH // 5,SCREEN_HEIGHT //3 ))
                        # print (tiles)

                    pg.display.update()
            
if __name__ == '__main__':                  
    runGame()
    pg.quit()
import pygame #파이 게임 모듈 임포트
from random import randint, shuffle

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock() 



#변수

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CELL_SIZE = 200
COLUMN_COUNT = 3
ROW_COUNT = 3

game_font = pygame.font.Font(None, CELL_SIZE) # 폰트 객체 생성 (폰트, 크기)

tiles =[x for x in range(COLUMN_COUNT * ROW_COUNT)] 
blocks= {0:BLACK}
for index in range(1, COLUMN_COUNT * ROW_COUNT):
    blocks[index]= WHITE
print(blocks)
rnd_blocks = shuffle(blocks)
print(rnd_blocks)

def tile_move(row_index, column_index):
    tile_no = row_index + column_index * COLUMN_COUNT
    if tiles[tile_no] != 0 : 

        if tile_no-COLUMN_COUNT >= 0:        
            if tiles[tile_no-COLUMN_COUNT] == 0:        # 위쪽   0
                tiles[tile_no],tiles[tile_no-COLUMN_COUNT]= tiles[tile_no- COLUMN_COUNT],tiles[tile_no]
        if tile_no+ROW_COUNT < len(tiles) :
            if tiles[tile_no+ROW_COUNT] == 0 :           # 아래 0
                tiles[tile_no],tiles[tile_no+ROW_COUNT]= tiles[tile_no+ROW_COUNT],tiles[tile_no]
        if tile_no+1 < len(tiles):    
            if tiles[tile_no+1] == 0:                     # 오른쪽 0  
                tiles[tile_no],tiles[tile_no+1]= tiles[tile_no+1],tiles[tile_no]    
        if tile_no-1 >= 0:     
            if tiles[tile_no-1] == 0:                     # 왼쪽 0  
                tiles[tile_no],tiles[tile_no-1]= tiles[tile_no-1],tiles[tile_no]    
        
    # if rnd_tiles[row_index -1 + column_index * COLUMN_COUNT] == 0:
    #     rnd_tiles[row_index+ column_index * COLUMN_COUNT], rnd_tiles[row_index -1 + column_index * COLUMN_COUNT] = \
    #         rnd_tiles[row_index -1 + column_index * COLUMN_COUNT], rnd_tiles[row_index+ column_index * COLUMN_COUNT]      

def draw_block(color,row_index,column_index):
    tile_no = row_index + column_index * COLUMN_COUNT
    pygame.draw.rect(screen, color , pygame.Rect
                     (column_index * CELL_SIZE+1, row_index * CELL_SIZE+1,
                       CELL_SIZE-1, CELL_SIZE-1))
    
    # print(color, self.self.tile_no, self.x_pos, self.y_pos)
    # pg.draw.rect(screen, self.color,
    #             (self.x_pos * CELL_SIZE, self.y_pos * CELL_SIZE,
    #             CELL_SIZE,CELL_SIZE))    
    NO_TAG = game_font.render(str(tiles[tile_no]), True, BLACK)
                # 출력할 글자, 안티 알리아스  True, 글자 색상
    screen.blit(NO_TAG, (int((row_index +0.2) * CELL_SIZE),int((column_index+0.2) * CELL_SIZE)))
       


while True: #게임 루프
    screen.fill(BLACK) #단색으로 채워 화면 지우기

    #변수 업데이트

    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN:
        column_index = event.pos[0] // CELL_SIZE
        row_index = event.pos[1] // CELL_SIZE
        tile_move(row_index, column_index)
 
 #화면 그리기
    for x in range(len(blocks)):
        column_index = int(x % COLUMN_COUNT)
        row_index = int(x // ROW_COUNT)
        tile_order = x
        tile_no= tiles[x]
        color = tiles[tile_no]
      
        draw_block(color,row_index,column_index)

        print(column_index, row_index,tile_order, tile_no ,color)    

#모든 화면 그리기 업데이트
    pygame.display.update() 
    clock.tick(20) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit() 
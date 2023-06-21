import pygame as pg # 1. 파이게임 불러오기
import sys
from datetime import datetime
from datetime import timedelta
import random


pg.init()           # 2. 초기화

                    # 3. 사용될 전역 변수 선언
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
GRAY = (200,200,200)

FIELD_W, FIELD_H = (20, 20)
block_size = 20
size = [FIELD_W * block_size, FIELD_H * block_size]

screen = pg.display.set_mode(size)
pg.display.set_caption('Snake')


done = False
clock = pg.time.Clock()
last_moved_time = datetime.now()
last_dir = 'E'

KEY_DIRECTION ={pg.K_UP:'N', pg.K_DOWN:'S',
                pg.K_LEFT:'W', pg.K_RIGHT:'E'}

def draw_grid():
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(screen, GRAY,
                        (x * block_size, y * block_size, block_size,block_size), 1)
                


def draw_block(screen,color,position):
    block = pg.Rect((position[0] * block_size , position[1] * block_size),
                    (block_size,block_size))
    pg.draw.rect(screen, color, block)


class Snake:
    def __init__(self):
        self.positions = [(2,0),(1,0),(0,0)] # 뱀의 위치 (2,0)이 머리
        self.direction = ''
       
    def draw(self):
        for position in self.positions:
            draw_block(screen, GREEN, position)
    
    def move(self):
        global last_dir
        head_position =self.positions[0]
        x, y = head_position
        print(self.direction, last_dir)
        if self.direction =='N' and last_dir !='S':
            if y-1 < 0 :
                self.direction = random.choice(['W','E'])
                last_dir = self.direction
            else:
                print('X')
                self.positions=[(x, y-1)] + self.positions[:-1]
                last_dir = self.direction
        elif self.direction =='S'and last_dir !='N':
            if y+1 > FIELD_H -1 :
                self.direction = random.choice(['W','E'])
                last_dir = self.direction
            else:
               self.positions=[(x, y+1)] + self.positions[:-1]
               last_dir = self.direction
        elif self.direction =='W' and last_dir != 'E':
            if x-1 <0 :
                self.direction = random.choice(['S','N'])
                last_dir = self.direction
            else:
                self.positions=[(x-1, y)] + self.positions[:-1]
                last_dir = self.direction
        elif self.direction =='E' and last_dir !='W':
            if x+1 > FIELD_W-1:
                self.direction = random.choice(['S','N'])
                last_dir = self.direction
            else:    
                self.positions=[(x+1, y)] + self.positions[:-1]
                last_dir = self.direction
        
        
    
    
    def grow(self):
        tail_position = self.positions[-1]
        x, y = tail_position
        if self.direction == 'N':
            self.positions.append((x, y - 1))
        elif self.direction == 'S':
            self.positions.append((x, y + 1))
        elif self.direction == 'W':
            self.positions.append((x - 1, y))
        elif self.direction == 'E':
            self.positions.append((x + 1, y))    
        
 
class Apple:
    def __init__(self, position =(5,5)):
        self.position= position

    def draw(self):
        draw_block(screen,RED, self.position)

                    # 4. pygame 무한루프

def runGame():
    global done, last_moved_time
    
    # 게임 시작시 뱀과 사과를 초기화
    snake = Snake()
    apple = Apple()

    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pg.event.get():        
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction = KEY_DIRECTION[event.key]  
               
            
    # 마지막 움직인시간 에서 0.5초 보다 크면 자동으로 가던 방향으로 움직임
        if datetime.now() - last_moved_time >= timedelta(seconds=0.5):
           last_dir = snake.direction
           snake.move()
           last_moved_time =datetime.now() # 자동움직임 뒤에도 시간 기록
        if snake.positions[0] == apple.position:
            snake.grow()    
            apple.position = (random.randint(0, 19), random.randint(0, 19))

        if snake.positions[0] in snake.positions[2:]:
            done = True


        draw_grid()
        snake.draw()
        apple.draw()
        pg.display.update()
            
runGame()
pg.quit()
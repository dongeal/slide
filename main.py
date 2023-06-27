import pygame
import random
import time
from sprite import *
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def create_game(self):
        grid =[[x + y *GAME_SIZE for x in range(1, GAME_SIZE + 1)] \
               for y in range(GAME_SIZE)]
        grid[-1][-1] = 0
        print(grid)

    def new(self):
        self.create_game()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
           
    def update(self):
        pass

    def draw_grid(self):
        for row in range(-1, GAME_SIZE * TILESIZE, TILESIZE): # 세로 줄
            pygame.draw.line(self.screen, LIGHTGREY, (row, 0), (row, GAME_SIZE * TILESIZE))    
        for col in range(-1, GAME_SIZE * TILESIZE, TILESIZE): # 가로 줄
            pygame.draw.line(self.screen, LIGHTGREY, (0, col), (GAME_SIZE * TILESIZE, col))  

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)


game = Game()
while True:
    game.new()
    game.run()
    
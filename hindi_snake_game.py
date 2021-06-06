import pygame
from pygame.locals import *

class Snake:

    def __init__(self, parent_screen):
        
        self.parent_screnn = parent_screen
        self.block = pygame.image.load("ressources/block.jpg").convert()
        self.x = 255
        self.y = 255
    
    def draw(self):
        
        self.parent_screnn.fill((110, 110, 5))
        self.parent_screnn.blit(self.block, (self.x, self.y))
        pygame.display.flip()
    
    def move_left(self):
        self.x -=10
        self.draw()
    
    def move_right(self):
        self.x +=10
        self.draw()
    
    def move_up(self):
        self.y -=10
        self.draw()
    
    def move_down(self):
        self.y +=10
        self.draw()


class Game:
    def __init__(self):
        
        pygame.init()

        self.surface = pygame.display.set_mode((600, 600))
        self.surface.fill((110, 110, 5))
        self.snake = Snake(self.surface)
        self.snake.draw()
    


    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                    

                    if event.key == K_DOWN:
                        self.snake.move_down()
                    

                    if event.key == K_LEFT:
                        self.snake.move_left()
                    

                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    


                elif event.type == QUIT:
                    running = False




if __name__ == "__main__":
   
    game = Game()
    game.run()
























    












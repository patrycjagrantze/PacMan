from pygame.locals import *
import pygame as pg
import glob
import os


class Direction:
    FORWARD = 1
    BACKWARD = 2
    UPWARD = 3
    DOWNWARD = 4


class Pacman():
    x = None
    y = None
    heart = None
    direction = None
    
    
    def __init__(self, x, y, direction,heart, current_score, WalkCount_x, WalkCount_y):
        self.x = x
        self.y = y
        self.heart = heart
        self.direction = direction
        self.grid_pos = [self.x, self.y]
        self.current_score = current_score
        self.WalkCount_x = WalkCount_x
        self.WalkCount_y = WalkCount_y
        return
    
    def update(self):
        pass
    
    def draw(self, screen, x_pos, y_pos, direction_):
        pacman = pg.image.load("pacman_2.png")
        if direction_ == 1:
            angle = 0
            surf = pg.transform.rotate(pacman, angle)    
            screen.blit(surf, (x_pos, y_pos))
        elif direction_ == 2:
            angle = 0
            surf = pg.transform.rotate(pacman, angle)    
            screen.blit(pg.transform.flip(pacman, True, False), (x_pos, y_pos))
        elif direction_ == 3:
            angle = 270
            surf = pg.transform.rotate(pacman, angle)    
            screen.blit(surf, (x_pos, y_pos))
        elif direction_ == 4:
            angle = 90
            surf = pg.transform.rotate(pacman, angle)    
            screen.blit(surf, (x_pos, y_pos))
        
        
   
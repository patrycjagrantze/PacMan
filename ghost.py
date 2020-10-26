from pygame.locals import *
import pygame as pg
import glob
import os


class Ghost():
    x = None
    y = None
    direction = None
    number_ghost = None
    
    
    def __init__(self,number_ghost, x, y, direction, WalkCount_x, WalkCount_y):
        self.number_ghost = number_ghost
        self.x = x
        self.y = y
        self.direction = direction
        self.WalkCount_x = WalkCount_x
        self.WalkCount_y = WalkCount_y
        return
    
    def draw(self,number_ghost_, screen, x_pos, y_pos, direction_):
        if number_ghost_ == 1:
            ghost_1 = pg.image.load("ghost_1.png")
            if direction_ == 1:
                angle = 0
                surf = pg.transform.rotate(ghost_1, angle)    
                screen.blit(surf, (x_pos, y_pos))
            elif direction_ == 2:
                angle = 0
                surf = pg.transform.rotate(ghost_1, angle)    
                screen.blit(pg.transform.flip(ghost_1, True, False), (x_pos, y_pos))
            elif direction_ == 3:
                angle = 270
                surf = pg.transform.rotate(ghost_1, angle)    
                screen.blit(surf, (x_pos, y_pos))
            elif direction_ == 4:
                angle = 90
                surf = pg.transform.rotate(ghost_1, angle)    
                screen.blit(surf, (x_pos, y_pos))
        elif number_ghost_ ==2:
            ghost_2 = pg.image.load("ghost_2.png")
            if direction_ == 1:
                angle = 0
                surf = pg.transform.rotate(ghost_2, angle)    
                screen.blit(surf, (x_pos, y_pos))
            elif direction_ == 2:
                angle = 0
                surf = pg.transform.rotate(ghost_2, angle)    
                screen.blit(pg.transform.flip(ghost_2, True, False), (x_pos, y_pos))
            elif direction_ == 3:
                angle = 270
                surf = pg.transform.rotate(ghost_2, angle)    
                screen.blit(surf, (x_pos, y_pos))
            elif direction_ == 4:
                angle = 90
                surf = pg.transform.rotate(ghost_2, angle)    
                screen.blit(surf, (x_pos, y_pos))
        elif number_ghost_ ==3:
            ghost_3 = pg.image.load("ghost_3.png")
            if direction_ == 1:
                angle = 0
                surf = pg.transform.rotate(ghost_3, angle)    
                screen.blit(surf, (x_pos, y_pos))
            elif direction_ == 2:
                angle = 0
                surf = pg.transform.rotate(ghost_3, angle)    
                screen.blit(pg.transform.flip(ghost_3, True, False), (x_pos, y_pos))
            elif direction_ == 3:
                angle = 270
                surf = pg.transform.rotate(ghost_3, angle)    
                screen.blit(surf, (x_pos, y_pos))
            elif direction_ == 4:
                angle = 90
                surf = pg.transform.rotate(ghost_3, angle)    
                screen.blit(surf, (x_pos, y_pos))
from pygame.locals import *
import pygame as pg
import glob
import os
import pacman
import ghost
import numpy as np
from const import *
import random
import time

#stałe pomocnicze
vec = pg.math.Vector2
global screen, tile
global WalkCount_x, WalkCount_y

#okno
FLAGS = pg.DOUBLEBUF | pg.HWSURFACE
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % WINDOW_POSITION
pg.init()
screen = pg.display.set_mode(WINDOW_SIZE, FLAGS)


#tytuł okna "Pacman"
pg.display.set_caption("Pacman")
#tło
bg = pg.image.load("pacman_original_map.png")
#wczytywanie mapy z pliku .txt gdzie X- walls, O -droga 
map_lvl1 = open("pacman_map_2.txt", "r")
road_ghost = open("road_ghost.txt", "r")


input = np.loadtxt("pacman_map.txt", dtype='i', delimiter=',')
#print(input)
#print(input[0,0])
#mapa dla pierwszego ducha


#wyswietlanie wyniku na ekranie
def draw_text(words, screen, pos, size, colour, font_name, centered=False):
        font = pg.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)




def START_SCREEN():
    screen.fill(BLACK)
    draw_text('PUSH SPACE BAR', screen, [
                       WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2-50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
    pg.display.update()
    loop =1 
    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = 0   
            if  event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    loop =0

def GAME_OVER_SCREEN(status_game):
    if status_game == 'win':
        screen.fill(BLACK)
        draw_text('YOU WIN!', screen, [
                       WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2-50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        pg.display.update()
        loop =1 
        while loop:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    loop = 0   
                if  event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        loop =0
    elif status_game == 'game_over':
        screen.fill(BLACK)
        draw_text('YOU LOSE! TRY AGAIN', screen, [
                       WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2-50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        pg.display.update()
        loop =1 
        while loop:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    loop = 0   
                if  event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        loop =0


#dodawanie wspólrzednych monet z planszy
coins = []
for y, line in enumerate(map_lvl1):
    for x, c in enumerate(line):
        if x ==1 and y == 1:
            print("pozycja startowa")
        else:
            if c == '0':
                coins.append([x,y])
                
    

# usuwamy pierwszą monetke z pozycji startującej

#print(coins)



road = []
for y, line in enumerate(road_ghost):
    #print(line)
    for x, c in enumerate(line):
        if c == '0':
            road.append([x,y])

#print(road)

def ghost_move(ghost):
    
    x = int((ghost.x + ghost.WalkCount_x)/30)
    y = int((ghost.y + ghost.WalkCount_y)/30)
    possible_direction = []
    if [x-1,y] in road:
        possible_direction.append(1)
    if [x+1,y] in road:
        possible_direction.append(2)
    if [x, y-1] in road:
        possible_direction.append(3)
    if [x, y+1] in road:
        possible_direction.append(4)
    if len(possible_direction) == 0:
        print("brak mozliwych ruchów")
        
    #print(len(possible_direction))
    #print("x : ", x)
    #print("y:", y)
    if ghost.direction == 2:
        if 1 in possible_direction:
            possible_direction.remove(1)
    elif ghost.direction == 1:
        if 2 in possible_direction:
            possible_direction.remove(2)
    elif ghost.direction == 3:
        if 4 in possible_direction:
            possible_direction.remove(4)
    elif ghost.direction == 4:
        if 3 in possible_direction:
            possible_direction.remove(3)
    #print(len(possible_direction))
    #print(possible_direction) 
    ghost.direction = random.choice(possible_direction)
    if ghost.direction == 1:
        ghost.WalkCount_x = ghost.WalkCount_x -30
    elif ghost.direction == 2:
        ghost.WalkCount_x = ghost.WalkCount_x +30
    elif ghost.direction == 3:
        ghost.WalkCount_y = ghost.WalkCount_y -30
    elif ghost.direction == 4:
        ghost.WalkCount_y = ghost.WalkCount_y + 30
        
    time.sleep( 0.05 )


def collision_check(ghost_1_, ghost_2_, ghost_3_, pacman):
    if ghost_1_.x + ghost_1_.WalkCount_x == pacman.x + pacman.WalkCount_x and ghost_1_.y + ghost_1_.WalkCount_y == pacman.y + pacman.WalkCount_y :
        status_game = 'game_over'
        GAME_OVER_SCREEN(status_game)
    if ghost_2_.x + ghost_2_.WalkCount_x == pacman.x + pacman.WalkCount_x and ghost_2_.y + ghost_2_.WalkCount_y == pacman.y + pacman.WalkCount_y:
        status_game = 'game_over'
        GAME_OVER_SCREEN(status_game)
    if ghost_3_.x + ghost_3_.WalkCount_x == pacman.x + pacman.WalkCount_x and ghost_3_.y + ghost_3_.WalkCount_y == pacman.y + pacman.WalkCount_y:
        status_game = 'game_over'
        GAME_OVER_SCREEN(status_game)
    
                    

status_game = 'game'

def MainLoop():
    loop = 1
    #licznik kroków zaRówno góra-dół jak i lewo-prawo
    while loop:
        ghost_move(ghost_1)
        ghost_move(ghost_2)
        ghost_move(ghost_3)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = 0   
            if  event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT or event.key == ord('a'):
                        pacman.direction =  2
                        checking = check()
                        if checking[0] == 1:
                            print("kolizja")
                        elif checking[0] == 0:
                            pacman.WalkCount_x = pacman.WalkCount_x - 30    
                         
                        eat_coins(pacman.x+pacman.WalkCount_x, pacman.y+pacman.WalkCount_y)
                    if event.key == pg.K_RIGHT or event.key == ord('d'):
                        pacman.direction = 1
                        checking = check()
                        if checking[0] == 1:
                            print("kolizja")
                        elif checking[0] == 0:
                            pacman.WalkCount_x = pacman.WalkCount_x +30
                            print("brak kolizji")
                        eat_coins(pacman.x+pacman.WalkCount_x, pacman.y+pacman.WalkCount_y)
                    if event.key == pg.K_UP or event.key == ord('w'):
                        pacman.direction=4
                        checking = check()
                        if checking[1] == 1:
                            print("kolizja")
                        elif checking[1] == 0:
                            pacman.WalkCount_y = pacman.WalkCount_y -30
                            print("brak kolizji")
                        eat_coins(pacman.x+pacman.WalkCount_x, pacman.y+pacman.WalkCount_y)
                    if event.key == pg.K_DOWN or event.key == ord('s'):
                        pacman.direction = 3
                        checking = check()
                        if checking[1] == 1:
                            print("kolizja")
                        elif checking[1] == 0:
                            pacman.WalkCount_y = pacman.WalkCount_y +30
                            print("brak kolizji")
                        eat_coins(pacman.x+pacman.WalkCount_x, pacman.y+pacman.WalkCount_y)
        collision_check(ghost_1, ghost_2, ghost_3, pacman)
        
        redrawGame()
        
    pg.quit()




#rysowanie monet z aktualnej listy coins[]
def draw_coins():
    for coin in coins:
        x = coin[0]
        y = coin[1]
        pg.draw.circle(screen,YELLOW ,
                               (int(x*sprite_size+ sprite_size//2),
                                int(y*sprite_size+ sprite_size//2)), 5)

#funkcja sprawdzająca czy nasza postać jest w miejscu gdzie do "zjedzenia " są jeszcze jakies monety
#jesli są usuwa je z listy i dostajemy punkt
def eat_coins(x_, y_):
    x_ = int(x_/sprite_size)
    y_ = int(y_/sprite_size)
    if [x_, y_] in coins:
        coins.remove([x_, y_])
        pacman.current_score = pacman.current_score +1
        if pacman.current_score == 200:
            status_game = 'win'
            GAME_OVER_SCREEN(status_game)
    else:
        print("zjedzone")
    return coins
    


#funkcja sprawdzająca czy nasz ruch może zostać wykonany czy być może nie wsytępuje kolizja ze scianą
def collision(x,y,direction):
    if direction == 2:
        x = int((x-step_x)/sprite_size)
        y = int(y/sprite_size)
        return [x,y]
    elif direction ==1:
        x = int((x+step_x)/sprite_size)
        y = int(y/sprite_size)
        return [x,y]
    elif direction == 3:
        x = int(x/sprite_size)
        y = int((y+step_y)/sprite_size)
        return [x,y]
    elif direction == 4:
        x = int(x/sprite_size)
        y = int((y-step_y)/sprite_size)
        return [x,y]
#funkcja pomocnicza przy sprawdzaniu kolizji   
def check():
    dx = 0
    dy = 0
    k = 0 
    if pacman.direction ==2:
        check = collision(pacman.x+pacman.WalkCount_x, pacman.y +pacman.WalkCount_y, pacman.direction)
        x = check[0]
        y  = check[1]
        k = input[y,x]
        #print(x)
        #print(y)
        if k == 1:
            #print("kolizja")
            dx = 1
        elif k ==0:
            dx = 0
    elif pacman.direction == 1:
        check = collision(pacman.x+pacman.WalkCount_x, pacman.y+pacman.WalkCount_y, pacman.direction)
        x = check[0]
        y  = check[1]
        k = input[y,x]
        #print(k)
        if k == 1:
            #print("kolizja")
            dx = 1
        elif k ==0:
            dx = 0
    elif pacman.direction == 3:
        check = collision(pacman.x+pacman.WalkCount_x, pacman.y+pacman.WalkCount_y, pacman.direction)
        x = check[0]
        y  = check[1]
        k = input[y,x]
        if k == 1:
            #print("kolizja")
            dy = 1
        elif k ==0:
            dy = 0
    elif pacman.direction == 4:
        check = collision(pacman.x+pacman.WalkCount_x, pacman.y+pacman.WalkCount_y, pacman.direction)
        x = check[0]
        y  = check[1]
        k = input[y,x]
        if k == 1:
            #print("kolizja")
            dy = 1 
        elif k ==0:
            dy = 0
    return dx, dy

#206

#funkcja rysująca grę w aktualnym stanie (np po poruszeniu Pacmana)            
def redrawGame():
    screen.blit(bg, (0,0))
    pacman.draw(screen, pacman.x + pacman.WalkCount_x , pacman.y + pacman.WalkCount_y , pacman.direction)
    draw_coins()
    ghost_1.draw(1,screen, ghost_1.x + ghost_1.WalkCount_x, ghost_1.y + ghost_1.WalkCount_y, ghost_1.direction)
    ghost_2.draw(2,screen, ghost_2.x + ghost_2.WalkCount_x, ghost_2.y + ghost_2.WalkCount_y, ghost_2.direction)
    ghost_3.draw(3,screen, ghost_3.x + ghost_3.WalkCount_x, ghost_3.y + ghost_3.WalkCount_y, ghost_3.direction)
    
    draw_text('Twój wynik: {}'.format(pacman.current_score),
                       screen, [60, 0], 18, WHITE, START_FONT)
    pg.display.update()





#Tworzymy postać Pacmana i przypisujemy go do pacman
pacman = pacman.Pacman(30,30,1,3, 0, 0, 0)
#tworzymy przeciwników
ghost_1 = ghost.Ghost(1, 270, 30, 2, 0, 0)
ghost_2 = ghost.Ghost(2, 570, 600, 2, 0, 0)
ghost_3 = ghost.Ghost(3, 570, 30, 2, 0, 0)

#GłóWna pętla, w której wywołóujemy grę
START_SCREEN()
MainLoop()
# plotEquation.py
# Chris Franklin
# November 13, 2014

import pygame, sys
from pygame.locals import *

# setup pygame
pygame.init()

#setup up the window
windowSurface = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('Equation Plot')

# set up the colors
# refer to http://www.rapidtables.com/web/color/RGB_Color.htm
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)
YELLOW = (255,255,0)
BROWN = (139,69,19)
PINK = (255,20,147)

# set up the fonts
basicFont = pygame.font.SysFont(None,48)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# draw the white background
windowSurface.fill(WHITE)

#draw some blue lines onto the surface
pygame.draw.line(windowSurface, BLACK, (0,200), (400,200), 4)
pygame.draw.line(windowSurface, BLACK, (200,0), (200,400), 4)

for i in range(-20,31):
    x = i + 200
    y = int( (i**2)/5 - 3*i ) + 200
    print ('x = ' + str(x-200) + '; y = ' + str(y - 200))
    
    # draw point as a 2x2 pixel square
    pygame.draw.line(windowSurface, RED, [(400-x),(400-y)], [(398 - x),(400 - y)], 2)


# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)


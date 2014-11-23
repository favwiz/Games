# ConnectFour.py
# Chris Franklin
# Connect Four Game
# October 1, 2014

# location (width, hieght)
import pygame, sys
from pygame.locals import *

# setup pygame
pygame.init()

#setup up the window
windowSurface = pygame.display.set_mode((550, 475), 0, 32)
pygame.display.set_caption('Connect Four')

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

# draw the yellow background
windowSurface.fill(YELLOW)

# draw a white circles on the surface
xloc = 50
yloc = 50
for i in range(0,7):
    yloc = 50
    for j in range(0,6):
        pygame.draw.circle(windowSurface, WHITE, (xloc,yloc), 30, 0)
        yloc = yloc + 75
    xloc = xloc + 75

# draw a blue circle
pygame.draw.circle(windowSurface, BLUE, (125,350), 30, 0)
pygame.draw.circle(windowSurface, BLUE, (125,425), 30, 0)
pygame.draw.circle(windowSurface, RED, (200,425), 30, 0)

# draw the window onto the screen
pygame.display.update()


# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

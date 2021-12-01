# pygame practice, jarodkyles, 11/19/2021 9:14am, v0.5

import pygame,sys
from pygame.locals import *

#start pygame
pygame.init()

#create game window 
window surface = pygame.display. set_mode((500,400),0,32)
pygame.display.set_caption("hello,world")

#set color values
black = (0, 0, 0)
white = (255,255,255)
red   = (255,0, 0)
green = (0,255 ,0)
blue  = (0,0,255)

# setup fonts
basicfont = pygame.font.sysfont(none,48)

#setup text
text = basicfont.render("hello,world",true, white,blue)
text rect = text.get_rect()
textrect.centerx = windowsurface.get_rect().centerx
textrect.centery = windowsurface.get_rect().centery


import pygame, sys, video
import os,number

from pygame.locals import *

# Color
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

WINDOWWIDTH = 1280 # Chiều dài cửa sổ
WINDOWHEIGHT = 720 # Chiều cao cửa sổ

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

# Screen, Caption, Background
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Poker')
background = pygame.image.load("Resource/poker_green_background.jpg")
background = pygame.transform.scale(background, (1280, 720))

# Icon
icon = pygame.image.load("Resource/poker_cards_icon.png")
pygame.display.set_icon(icon)

# Font
fontHeading = pygame.font.Font('Resource/Calibri Bold.TTF', 96)
fontInline = pygame.font.Font('Resource/Calibri Bold.TTF', 64)

# Logo
class Logo():
    def __init__(self):
        self.surface = pygame.image.load('Resource/poker_logo.png')
        self.surface = pygame.transform.scale(self.surface, (400, 400))

    def draw(self):  # Hàm dùng để vẽ xe
        screen.blit(self.surface, (432,0))
logo = Logo()



def Single_Player(x, y,mouse_position,click):
    singleplayer = fontInline.render("Single Player", True, (255,255,255))
    screen.blit(singleplayer, (x,y))
    rect = pygame.Rect(448, 320, 376, 72)
    #pygame.draw.rect(screen, (0, 0, 0), rect, 1)
    if rect.collidepoint((mouse_position)):
        if click==True:
            number.current_screen = 7

def Multiplayer(x, y,mouse_position,click):
    multiplayer = fontInline.render("Multiplayer", True, (255, 255, 255))
    screen.blit(multiplayer, (x, y))

def Guide(x, y,mouse_position,click):
    guide = fontInline.render("Guide", True, (255, 255, 255))
    screen.blit(guide, (x, y))
    rect = pygame.Rect(544, 464, 176, 72)
    #pygame.draw.rect(screen, (0, 0, 0), rect, 1)
    if rect.collidepoint((mouse_position)):
        if click == True:
            '''pygame.quit()
            os.system('option.py')'''
            number.current_screen = 1

def Option(x, y,mouse_position,click):
    option = fontInline.render("Option", True, (255, 255, 255))
    screen.blit(option, (x, y))
    rect = pygame.Rect(520, 536, 216, 72)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen=2


def Exit(x, y,mouse_position,click):
    exit = fontInline.render("Exit", True, (255, 255, 255))
    screen.blit(exit, (x, y))
    rect = pygame.Rect(568, 608, 136, 72)
    if rect.collidepoint((mouse_position)):
        if click==True:
            pygame.quit()
            sys.exit()

def mainmenux():
    click=False
    logo = Logo()
    mouse_position = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #video.Res1920x1080(474, 584, mouse_position, click)
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            number.Sound.click_channel.play(number.Sound.click_sound)
            click=True

    logo.__init__()
    logo.draw()
    Single_Player(472,328,mouse_position,click)
    Multiplayer(480,400,mouse_position,click)
    Guide(552,472,mouse_position,click)
    Option(536,544,mouse_position,click)
    Exit(584,616,mouse_position,click)
    pygame.display.update()
    fpsClock.tick(FPS)
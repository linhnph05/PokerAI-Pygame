import number,video
import pygame, sys
import os
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

#Return Arrow
reArrow = pygame.image.load('Resource/return_arrow.png')
reArrow = pygame.transform.scale(reArrow, (160, 160))
background = pygame.transform.scale(background, (1280, 720))

# Font
fontHeading = pygame.font.Font('Resource/Calibri Bold.TTF', 96)
fontInline = pygame.font.Font('Resource/Calibri Bold.TTF', 64)


def Option(x, y,mouse_position,click):
    option = fontHeading.render("Option", True, (255,255,255))
    screen.blit(option, (x,y))

# def Video(x, y,mouse_position,click):
#     rect = pygame.Rect(536, 304, 200, 72)
#     #pygame.draw.rect(screen, (0, 0, 0), rectvideo, 1)
#     video = fontInline.render("Video", True, (255, 255, 255))
#     screen.blit(video, (x, y))
#     if rect.collidepoint((mouse_position)):
#         if click == True:
#             number.current_screen = 4

def Sound(x, y,mouse_position,click):
    rect = pygame.Rect(536, 376, 200, 72)
    #pygame.draw.rect(screen,(0,0,0),rectsound,1)
    sound = fontInline.render("Sound", True, (255, 255, 255))
    screen.blit(sound, (x, y))
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen = 5

def Arrow(x, y,mouse_position,click):
    screen.blit(reArrow, (x, y))
    rect=pygame.Rect(30, 30, 104, 104)
    #pygame.draw.rect(screen,(0,0,0),rectarrow,1)
    if rect.collidepoint((mouse_position)):
        if click==True and number.game_in_session==True:
            number.current_screen = 12
        elif click==True:
            number.current_screen = 0

def optionx():
    click = False
    mouse_position = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            video.Res1920x1080(474,584, mouse_position, click)
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            number.Sound.click_channel.play(number.Sound.click_sound)
            click=True

    Option(496,80,mouse_position,click)
    #Video(555,312,mouse_position,click)
    Sound(552,384,mouse_position,click)
    Arrow(0,0,mouse_position,click)
    pygame.display.update()
    fpsClock.tick(FPS)
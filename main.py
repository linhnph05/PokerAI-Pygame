import pygame,number
from pygame.locals import *
from pygame import mixer

# Color
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

WINDOWWIDTH = 1280 # Chiều dài cửa sổ
WINDOWHEIGHT = 720 # Chiều cao cửa sổ

pygame.init()
mixer.init()

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


import sys, mainmenu , difficulty, option,  video, BlindBet,guide,TableAI,os,numberofplayer
import sound,money,timey

number.Sound.main_sound.set_volume(number.Sound.sound_music/float(100))
number.Sound.main_channel.play(number.Sound.main_sound)
number.Sound.main_sound.play(loops=-1)

t=0
# Chay chuong trinh
while True:
    if number.current_screen == 0: mainmenu.mainmenux()
    if number.current_screen == 1:
        guide.guidex()
        number.current_screen = 0
    if number.current_screen == 2: option.optionx()
    # if number.current_screen == 4: video.videox()
    if number.current_screen == 5: sound.soundx()

    if number.current_screen == 7: difficulty.difficultyx()
    if number.current_screen == 8: timey.timex()
    if number.current_screen == 9: money.moneyx()

    if number.current_screen == 10: BlindBet.BlindBetx()
    if number.current_screen == 11: numberofplayer.numberofplayerx()
    if number.current_screen == 12:
        if (t==0): TableAI.Define()
        t+=1
        TableAI.TableAIx()

# click=True
# mouse_position = pygame.mouse.get_pos()
# video.Res1920x1080(mouse_position, click)
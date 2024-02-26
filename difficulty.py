import pygame, sys,number,video
from pygame.locals import *

pygame.init()

#Screen and background
screen = pygame.display.set_mode((1280, 720))  # Ratio 16:9
background = pygame.image.load("Resource/poker_green_background.jpg")

#Caption
pygame.display.set_caption('Poker')

#Icon
icon = pygame.image.load("Resource/poker_cards_icon.png")
pygame.display.set_icon(icon)

#Return Arrow
reArrow = pygame.image.load('Resource/return_arrow.png')
reArrow = pygame.transform.scale(reArrow, (160, 160))
background = pygame.transform.scale(background, (1280, 720))

#Font and size
fontHeading = pygame.font.Font('Resource/Calibri Bold.TTF', 96)
fontInline = pygame.font.Font('Resource/Calibri Bold.TTF', 64)

#Text func
def Difficulty(x, y,mouse_position,click):
    difficulty = fontHeading.render("Difficulty", True, (255,255,255))
    screen.blit(difficulty, (x,y))

def Easy(x, y,mouse_position,click):
    easy = fontInline.render("Easy", True, (255, 255, 255))
    screen.blit(easy, (x, y))
    rect = pygame.Rect(560, 272, 152, 80)

    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_level="Easy"
            number.multiplier=1.25
            number.current_screen = 8

def Normal(x, y,mouse_position,click):
    normal = fontInline.render("Normal", True, (255, 255, 255))
    screen.blit(normal, (x, y))
    rect = pygame.Rect(528, 392, 232, 80)

    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_level="Normal"
            number.multiplier=1.5
            number.current_screen = 8

def Hard(x, y,mouse_position,click):
    hard = fontInline.render("Hard", True, (255, 255, 255))
    screen.blit(hard, (x, y))
    rect = pygame.Rect(560, 512, 160, 80)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_level="Hard"
            number.multiplier=2
            number.current_screen = 8

#Return arrow func
def Arrow(x, y,mouse_position,click):
    screen.blit(reArrow, (x, y))
    rect = pygame.Rect(30,30,104,104)
    if rect.collidepoint((mouse_position)):
        if click == True:
            '''pygame.quit()
            os.system('option.py')'''
            number.current_screen = 0



def difficultyx():
    click = False
    mouse_position = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            video.Res1920x1080(474, 584, mouse_position, click)
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            #click_sound = pygame.mixer.Sound("click.mp3")
            #pygame.mixer.Sound.play(click_sound)
            number.Sound.click_channel.play(number.Sound.click_sound)
            click = True

    Difficulty(456, 80, mouse_position, click)
    Easy(576, 280, mouse_position, click)
    Normal(544, 400, mouse_position, click)
    Hard(576, 520, mouse_position, click)
    Arrow(0, 0, mouse_position, click)
    pygame.display.update()
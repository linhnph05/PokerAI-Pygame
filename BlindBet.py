import pygame, sys,number,video
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Poker')
background = pygame.image.load("Resource/poker_green_background.jpg")
background = pygame.transform.scale(background, (1280, 720))

reArrow = pygame.image.load("Resource/return_arrow.png")
reArrow = pygame.transform.scale(reArrow, (160, 160))
forArrow = pygame.transform.flip(reArrow, True, False)

chip50 = pygame.image.load("Resource/Chip 50.png")
chip50 = pygame.transform.scale(chip50, (192, 192))
chip500 = pygame.image.load("Resource/Chip 500.png")
chip500 = pygame.transform.scale(chip500, (192, 192))
chip1000 = pygame.image.load("Resource/Chip 1000.png")
chip1000 = pygame.transform.scale(chip1000, (192, 192))

FPS = 60
fpsClock = pygame.time.Clock()

fontHeading = pygame.font.Font('Resource/Calibri Bold.TTF', 96)
fontInline = pygame.font.Font('Resource/Calibri Bold.TTF', 64)
fontSmall = pygame.font.Font('Resource/Calibri Bold.TTF', 32)


def Table(x, y):
    table = fontHeading.render("Table", True, (255, 255, 255))
    screen.blit(table, (x, y))


def Return(x, y,mouse_position,click):
    screen.blit(reArrow, (x, y))
    rect = pygame.Rect(64, 64, 104, 104)
    # pygame.draw.rect(screen,(0,0,0),rectarrow,1)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen = 9

def Blind_50(x, y, mouse_position, click):
    blind_50 = fontSmall.render("Blinds 50$/100$", True, (255, 255, 255))
    screen.blit(blind_50, (x, y))
    rect = pygame.Rect(200, 250, 260, 260)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen = 11
            number.blindMoney = 50


def Blind_500(x, y, mouse_position, click):
    blind_500 = fontSmall.render("Blinds 500$/1000$", True, (255, 255, 255))
    screen.blit(blind_500, (x, y))
    rect = pygame.Rect(520, 250, 270, 260)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen = 11
            number.blindMoney = 500


def Blind_1000(x, y, mouse_position, click):
    blind_1000 = fontSmall.render("Blinds 1000$/2000$", True, (255, 255, 255))
    screen.blit(blind_1000, (x, y))
    rect = pygame.Rect(850, 250, 270, 260)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen = 11
            number.blindMoney = 1000



def BlindBetx():
    click = False
    mouse_position = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))
    screen.blit(chip50, (240, 240))
    screen.blit(chip500, (560, 240))
    screen.blit(chip1000, (880, 240))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            video.Res1920x1080(474,584, mouse_position, click)
            pygame.quit()
            sys.exit()
        if e.type == MOUSEBUTTONDOWN:
            click_sound = pygame.mixer.Sound("Resource/click.mp3")
            pygame.mixer.Sound.play(click_sound)
            click = True

    Return(32, 32, mouse_position, click)
    #Forward(1088, 32,mouse_position,click)
    Table(528, 80)
    Blind_50(224, 464, mouse_position, click)
    Blind_500(539, 464, mouse_position, click)
    Blind_1000(858, 464, mouse_position, click)
    fpsClock.tick(FPS)
    pygame.display.update()
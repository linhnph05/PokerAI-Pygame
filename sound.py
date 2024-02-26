import pygame, sys,video,number
import os,tkinter
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

# Return_arrow
reArrow = pygame.image.load('Resource/return_arrow.png')
reArrow = pygame.transform.scale(reArrow, (160, 160))
background = pygame.transform.scale(background, (1280, 720))

# Icon
icon = pygame.image.load("Resource/poker_cards_icon.png")
pygame.display.set_icon(icon)

# Font
fontHeading = pygame.font.Font('Resource/Calibri Bold.TTF', 96)
fontInline = pygame.font.Font('Resource/Calibri Bold.TTF', 64)



def Sound(x, y):
    sound = fontHeading.render("Sound", True, (255,255,255))
    screen.blit(sound, (x,y))

def MasterVolume(x, y):
    mastervolume = fontInline.render("Master Volume", True, (255,255,255))
    screen.blit(mastervolume, (x,y))

def MusicVolume(x, y):
    musicvolume = fontInline.render("Music Volume", True, (255,255,255))
    screen.blit(musicvolume, (x,y))

def EffectsVolume(x, y):
    effectsvolume = fontInline.render("Effects Volume", True, (255,255,255))
    screen.blit(effectsvolume, (x,y))

def VoiceVolume(x, y):
    voicevolume = fontInline.render("Voice Volume", True, (255,255,255))
    screen.blit(voicevolume, (x,y))

def Arrow(x, y,mouse_position,click):
    screen.blit(reArrow, (x, y))
    rect=pygame.Rect(30,30,104,104)
    #pygame.draw.rect(screen,(0,0,0),rectarrow,1)
    if rect.collidepoint((mouse_position)):
        if click==True:
            if click == True:
                number.current_screen = 2

def Line(x, y, z, t):
    pygame.draw.line(x, y, z, t)

def Sound_set(x, y, text):
    Time_set = fontInline.render(text, True, (255, 255, 255))
    screen.blit(Time_set, (x, y))

class variable():
    sound_master_text = str(number.Sound.sound_master)
    x_master=640+number.Sound.sound_master*4
    sound_music_text = str(number.Sound.sound_music)
    x_music=640+number.Sound.sound_music*4
    sound_effects_text= str(number.Sound.sound_effects)
    x_effects=640+number.Sound.sound_effects*4
    sound_voice_text = str(number.Sound.sound_voice)
    x_voice=640+number.Sound.sound_voice*4
    rect_dragging=False

def soundx():
    click = False
    check=False
    mouse_position = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))
    '''variable.sound_master_text = str(number.Sound.sound_master).zfill(3)
    variable.sound_music_text = str(number.Sound.sound_music).zfill(3)
    variable.sound_effects_text = str(number.Sound.sound_effects).zfill(3)
    variable.sound_voice_text = str(number.Sound.sound_voice).zfill(3)'''

    Line(screen, (255, 255, 255), (640, 272), (1040, 272))
    Line(screen, (255, 255, 255), (640, 240), (640, 304))
    Line(screen, (255, 255, 255), (1040, 240), (1040, 304))

    Line(screen, (255, 255, 255), (640, 360), (1040, 360))
    Line(screen, (255, 255, 255), (640, 328), (640, 392))
    Line(screen, (255, 255, 255), (1040, 328), (1040, 392))

    Line(screen, (255, 255, 255), (640, 448), (1040, 448))
    Line(screen, (255, 255, 255), (640, 416), (640, 480))
    Line(screen, (255, 255, 255), (1040, 416), (1040, 480))

    Line(screen, (255, 255, 255), (640, 536), (1040, 536))
    Line(screen, (255, 255, 255), (640, 504), (640, 568))
    Line(screen, (255, 255, 255), (1040, 504), (1040, 568))

    Sound_set(1100, 248, variable.sound_master_text)
    Sound_set(1100, 336, variable.sound_music_text)
    Sound_set(1100, 424, variable.sound_effects_text)
    Sound_set(1100, 512, variable.sound_voice_text)

    #Master
    Line(screen, (255, 255, 255), (640+number.Sound.sound_master*4, 256), (640+number.Sound.sound_master*4, 288))
    rect1 = pygame.Rect(640 + number.Sound.sound_master * 4 - 10, 240, 32, 64)
    if rect1.collidepoint((mouse_position)):
        for e in pygame.event.get():
            check=True
            if e.type == QUIT:
                video.Res1920x1080(474,584, mouse_position, click)
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                click_sound = pygame.mixer.Sound("click.mp3")
                pygame.mixer.Sound.play(click_sound)
                click = True
                if rect1.collidepoint(e.pos):
                    variable.rect_dragging = True
                    mouse_x, mouse_y = e.pos
                    variable.x_master_offset = rect1.x - mouse_x
            elif e.type == pygame.MOUSEBUTTONUP:
                variable.rect_dragging = False
            elif e.type == pygame.MOUSEMOTION:
                if variable.rect_dragging:
                    mouse_x, mouse_y = e.pos
                    if 1040 >= (mouse_x + variable.x_master_offset) >= 640:
                        x_now = variable.x_master
                        rect1.x = mouse_x + variable.x_master_offset
                        variable.x_master = mouse_x + variable.x_master_offset
                        number.Sound.sound_master += (variable.x_master - x_now) / 4
                        variable.sound_master_text = str(round(number.Sound.sound_master))
                    else:
                        continue
    #Music
    Line(screen, (255, 255, 255), (640 + number.Sound.sound_music * 4, 344), (640 + number.Sound.sound_music * 4, 378))
    rect2 = pygame.Rect(640 + number.Sound.sound_music * 4 - 10, 312, 32, 64)
    number.Sound.main_sound.set_volume(number.Sound.sound_music/float(100))
    if rect2.collidepoint((mouse_position)) and check==False:
        for e in pygame.event.get():
            check=True
            if e.type == pygame.MOUSEBUTTONDOWN:
                if rect2.collidepoint(e.pos):
                    variable.rect_dragging = True
                    mouse_x, mouse_y = e.pos
                    variable.x_music_offset = rect2.x - mouse_x
            elif e.type == pygame.MOUSEBUTTONUP:
                variable.rect_dragging = False
            elif e.type == pygame.MOUSEMOTION:
                if variable.rect_dragging:
                    mouse_x, mouse_y = e.pos
                    if 1040 >= (mouse_x + variable.x_music_offset) >= 640:
                        x_now = variable.x_music
                        rect2.x = mouse_x + variable.x_music_offset
                        variable.x_music = mouse_x + variable.x_music_offset
                        number.Sound.sound_music += (variable.x_music - x_now) / 4
                        variable.sound_music_text = str(round(number.Sound.sound_music))
                    else:
                        continue
    #Effect
    Line(screen, (255, 255, 255), (640 + number.Sound.sound_effects * 4, 432), (640 + number.Sound.sound_effects * 4, 464))
    rect3 = pygame.Rect(640 + number.Sound.sound_effects * 4 - 10, 416, 32, 64)
    number.Sound.click_sound.set_volume(number.Sound.sound_effects / float(100))
    if rect3.collidepoint((mouse_position)) and check == False:
        for e in pygame.event.get():
            check = True
            if e.type == pygame.MOUSEBUTTONDOWN:
                if rect3.collidepoint(e.pos):
                    variable.rect_dragging = True
                    mouse_x, mouse_y = e.pos
                    variable.x_effects_offset = rect3.x - mouse_x
            elif e.type == pygame.MOUSEBUTTONUP:
                variable.rect_dragging = False
            elif e.type == pygame.MOUSEMOTION:
                if variable.rect_dragging:
                    mouse_x, mouse_y = e.pos
                    if 1040 >= (mouse_x + variable.x_effects_offset) >= 640:
                        x_now = variable.x_effects
                        rect3.x = mouse_x + variable.x_effects_offset
                        variable.x_effects = mouse_x + variable.x_effects_offset
                        number.Sound.sound_effects += (variable.x_effects - x_now) / 4
                        variable.sound_effects_text = str(round(number.Sound.sound_effects))
                    else:
                        continue
    #Voice
    Line(screen, (255, 255, 255), (640 + number.Sound.sound_voice* 4, 520),(640 + number.Sound.sound_voice * 4, 552))
    rect4 = pygame.Rect(640 + number.Sound.sound_voice * 4 - 10, 504, 32, 64)
    if rect4.collidepoint((mouse_position)) and check == False:
        for e in pygame.event.get():
            check = True
            if e.type == pygame.MOUSEBUTTONDOWN:
                if rect4.collidepoint(e.pos):
                    variable.rect_dragging = True
                    mouse_x, mouse_y = e.pos
                    variable.x_voice_offset = rect4.x - mouse_x
            elif e.type == pygame.MOUSEBUTTONUP:
                variable.rect_dragging = False
            elif e.type == pygame.MOUSEMOTION:
                if variable.rect_dragging:
                    mouse_x, mouse_y = e.pos
                    if 1040 >= (mouse_x + variable.x_voice_offset) >= 640:
                        x_now = variable.x_voice
                        rect4.x = mouse_x + variable.x_voice_offset
                        variable.x_voice = mouse_x + variable.x_voice_offset
                        number.Sound.sound_voice += (variable.x_voice - x_now) / 4
                        variable.sound_voice_text = str(round(number.Sound.sound_voice))
                    else:
                        continue


    if check==False:
        for e in pygame.event.get():
            if e.type == QUIT:
                video.Res1920x1080(474,584, mouse_position, click)
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                #click_sound = pygame.mixer.Sound("click.mp3")
                #pygame.mixer.Sound.play(click_sound)
                number.Sound.click_channel.play(number.Sound.click_sound)
                click = True
            elif e.type == pygame.MOUSEMOTION:
                if variable.rect_dragging:
                    variable.rect_dragging=False

    Sound(496, 80)
    MasterVolume(80,240)
    MusicVolume(80,328)
    EffectsVolume(80,416)
    VoiceVolume(80,504)
    Arrow(0,0,mouse_position,click)
    pygame.display.update()
    fpsClock.tick(FPS)
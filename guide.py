import pygame,number,webbrowser,cv2
from pygame.locals import *
from pygame import mixer
import sys
# Color
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

WINDOWWIDTH = 800 # Chiều dài cửa sổ
WINDOWHEIGHT = 450 # Chiều cao cửa sổ

pygame.init()
mixer.init()

FPS = 60
fpsClock = pygame.time.Clock()

# Screen, Caption, Background
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Poker')
background = pygame.image.load("Resource/poker_green_background.jpg")
background = pygame.transform.scale(background, (800, 450))

# Icon
icon = pygame.image.load("Resource/poker_cards_icon.png")
pygame.display.set_icon(icon)

# Font
fontHeading = pygame.font.Font('Resource/Calibri Bold.TTF', 60)
fontInline = pygame.font.Font('Resource/Calibri Bold.TTF', 40)

def guidex():
    click = False
    mouse_position = pygame.mouse.get_pos()
    '''click = False
    mouse_position = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))'''
    # Bat sound
    mixer.init()
    guide_sound = mixer.Sound('Resource/Cách chơi Poker Texas Hold-em đơn giản dễ hiểu.mp3')
    guide_channel= mixer.find_channel()
    guide_channel.play(guide_sound)
    number.Sound.main_sound.set_volume(0)

    # Bat video
    cap = cv2.VideoCapture('Resource/Cách chơi Poker Texas Hold-em đơn giản dễ hiểu.mp4')
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            b = cv2.resize(frame, (1280, 720), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Poker', b)
            # & 0xFF is required for a 64-bit system
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #video.Res1920x1080(474, 584, mouse_position, click)
                    #number.CScreen.current_screen == 0
                    guide_channel.pause()
                    pygame.quit()
                    sys.exit()
            if cv2.getWindowProperty('Poker', cv2.WND_PROP_VISIBLE) < 1:
                break
        else:
            break

    number.Sound.main_sound.set_volume(number.Sound.sound_music/float(100))
    #number.Sound.main_channel.unpause()
    guide_channel.pause()
    cap.release()
    cv2.destroyAllWindows()

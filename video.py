# import pygame, sys,number
# from pygame.locals import *
#
#
# # Color
# WHITE = (255, 255, 255)
# RED   = (255,   0,   0)
# GREEN = (  0, 255,   0)
#
# WINDOWWIDTH = 1280 # Chiều dài cửa sổ
# WINDOWHEIGHT = 720 # Chiều cao cửa sổ
#
# pygame.init()
#
# FPS = 60
# fpsClock = pygame.time.Clock()
#
# # Screen, Caption, Background
# screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
# pygame.display.set_caption('Poker')
# background = pygame.image.load("Resource/poker_green_background.jpg")
# background = pygame.transform.scale(background, (1280, 720))
#
# # Return_arrow
# reArrow = pygame.image.load('Resource/return_arrow.png')
# reArrow = pygame.transform.scale(reArrow, (160, 160))
# background = pygame.transform.scale(background, (1280, 720))
#
# # Icon
# icon = pygame.image.load("Resource/poker_cards_icon.png")
# pygame.display.set_icon(icon)
#
# # Font
# fontHeading = pygame.font.Font('Resource/Calibri Bold.TTF', 96)
# fontInline = pygame.font.Font('Resource/Calibri Bold.TTF', 64)
#
# def change_screen_size(width, height):
#     # Set the size of the window
#     screen = pygame.display.set_mode((width, height))
#
#     # Fill the screen with white color
#     screen.fill((255, 255, 255))
#
#     # Update the display
#     pygame.display.flip()
#
# def Video(x, y):
#     video = fontHeading.render("Video", True, (255,255,255))
#     screen.blit(video, (x,y))
#
# def Res640x360(x, y,mouse_position,click):
#     res640x360 = fontInline.render("640 x 360", True, (255,255,255))
#     screen.blit(res640x360, (x,y))
#     rect = pygame.Rect(480, 216, 288, 72)
#     #pygame.draw.rect(screen,(0,0,0),rect,1)
#     if rect.collidepoint((mouse_position)):
#         if click == True:
#             change_screen_size(1920, 1080)
#             # devmode = pywintypes.DEVMODEType()
#             # devmode.PelsWidth = 640
#             # devmode.PelsHeight = 360
#             # devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
#             # win32api.ChangeDisplaySettings(devmode, 0)
#
# def Res800x450(x, y,mouse_position,click):
#     res800x450 = fontInline.render("800 x 450", True, (255,255,255))
#     screen.blit(res800x450, (x,y))
#     rect = pygame.Rect(480, 288, 288, 72)
#     #pygame.draw.rect(screen, (0, 0, 0), rect, 1)
#     # if rect.collidepoint((mouse_position)):
#     #     if click == True:
#     #         devmode = pywintypes.DEVMODEType()
#     #         devmode.PelsWidth = 800
#     #         devmode.PelsHeight = 450
#     #         devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
#     #         win32api.ChangeDisplaySettings(devmode, 0)
#
# def Res1024x576(x, y,mouse_position,click):
#     res1024x576 = fontInline.render("1024 x 576", True, (255,255,255))
#     screen.blit(res1024x576, (x,y))
#     rect = pygame.Rect(464, 360, 320, 72)
#     #pygame.draw.rect(screen, (0, 0, 0), rect, 1)
#     # if rect.collidepoint((mouse_position)):
#     #     if click == True:
#     #         devmode = pywintypes.DEVMODEType()
#     #         devmode.PelsWidth = 1024
#     #         devmode.PelsHeight = 576
#     #         devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
#     #         win32api.ChangeDisplaySettings(devmode, 0)
#
# def Res1280x720(x, y,mouse_position,click):
#     res1280x720 = fontInline.render("1280 x 720", True, (255,255,255))
#     screen.blit(res1280x720, (x,y))
#     rect = pygame.Rect(464, 432, 320, 72)
#     #pygame.draw.rect(screen, (0, 0, 0), rect, 1)
#     # if rect.collidepoint((mouse_position)):
#     #     if click == True:
#     #         #permachange=open('reso.py',"w")
#     #         #permachange.write("1280 720")
#     #         #number.ChangeRes()
#     #         devmode = pywintypes.DEVMODEType()
#     #         devmode.PelsWidth = 1280
#     #         devmode.PelsHeight = 720
#     #         devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
#     #         win32api.ChangeDisplaySettings(devmode, 0)
#
# def Res1600x900(x, y,mouse_position,click):
#     res1600x900 = fontInline.render("1600 x 900", True, (255,255,255))
#     screen.blit(res1600x900, (x,y))
#     rect = pygame.Rect(464, 504, 320, 72)
#     #pygame.draw.rect(screen, (0, 0, 0), rect, 1)
#     # if rect.collidepoint((mouse_position)):
#     #     if click == True:
#     #         devmode = pywintypes.DEVMODEType()
#     #         devmode.PelsWidth = 1600
#     #         devmode.PelsHeight = 900
#     #         devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
#     #         win32api.ChangeDisplaySettings(devmode, 0)
#
#
#
# def Res1920x1080(x, y,mouse_position,click):
#     res1920x1080 = fontInline.render("1920 x 1080", True, (255,255,255))
#     screen.blit(res1920x1080, (x,y))
#     rect = pygame.Rect(456, 576, 344, 72)
#     #pygame.draw.rect(screen, (0, 0, 0), rect, 1)
#     # if rect.collidepoint((mouse_position)):
#     #     if click == True:
#     #         devmode = pywintypes.DEVMODEType()
#     #         devmode.PelsWidth = 1920
#     #         devmode.PelsHeight = 1080
#     #         devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
#     #         win32api.ChangeDisplaySettings(devmode, 0)
#
# def Fullscreen(x, y,mouse_position,click):
#     fullscreen = fontInline.render("Fullscreen", True, (255,255,255))
#     screen.blit(fullscreen, (x,y))
#     rect = pygame.Rect(472, 648, 312, 72)
#     #screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),pygame.fullscreen)
#     #if rect.collidepoint((mouse_position)):
#         #if click == True:
#     #pygame.draw.rect(screen, (0, 0, 0), rect, 1)
#
#
# def Arrow(x, y,mouse_position,click):
#     screen.blit(reArrow, (x, y))
#     rect=pygame.Rect(30, 30, 104, 104)
#     #pygame.draw.rect(screen,(0,0,0),rect,1)
#     if rect.collidepoint((mouse_position)):
#         if click==True:
#             number.current_screen = 2
#
#
# def videox():
#     click = False
#     mouse_position = pygame.mouse.get_pos()
#     screen.blit(background, (0, 0))
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             Res1920x1080(474,584, mouse_position, click)
#             pygame.quit()
#             sys.exit()
#         if event.type == MOUSEBUTTONDOWN:
#             #click_sound = pygame.mixer.Sound("click.mp3")
#             #pygame.mixer.Sound.play(click_sound)
#             number.Sound.click_channel.play(number.Sound.click_sound)
#             click = True
#
#     Video(512,80)
#     Res640x360(496, 224, mouse_position, click)
#     Res800x450(496, 296, mouse_position, click)
#     Res1024x576(480, 368, mouse_position, click)
#     Res1280x720(480, 440, mouse_position, click)
#     Res1600x900(480, 512, mouse_position, click)
#     Res1920x1080(472, 584, mouse_position, click)
#     Fullscreen(496, 656, mouse_position, click)
#     Arrow(0,0, mouse_position, click)
#     pygame.display.update()
#     fpsClock.tick(FPS)
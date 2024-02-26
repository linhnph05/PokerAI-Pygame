import pygame, sys
from pygame import mixer

pygame.init()
mixer.init()

current_screen = 0
# 0 main
# 1 guide
# 2 option
# 3 keyboardmouse
# 4 video
# 5 sound
# 6 music
# 7 difficulty
# 8 time
# 9 money
# 10 blindbet
# 11 numberofplayer
# 12 tableai
# 13 tablemulti


class Res():
    resx,resy=1280,720
    multi=resx/800

current_level = "Easy"
multiplier = 1
starting_money = 2000
time_set = 20
blindMoney = 50
player_count = 2

class Sound():
    main_sound=mixer.Sound("Resource/Los Santos.mp3")
    main_channel = mixer.find_channel()
    click_sound = mixer.Sound("Resource/click.mp3")
    click_channel = mixer.find_channel()
    sound_master = 100
    sound_music = 10
    sound_effects = 100
    sound_voice = 100


game_in_session=False

class Screen():
    pass

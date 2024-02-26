import pygame,number,video
import sys

pygame.init()

#screen = pygame.display.set_mode((800,450),pygame.RESIZABLE)
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Poker')
background = pygame.image.load("Resource/poker_green_background.jpg")
background = pygame.transform.scale(background, (1280, 720))
reArrow = pygame.image.load("Resource/return_arrow.png")
reArrow = pygame.transform.scale(reArrow, (160, 160))
forArrow = pygame.transform.flip(reArrow, True, False)

clock = pygame.time.Clock()

fontHeading = pygame.font.Font('Resource/Calibri Bold.TTF', 96)
fontInline = pygame.font.Font('Resource/Calibri Bold.TTF', 64)
fontTime = pygame.font.Font('Resource/Calibri Bold.TTF', 32)


def Player(x, y):
    Player = fontHeading.render("Number of Players", True, (255, 255, 255))
    screen.blit(Player, (x, y))

'''
def Continue(x, y,mouse_position,click):
    Continue = fontInline.render("Continue", True, (255, 255, 255))
    screen.blit(Continue, (x, y))
    rect = pygame.Rect(512, 552, 256, 80)
    #pygame.draw.rect(screen, (0, 0, 0), rect, 1)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.CScreen.current_screen = 12
'''

def Arrow(x, y, mouse_position, click):
    screen.blit(reArrow, (x, y))
    rect = pygame.Rect(30, 30, 104, 104)

    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen=10


def Forward(x, y, mouse_position, click):
    screen.blit(forArrow, (x, y))
    rect = pygame.Rect(1145, 30, 104, 104)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen = 12

def Player_set(x, y,text):
    Player_set = fontInline.render(text + ' Player', True, (255, 255, 255))
    screen.blit(Player_set, (x, y))


def Line(x, y, z, t):
    pygame.draw.line(x, y, z, t)


def Player_min(x, y):
    Player_min = fontTime.render("2", True, (255, 255, 255))
    screen.blit(Player_min, (x, y))


def Player_max(x, y):
    Player_max = fontTime.render("6", True, (255, 255, 255))
    screen.blit(Player_max, (x, y))



x_change = 340
player_set = 2
text = str(player_set)
rect_dragging = False
def numberofplayerx():
    click = False
    global x_change,player_set,text,rect_dragging,offset_x
    mouse_position = pygame.mouse.get_pos()
    rect = pygame.rect.Rect(x_change, 296, 80, 46)
    screen.blit(background, (0, 0))
    Line(screen, (255, 255, 255), (340, 320), (940, 320))
    Line(screen, (255, 255, 255), (340, 288), (340, 352))
    Line(screen, (255, 255, 255), (940, 288), (940, 352))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect(x_change-2, 296, 4, 46))
    Player_min(330, 256)
    Player_max(930, 256)
    Player(275, 80)
    # Time_selection(150, 250) (Optional)
    Player_set(520, 400, text)  # (400, 250) if Time_selection is on
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            video.Res1920x1080(474, 584, mouse_position, click)
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN:
            x_beginning=x_change
            if e.key == pygame.K_LEFT and x_change != 340:
                x_change -= 150
                player_set -= 1
                text = str(round(player_set))
            elif e.key == pygame.K_LEFT and x_change == 340:
                continue
            if e.key == pygame.K_RIGHT and x_change != 940:
                x_change += 150
                player_set += 1
                text = str(round(player_set))
            elif e.key == pygame.K_RIGHT and x_change == 940:
                continue

        if e.type == pygame.MOUSEBUTTONDOWN:
            #click_sound = pygame.mixer.Sound("click.mp3")
            #pygame.mixer.Sound.play(click_sound)
            number.Sound.click_channel.play(number.Sound.click_sound)
            click = True
            if e.button == 1:
                if rect.collidepoint(e.pos):
                    rect_dragging = True
                    mouse_x, mouse_y = e.pos
                    offset_x = rect.x - mouse_x
        elif e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                rect_dragging = False
        elif e.type == pygame.MOUSEMOTION:
            if rect_dragging:
                mouse_x, mouse_y = e.pos
                if 940 >= (mouse_x + offset_x) >= 340:
                    x_now = x_change
                    rect.x = mouse_x + offset_x
                    x_change = mouse_x + offset_x
                    player_set = (x_now-340)/150+2
                    text = str(round(player_set))
                else:
                    continue
    number.player_count = round(player_set)
    #Continue(510, 560, mouse_position, click)
    Arrow(0,0, mouse_position, click)
    Forward(1120, 0, mouse_position, click)
    pygame.display.update()
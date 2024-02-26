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


def Time(x, y):
    Time = fontHeading.render("Time between moves", True, (255, 255, 255))
    screen.blit(Time, (x, y))

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
    rect = pygame.Rect(30,30,104,104)

    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen=7


def Forward(x, y, mouse_position, click):
    screen.blit(forArrow, (x, y))
    rect = pygame.Rect(1145, 30, 104, 104)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen = 9


# def Time_selection(x, y):
#    Time_selection = fontInline.render("Time/move: ", True, (255, 255, 255))
#    screen.blit(Time_selection, (x, y))
# Optional (only if teacher needs it)

def Time_set(x, y,text):
    Time_set = fontInline.render(text, True, (255, 255, 255))
    screen.blit(Time_set, (x, y))


def Line(x, y, z, t):
    pygame.draw.line(x, y, z, t)


def Time_min(x, y):
    Time_min = fontTime.render("20s", True, (255, 255, 255))
    screen.blit(Time_min, (x, y))


def Time_max(x, y):
    Time_max = fontTime.render("300s", True, (255, 255, 255))
    screen.blit(Time_max, (x, y))



x_change = 360
time_set = 20
text = str(time_set) + "s"
rect_dragging = False
def timex():
    global x_change,time_set,text,rect_dragging,offset_x
    click = False
    mouse_position = pygame.mouse.get_pos()
    rect = pygame.rect.Rect(x_change, 296, 80, 46)
    screen.blit(background, (0, 0))
    Line(screen, (255, 255, 255), (360, 320), (920, 320))
    Line(screen, (255, 255, 255), (360, 288), (360, 352))
    Line(screen, (255, 255, 255), (920, 288), (920, 352))
    pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect(x_change-2, 296, 4, 46))
    Time_min(340, 256)
    Time_max(900, 256)
    Time(224, 80)
    # Time_selection(150, 250) (Optional)
    Time_set(570, 400, text)  # (400, 250) if Time_selection is on
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            video.Res1920x1080(474, 584, mouse_position, click)
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT and x_change != 360:
                x_change -= 1
                time_set -= 1
                text = str(time_set).zfill(3) + "s"
            elif e.key == pygame.K_LEFT and x_change == 360:
                continue
            if e.key == pygame.K_RIGHT and x_change != 920:
                x_change += 1
                time_set += 1
                text = str(time_set).zfill(3) + "s"
            elif e.key == pygame.K_RIGHT and x_change == 920:
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
                if 920 >= (mouse_x + offset_x) >= 360:
                    x_now = x_change
                    rect.x = mouse_x + offset_x
                    x_change = mouse_x + offset_x
                    time_set += (x_change - x_now)/2 #???
                    text = str(round(time_set)) + "s"
                else:
                    continue
    number.time_set = round(time_set)
    #Continue(510, 560, mouse_position, click)
    Arrow(0,0, mouse_position, click)
    Forward(1120, 0, mouse_position, click)
    pygame.display.update()
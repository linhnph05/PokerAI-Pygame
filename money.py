import pygame,number, sys

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Poker')
background = pygame.image.load("Resource/poker_green_background.jpg")
background = pygame.transform.scale(background, (1280, 720))

reArrow = pygame.image.load("Resource/return_arrow.png")
reArrow = pygame.transform.scale(reArrow, (160, 160))
forArrow = pygame.transform.flip(reArrow, True, False)

chip50 = pygame.image.load("Resource/Chip 50.png")
chip50 = pygame.transform.scale(chip50, (200, 200))
chip500 = pygame.image.load("Resource/Chip 500.png")
chip500 = pygame.transform.scale(chip500, (200, 200))
chip500 = pygame.transform.rotate(chip500, -4.285)
chip1000 = pygame.image.load("Resource/Chip 1000.png")
chip1000 = pygame.transform.scale(chip1000, (200, 200))
chip5000 = pygame.image.load("Resource/Chip 5000.png")
chip5000 = pygame.transform.scale(chip5000, (200, 200))

FPS = 60
fpsClock = pygame.time.Clock()

fontHeading = pygame.font.Font('Resource/Calibri Bold.TTF', 96)
fontInline = pygame.font.Font('Resource/Calibri Bold.TTF', 64)
fontSmall = pygame.font.Font('Resource/Calibri Bold.TTF', 32)


def Money(x, y):
    money = fontHeading.render("Starting money", True, (255, 255, 255))
    screen.blit(money, (x, y))


def Chip_50(x, y):
    screen.blit(chip50, (x, y))


def Chip_500(x, y):
    screen.blit(chip500, (x, y))


def Chip_1000(x, y):
    screen.blit(chip1000, (x, y))


def Chip_5000(x, y):
    screen.blit(chip5000, (x, y))


def Return(x, y,mouse_position,click):
    screen.blit(reArrow, (x, y))
    rect = pygame.Rect(30,30,104,104)
    # pygame.draw.rect(screen,(0,0,0),rectarrow,1)
    if rect.collidepoint((mouse_position)):
       if click == True:
            number.current_screen = 8


def Forward(x, y,mouse_position,click):
    screen.blit(forArrow, (x, y))
    rect = pygame.Rect(1145, 30, 104, 104)
    # pygame.draw.rect(screen,(0,0,0),rect,1)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen = 10


def Line(x, y, z, t):
    pygame.draw.line(x, y, z, t)


def Chip50_set(x, y):
    Chip50_set = fontSmall.render(text_50, True, (255, 255, 255))
    screen.blit(Chip50_set, (x, y))


def Chip500_set(x, y):
    Chip500_set = fontSmall.render(text_500, True, (255, 255, 255))
    screen.blit(Chip500_set, (x, y))


def Chip1000_set(x, y):
    Chip1000_set = fontSmall.render(text_1000, True, (255, 255, 255))
    screen.blit(Chip1000_set, (x, y))


def Chip5000_set(x, y):
    Chip5000_set = fontSmall.render(text_5000, True, (255, 255, 255))
    screen.blit(Chip5000_set, (x, y))


def Total(x, y):
    Total = fontInline.render("Total:", True, (255, 255, 255))
    screen.blit(Total, (x, y))


def Sum(x, y):
    Sum = fontInline.render(text_sum, True, (255, 255, 255))
    screen.blit(Sum, (x, y))


def Warning(x, y):
    Warning = fontSmall.render("*The maximum is 100,000$*", True, (255, 255, 255))
    screen.blit(Warning, (x, y))


chip50_set = 0
text_50 = str(chip50_set)
chip500_set = 0
text_500 = str(chip500_set)
chip1000_set = 0
text_1000 = str(chip1000_set)
chip5000_set = 0
text_5000 = str(chip5000_set)
sum=2000
text_sum = str(sum) + "$"

#while True:
def moneyx():
    global chip50_set ,text_50 ,chip500_set,text_500 ,chip1000_set ,text_1000 ,chip5000_set ,text_5000 ,sum ,text_sum

    click = False
    mouse_position = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))

    Money(320, 80)
    Total(400, 560)
    Sum(640, 560)
    Warning(400, 640)

    Chip_50(120, 240)
    rect_50p = pygame.rect.Rect(320, 440, 34, 34)
    pygame.draw.rect(screen, (0, 0, 0), rect_50p)
    rect_50m = pygame.rect.Rect(120, 440, 34, 34)
    pygame.draw.rect(screen, (0, 0, 0), rect_50m)
    Line(screen, (255, 255, 255), (320, 456), (352, 456))
    Line(screen, (255, 255, 255), (336, 440), (336, 472))
    Line(screen, (255, 255, 255), (120, 456), (152, 456))
    Chip50_set(211, 440)

    Chip_500(400, 230)
    rect_500p = pygame.rect.Rect(600, 440, 34, 34)
    pygame.draw.rect(screen, (0, 0, 0), rect_500p)
    rect_500m = pygame.rect.Rect(400, 440, 34, 34)
    pygame.draw.rect(screen, (0, 0, 0), rect_500m)
    Line(screen, (255, 255, 255), (600, 456), (632, 456))
    Line(screen, (255, 255, 255), (616, 440), (616, 472))
    Line(screen, (255, 255, 255), (400, 456), (432, 456))
    Chip500_set(491, 440)

    Chip_1000(680, 232)
    rect_1000p = pygame.rect.Rect(880, 440, 34, 34)
    pygame.draw.rect(screen, (0, 0, 0), rect_1000p)
    rect_1000m = pygame.rect.Rect(680, 440, 34, 34)
    pygame.draw.rect(screen, (0, 0, 0), rect_1000m)
    Line(screen, (255, 255, 255), (880, 456), (912, 456))
    Line(screen, (255, 255, 255), (896, 440), (896, 472))
    Line(screen, (255, 255, 255), (680, 456), (712, 456))
    Chip1000_set(771, 440)

    Chip_5000(960, 232)
    rect_5000p = pygame.rect.Rect(1160, 440, 34, 34)
    pygame.draw.rect(screen, (0, 0, 0), rect_5000p)
    rect_5000m = pygame.rect.Rect(960, 440, 34, 34)
    pygame.draw.rect(screen, (0, 0, 0), rect_5000m)
    Line(screen, (255, 255, 255), (1160, 456), (1192, 456))
    Line(screen, (255, 255, 255), (1176, 440), (1176, 472))
    Line(screen, (255, 255, 255), (960, 456), (992, 456))
    Chip5000_set(1051, 440)


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            number.Sound.click_channel.play(number.Sound.click_sound)
            click=True
            if e.button == 1:
                # Chip 50
                if rect_50p.collidepoint(e.pos) and sum <= 99950:
                    chip50_set += 1
                    sum += 50
                if rect_50m.collidepoint(e.pos) and chip50_set > 0:
                    chip50_set -= 1
                    sum -= 50
                text_50 = str(chip50_set)
                Chip50_set(211, 440)

                # Chip 500
                if rect_500p.collidepoint(e.pos) and sum <= 99500:
                    chip500_set += 1
                    sum += 500
                if rect_500m.collidepoint(e.pos) and chip500_set > 0:
                    chip500_set -= 1
                    sum -= 500
                text_500 = str(chip500_set)
                Chip500_set(491, 440)

                # Chip 1000
                if rect_1000p.collidepoint(e.pos) and sum <= 99000:
                    chip1000_set += 1
                    sum += 1000
                if rect_1000m.collidepoint(e.pos) and chip1000_set > 0:
                    chip1000_set -= 1
                    sum -= 1000
                text_1000 = str(chip1000_set)
                Chip1000_set(771, 440)

                # Chip 5000
                if rect_5000p.collidepoint(e.pos) and sum <= 95000:
                    chip5000_set += 1
                    sum += 5000
                if rect_5000m.collidepoint(e.pos) and chip5000_set > 0:
                    chip5000_set -= 1
                    sum -= 5000
                text_5000 = str(chip5000_set)
                Chip5000_set(1051, 440)
            if sum < 1000:
                text_sum = str(sum) + "$"
            else:
                num2 = sum
                num1, num2 = divmod(num2, 1000)
                text_sum = str(num1) + "," + str(num2).zfill(3) + "$"
            Sum(640, 560)

    number.starting_money = sum

    Return(0, 0, mouse_position, click)
    Forward(1120, 0, mouse_position, click)
    fpsClock.tick(FPS)
    pygame.display.update()
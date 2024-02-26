import random, pygame, sys

pygame.init()

screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption('Poker')
background = pygame.image.load("Resource/poker_green_background.png")
background = pygame.transform.scale(background, (800, 450))

reArrow = pygame.image.load("Resource/return arrow.png")
reArrow = pygame.transform.scale(reArrow, (100, 100))
setting = pygame.image.load("Resource/Setting.png")
setting = pygame.transform.scale(setting, (50, 50))
emoji = pygame.image.load("Resource/Emoji.png")
emoji = pygame.transform.scale(emoji, (50, 50))
chat = pygame.image.load("Resource/Chat.png")
chat = pygame.transform.scale(chat, (50, 50))
table = pygame.image.load("Resource/Table.png")
table = pygame.transform.scale(table, (370, 170))
woman = pygame.image.load("Resource/The woman.png")
woman = pygame.transform.scale(woman, (100, 100))
cards_symbol = pygame.image.load("Resource/Cards Symbol.png")
cards_symbol = pygame.transform.scale(cards_symbol, (25, 25))
poker_night = pygame.image.load("Resource/Poker night.png")
poker_night = pygame.transform.scale(poker_night, (200, 100))

big_blind = pygame.image.load("Resource/Big blind button.png")
big_blind = pygame.transform.scale(big_blind, (50, 50))
small_blind = pygame.image.load("Resource/Small blind button.png")
small_blind = pygame.transform.scale(small_blind, (50, 50))
dealer = pygame.image.load("Resource/Dealer button.png")
dealer = pygame.transform.scale(dealer, (50, 50))

Ten_of_C = pygame.image.load("Resource/10 of C.png")
Ten_of_C = pygame.transform.scale(Ten_of_C, (70, 90))
Ten_of_C = pygame.transform.rotate(Ten_of_C, 15)
Q_of_D = pygame.image.load("Resource/Q of D.png")
Q_of_D = pygame.transform.scale(Q_of_D, (70, 90))
flip_card_1 = pygame.image.load("Resource/Flip card.png")
flip_card_1 = pygame.transform.scale(flip_card_1, (110, 110))
flip_card_2 = pygame.image.load("Resource/Flip card.png")
flip_card_2 = pygame.transform.scale(flip_card_2, (110, 110))
flip_card_2 = pygame.transform.rotate(flip_card_2, -15)
Adam = pygame.image.load("Resource/Adam.png")
Adam = pygame.transform.scale(Adam, (600, 350))

FPS = 60
fpsClock = pygame.time.Clock()

fontHeading = pygame.font.Font('Resource/Calibri Bold Poker.TTF', 60)
fontInline = pygame.font.Font('Resource/Calibri Bold Poker.TTF', 40)
fontSmall = pygame.font.Font('Resource/Calibri Bold Poker.TTF', 20)
fontTiny = pygame.font.Font('Resource/Calibri Bold Poker.TTF', 15)


def Return(x, y):
    screen.blit(reArrow, (x, y))


def Name(x, y):
    name = fontTiny.render("NAME", True, (0, 0, 0))
    screen.blit(name, (x, y))


def Avatar(x, y):
    avatar = fontTiny.render("AVATAR", True, (0, 0, 0))
    screen.blit(avatar, (x, y))


def Money(x, y):
    money = fontTiny.render(text_starting_money, True, (0, 0, 0))
    screen.blit(money, (x, y))


def Fold(x, y):
    fold = fontSmall.render("Fold", True, (255, 255, 255))
    screen.blit(fold, (x, y))


def Check(x, y):
    check = fontSmall.render("Check", True, (255, 255, 255))
    screen.blit(check, (x, y))


def Call_Bet(x, y):
    call_bet = fontSmall.render("Call/Bet", True, (255, 255, 255))
    screen.blit(call_bet, (x, y))


def Raise(x, y):
    raise_money = fontSmall.render("Raise", True, (255, 255, 255))
    screen.blit(raise_money, (x, y))


def Time_starting(x, y):
    time_starting = fontHeading.render("Starting after:", True, (0, 0, 0))
    screen.blit(time_starting, (x, y))


'''
def Time_num(x, y):
    time_num = fontHeading.render(text_count, True, (0, 0, 0))
    screen.blit(time_num, (x, y))
'''


def My_turn(x, y):
    my_turn = fontSmall.render("My turn:", True, (255, 255, 255))
    screen.blit(my_turn, (x, y))


def Their_turn(x, y):
    their_turn = fontSmall.render("Their turn:", True, (255, 255, 255))
    screen.blit(their_turn, (x, y))


def Time_left(x, y):
    time = fontSmall.render(text_timeleft, True, (255, 255, 255))
    screen.blit(time, (x, y))


def Bet_Raise_Money(x, y, z):
    if len(z) > 0:
        bet_raise_money = fontSmall.render(z + "$", True, (0, 0 ,0))
    else:
        bet_raise_money = fontSmall.render(z, True, (0, 0, 0))
    screen.blit(bet_raise_money, (x, y))


c1 = random.randint(0, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)
c4 = random.randint(0, 255)

time_left = 100000 #30
mini_time_left = 10
time_change = 0
text_timeleft = str(time_left) + "s"
check = True
#time_start = False
#count = 6
#text_count = str(count) + "s"
end_turn = False
check_bet = False
last_bet = 0
starting_money = 100000
text_starting_money = str(starting_money) + "$"
pot_money = 0
turn_bet = ""
turn_raise = ""
click_call = False
check_click_call = True
click_raise = False
check_click_raise = True
click_check = False
click_fold = False
check_click_fold = False
check_click_fold_myturn = False

# Button screens
screen1 = True
screen2 = False
screen3 = False

while True:

    # Details
    screen.blit(background, (0, 0))
    screen.blit(setting, (680, 50))
    screen.blit(emoji, (30, 380))
    screen.blit(chat, (100, 380))
    screen.blit(table, (215, 120))
    screen.blit(woman, (350, 24))
    screen.blit(cards_symbol, (370, 135))
    screen.blit(poker_night, (385, 125))
    screen.blit(big_blind, (280, 230))
    screen.blit(small_blind, (380, 230))
    screen.blit(dealer, (480, 230))
    screen.blit(Ten_of_C, (440, 295))
    screen.blit(Q_of_D, (460, 295))
    screen.blit(flip_card_1, (200, 100))
    screen.blit(flip_card_2, (200, 95))
    screen.blit(Adam, (140, 110))
    Return(20, 20)

    # Name, avatar, money
    pygame.draw.rect(screen, (255, 100, 10), (375, 290, 51, 26))
    rect_name = pygame.rect.Rect(375, 290, 51, 26)
    Name(380, 295)
    pygame.draw.rect(screen, (0, 0, 255), (370, 320, 61, 26))
    rect_ava = pygame.rect.Rect(370, 320, 61, 26)
    Avatar(375, 325)
    pygame.draw.rect(screen, (255, 255, 0), (371, 350, 58, 26))
    rect_mon = pygame.rect.Rect(371, 350, 58, 26)
    Money(376, 355)

    # Buttons
    pygame.draw.rect(screen, (0, 0, 0), (225, 385, 86, 41))
    rect_fold = pygame.rect.Rect(225, 385, 86, 41)
    Fold(250, 395)
    pygame.draw.rect(screen, (0, 0, 0), (351, 385, 101, 41))
    rect_check = pygame.rect.Rect(351, 385, 101, 41)
    Check(376, 395)
    pygame.draw.rect(screen, (0, 0, 0), (492, 385, 118, 41))
    rect_call = pygame.rect.Rect(492, 385, 118, 41)
    Call_Bet(517, 395)
    pygame.draw.rect(screen, (0, 0, 0), (650, 385, 94, 41))
    rect_raise = pygame.rect.Rect(650, 385, 94, 41)
    Raise(675, 395)

    # After click at fold button
    if click_fold:
        flip_card_3 = flip_card_1
        flip_card_4 = flip_card_2
        flip_card_4 = pygame.transform.rotate(flip_card_4, 30)
        screen.blit(flip_card_4, (394, 257))
        screen.blit(flip_card_3, (440, 285))
        check_click_fold_myturn = True

    # After click at check button
    if click_check:
        end_turn = True
        click_check = False

    # After click at call/bet button
    if click_call:
        if check_click_call:
            mini_time_left -= 1
            check_click_call = False
        pygame.draw.rect(screen, (0, 0, 0), (522, 306, 222, 60))
        pygame.draw.rect(screen, (255, 255, 255), (542, 311, 183, 30))
        if len(turn_bet) > 0:
            if int(turn_bet) > starting_money:
                turn_bet = str(starting_money)
        Bet_Raise_Money(562, 321, turn_bet)
    else:
        check_click_call = True

    # After click at raise button
    if click_raise:
        if check_click_raise:
            mini_time_left -= 1
            check_click_raise = False
        pygame.draw.rect(screen, (0, 0, 0), (522, 306, 222, 60))
        pygame.draw.rect(screen, (255, 255, 255), (542, 311, 183, 30))
        if len(turn_raise) > 0:
            if int(turn_raise) > starting_money:
                turn_raise = str(starting_money)
        Bet_Raise_Money(562, 321, turn_raise)
    else:
        check_click_raise = True

    # Check if it's your turn or not
    if check: #and time_start:
        if (click_call or click_raise) and time_left > 0:
            mini_time_left += 1
            My_turn(30, 320)
        elif time_left == 0 or end_turn or check_click_fold:
            check = False
            check_click_fold = False
            turn_bet = ""
            turn_raise = ""
            time_left = 10 #30
            screen1 = True
            screen2 = False
            screen3 = False
            if click_call:
                click_call = False
                mini_time_left -= 1
            if click_raise:
                click_raise = False
                mini_time_left -= 1
            Their_turn(30, 320)
            end_turn = False
        elif time_left > 0:
            mini_time_left += 1
            My_turn(30, 320)
        pygame.time.delay(100)
    elif not check: #and time_start:
        if time_left == 0 or end_turn:
            if check_click_fold_myturn:
                check = False
                turn_bet = ""
                turn_raise = ""
                time_left = 10
                Their_turn(30, 320)
                end_turn = False
            else:
                check = True
                turn_bet = ""
                turn_raise = ""
                time_left = 90000 #30
                My_turn(30, 320)
                end_turn = False
        elif time_left > 0:
            mini_time_left += 1
            Their_turn(30, 320)
        pygame.time.delay(100)

    # Show time on one's turn
    text_timeleft = str(time_left) + "s"
    Time_left(70, 360)

    '''if not time_start:
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 801, 451))
        Time_starting(200, 195)
        count -= 1
        text_count = str(count) + "s"
        Time_num(550, 195)
        pygame.time.delay(1000)
        if count == 0:
            time_start = True
    '''

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if check and e.type == pygame.MOUSEBUTTONDOWN and screen1:
            if e.button == 1:
                if rect_fold.collidepoint(e.pos):
                    click_fold = True
                    check_click_fold = True
                if rect_check.collidepoint(e.pos) and not check_bet:
                    click_check = True
                if rect_call.collidepoint(e.pos):
                    if not check_bet:
                        mini_time_left += 1
                        click_call = True
                        screen1 = False
                        screen2 = True
                    else:
                        end_turn = True
                        pot_money += last_bet
                        starting_money -= last_bet
                        text_starting_money = str(starting_money) + "$"
                if rect_raise.collidepoint(e.pos) and check_bet:
                    mini_time_left += 1
                    click_raise = True
                    screen1 = False
                    screen3 = True

        if e.type == pygame.KEYDOWN and check and screen2:
            if e.key == pygame.K_RETURN and len(turn_bet) == 0:
                screen2 = False
                screen1 = True
                click_call = False
            elif e.key == pygame.K_RETURN and len(turn_bet) > 0:
                screen2 = False
                screen1 = True
                click_call = False
                end_turn = True
                check_bet = True
                last_bet = int(turn_bet)
                pot_money += last_bet
                starting_money -= last_bet
                text_starting_money = str(starting_money) + "$"
            if e.key == pygame.K_0 and turn_bet == "":
                continue
            elif e.key == pygame.K_0 and int(turn_bet) == 0:
                continue
            elif e.key == pygame.K_0 and (int(turn_bet) != 0 or turn_bet != ""):
                turn_bet += "0"
            if e.key == pygame.K_1:
                turn_bet += "1"
            if e.key == pygame.K_2:
                turn_bet += "2"
            if e.key == pygame.K_3:
                turn_bet += "3"
            if e.key == pygame.K_4:
                turn_bet += "4"
            if e.key == pygame.K_5:
                turn_bet += "5"
            if e.key == pygame.K_6:
                turn_bet += "6"
            if e.key == pygame.K_7:
                turn_bet += "7"
            if e.key == pygame.K_8:
                turn_bet += "8"
            if e.key == pygame.K_9:
                turn_bet += "9"
            if e.key == pygame.K_BACKSPACE:
                turn_bet = turn_bet[:-1]

        if e.type == pygame.KEYDOWN and check and screen3:
            if e.key == pygame.K_RETURN and len(turn_raise) == 0:
                screen3 = False
                screen1 = True
                click_raise = False
            elif e.key == pygame.K_RETURN and len(turn_raise) > 0 and int(turn_raise) > last_bet:
                screen3 = False
                screen1 = True
                click_raise = False
                end_turn = True
                last_bet = int(turn_raise)
                pot_money += last_bet
                starting_money -= last_bet
                text_starting_money = str(starting_money) + "$"
            if e.key == pygame.K_0 and turn_raise == "":
                continue
            elif e.key == pygame.K_0 and int(turn_raise) == 0:
                continue
            elif e.key == pygame.K_0 and (int(turn_raise) != 0 or turn_raise != ""):
                turn_raise += "0"
            if e.key == pygame.K_1:
                turn_raise += "1"
            if e.key == pygame.K_2:
                turn_raise += "2"
            if e.key == pygame.K_3:
                turn_raise += "3"
            if e.key == pygame.K_4:
                turn_raise += "4"
            if e.key == pygame.K_5:
                turn_raise += "5"
            if e.key == pygame.K_6:
                turn_raise += "6"
            if e.key == pygame.K_7:
                turn_raise += "7"
            if e.key == pygame.K_8:
                turn_raise += "8"
            if e.key == pygame.K_9:
                turn_raise += "9"
            if e.key == pygame.K_BACKSPACE:
                turn_raise = turn_raise[:-1]

    time_change, mini_time_left = divmod(mini_time_left, 10)
    time_left -= time_change

    fpsClock.tick(FPS)
    pygame.display.update()

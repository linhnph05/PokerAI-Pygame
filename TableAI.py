import random, pygame, time, sys, number, rankcard

import money, numpy
import percentCalc as calc
import CalcFunction as calcFunc

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Poker')
background = pygame.image.load("Resource/poker_green_background.jpg")
background = pygame.transform.scale(background, (1280, 720))

reArrow = pygame.image.load("Resource/return_arrow.png")
reArrow = pygame.transform.scale(reArrow, (160, 160))
setting = pygame.image.load("Resource/Setting.png")
setting = pygame.transform.scale(setting, (80, 80))
#emoji = pygame.image.load("Resource/Emoji.png")
#emoji = pygame.transform.scale(emoji, (80, 80))
#chat = pygame.image.load("Resource/Chat.png")
#chat = pygame.transform.scale(chat, (80, 80))
table = pygame.image.load("Resource/Table.png")
table = pygame.transform.scale(table, (700, 500))
#woman = pygame.image.load("Resource/The woman.png")
#woman = pygame.transform.scale(woman, (160, 160))
cards_symbol = pygame.image.load("Resource/Cards Symbol.png")
cards_symbol = pygame.transform.scale(cards_symbol, (40, 40))
poker_night = pygame.image.load("Resource/Poker night.png")
poker_night = pygame.transform.scale(poker_night, (320, 160))
# ellipse = pygame.image.load("Resource/Ellipse.png")
# ellipse = pygame.transform.scale(ellipse, (144, 112))
yellow_ellipse = pygame.image.load("Resource/Yellow ellipse.png")
yellow_ellipse = pygame.transform.scale(yellow_ellipse, (160, 70))
total_money = pygame.image.load("Resource/Total money.png")
total_money = pygame.transform.scale(total_money, (150, 100))

big_blind = pygame.image.load("Resource/Big blind button.png")
big_blind = pygame.transform.scale(big_blind, (40, 40))
small_blind = pygame.image.load("Resource/Small blind button.png")
small_blind = pygame.transform.scale(small_blind, (40, 40))
dealer = pygame.image.load("Resource/Dealer button.png")
dealer = pygame.transform.scale(dealer, (40, 40))

Player_card_1 = pygame.image.load("Resource/8 of C.png")
Player_card_1 = pygame.transform.scale(Player_card_1, (100, 130))
Player_card_1 = pygame.transform.rotate(Player_card_1, 10)
Player_card_2 = pygame.image.load("Resource/Q of D.png")
Player_card_2 = pygame.transform.scale(Player_card_2, (100, 130))
Player_card_2 = pygame.transform.rotate(Player_card_2, -10)
Enemy1_card_1 = pygame.image.load("Resource/Flip card.png")
Enemy1_card_2 = pygame.image.load("Resource/Flip card.png")
Enemy2_card_1 = pygame.image.load("Resource/8 of C.png")
Enemy2_card_2 = pygame.image.load("Resource/Q of D.png")
Enemy3_card_1 = pygame.image.load("Resource/8 of C.png")
Enemy3_card_2 = pygame.image.load("Resource/Q of D.png")
Enemy4_card_1 = pygame.image.load("Resource/8 of C.png")
Enemy4_card_2 = pygame.image.load("Resource/Q of D.png")
Enemy5_card_1 = pygame.image.load("Resource/8 of C.png")
Enemy5_card_2 = pygame.image.load("Resource/Q of D.png")
Community_card_1 = pygame.image.load("Resource/8 of C.png")
Community_card_2 = pygame.image.load("Resource/8 of C.png")
Community_card_3 = pygame.image.load("Resource/8 of C.png")
Community_card_4 = pygame.image.load("Resource/8 of C.png")
Community_card_5 = pygame.image.load("Resource/8 of C.png")
Flip_card = pygame.image.load("Resource/Flip card.png")
Flip_card = pygame.transform.scale(Flip_card, (130, 140))
Flip_card_1 = pygame.image.load("Resource/Flip card.png")
Flip_card_1 = pygame.transform.scale(Flip_card_1, (130, 140))
Flip_card_1 = pygame.transform.rotate(Flip_card_1, 10)
Flip_card_2 = pygame.image.load("Resource/Flip card.png")
Flip_card_2 = pygame.transform.scale(Flip_card_2, (130, 140))
Flip_card_2 = pygame.transform.rotate(Flip_card_2, -10)
white_flag = pygame.image.load("Resource/White flag.png")
white_flag = pygame.transform.scale(white_flag, (40, 40))
crown = pygame.image.load("Resource/Crown.png")
crown = pygame.transform.scale(crown, (40, 40))
# Adam = pygame.image.load("Resource/Adam.png")
# Adam = pygame.transform.scale(Adam, (960, 560))

FPS = 60
fpsClock = pygame.time.Clock()

fontHeading = pygame.font.Font('Resource/Calibri Bold.TTF', 96)
fontInline = pygame.font.Font('Resource/Calibri Bold.TTF', 64)
fontSmall = pygame.font.Font('Resource/Calibri Bold.TTF', 32)
fontTiny = pygame.font.Font('Resource/Calibri Bold.TTF', 24)


def Return(mouse_position, click):
    # screen.blit(reArrow, (x, y))
    rect = pygame.Rect(30, 30, 104, 104)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.game_in_session = False
            number.current_screen = 0


def Setting(mouse_position, click):
    # screen.blit(reArrow, (x, y))
    rect = pygame.Rect(1150, 40, 104, 104)
    # pygame.draw.rect(screen,(0,0,0),rect,1)
    if rect.collidepoint((mouse_position)):
        if click == True:
            number.current_screen = 2


def Name(x, y, thename):
    name = fontTiny.render(thename, True, (255, 255, 255))
    screen.blit(name, (x, y))


def Name_White(x, y, thename):
    name = fontTiny.render(thename, True, (255, 255, 255))
    screen.blit(name, (x, y))


def Name_Red(x, y, thename):
    name = fontTiny.render(thename, True, (255, 0, 0))
    screen.blit(name, (x, y))


# def Avatar(x, y):
#     avatar = fontTiny.render("AVATAR", True, (0, 0, 0))
#     screen.blit(avatar, (x, y))


def Money(x, y, player_money):
    money = str(player_money)
    res = fontTiny.render('$' + money, True, (255, 255, 255))
    screen.blit(res, (x, y))


def Money2(x, y, player_money):
    money = str(player_money)
    res = fontTiny.render('$' + money, True, (0, 0, 0))
    screen.blit(res, (x, y))


def Start(x, y):
    start = fontSmall.render("Start", True, (255, 255, 255))
    screen.blit(start, (x, y))


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


def Time_num(text_count, x, y):
    time_num = fontHeading.render(text_count, True, (0, 0, 0))
    screen.blit(time_num, (x, y))


def My_turn(x, y):
    my_turn = fontSmall.render("My turn:", True, (255, 255, 255))
    screen.blit(my_turn, (x, y))


def Their_turn(x, y):
    their_turn = fontSmall.render("Their turn:", True, (255, 255, 255))
    screen.blit(their_turn, (x, y))


def Time_left(timeleft, x, y):
    time = fontInline.render(str(timeleft) + 's', True, (255, 255, 255))
    screen.blit(time, (x, y))


def Define():
    global list_current_money, blindMoney, each_player_card, playercount, time_left
    list_current_money = [number.starting_money] * 7
    blindMoney = number.blindMoney
    playercount = int(number.player_count)
    time_left = number.time_set
    # each_player_card = numpy.zeros(((playercount + 1), 7))


HOLD = []


def Randomize(location):
    t = random.randint(0, 51)
    while (taken[t] == True): t = random.randint(0, 51)
    taken[t] = True
    global thecard, index, HOLD
    index[t] = location
    thecard = "Resource/" + listofcards[t]
    HOLD.append(listCardCalc[t])
    '''yeah=fontHeading.render(thecard, True, (255, 255, 255))
    screen.blit(yeah,(x,y))'''


def Bet_Raise_Money(x, y, amountofmoney):
    bet_raise_money = fontSmall.render('$' + amountofmoney, True, (0, 0, 0))
    screen.blit(bet_raise_money, (x, y))


# Hàm check coi tất cả phần tử trong mảng có bằng nhau và tất cả phần tử có lớn hơn 0 ko
def checkbetDone():
    global listBet, playercount, has_not_fold
    mini = 1000000
    maxi = -1
    cnt = 0
    checkPlayer = 0
    currentplayer = 0
    for i in range(playercount):
        if (has_not_fold[i] == True): currentplayer += 1
        if (listBet[i] > 0 and has_not_fold[i] == True): cnt = cnt + 1
        if (listCheck[i] > 0 and has_not_fold[i] == True): checkPlayer += 1

    if (cnt == currentplayer):
        for i in range(playercount):
            if (listBet[i] != 0 and listBet[i] != -1 and has_not_fold[i] == True):
                mini = min(mini, listBet[i])
                maxi = max(maxi, listBet[i])

    if (mini == maxi or checkPlayer == currentplayer):
        betDone = True
    else:
        betDone = False
    return betDone


def createListHB(Round):
    global HOLD, listBoard

    if Round == 1:
        listBoard = None
    elif Round < 5:
        listBoard = []
        for i in range(0, Round + 1):
            listBoard.append(HOLD[i])

        listBoard = calcFunc.create_board(listBoard)

    tempHold = HOLD.copy();
    for i in range(0, 5):
        tempHold.pop(0)

    listHold = calcFunc.create_hole_cards(tempHold)
    listDeck = calcFunc.generate_deck(listHold, listBoard)

    return listHold, listBoard, listDeck


def update_turn():
    global listofcards, listBet, SBindex, BBindex, pot_money, playercount, has_not_fold, deal, active_player
    for i in range(playercount):
        Name_White(locateName[i][0], locateName[i][1], listofnames[i])
        Money2(locateMoney[i][0], locateMoney[i][1], listBet[i])
        if (has_not_fold[i] == False):
            screen.blit(white_flag, locateWhiteflag[i])
    Name_Red(locateName[turn][0], locateName[turn][1], listofnames[turn])
    if (active_player > 2):
        screen.blit(dealer, locateBlind[deal])
        screen.blit(small_blind, (locateBlind[(SBindex) % playercount]))
        screen.blit(big_blind, locateBlind[(BBindex) % playercount])
    elif (active_player == 2):
        screen.blit(small_blind, (locateBlind[(SBindex) % playercount]))
        screen.blit(big_blind, locateBlind[(BBindex) % playercount])
    Money(610, 190, pot_money)


listofcards = ["2 of S.png", "2 of C.png", "2 of D.png", "2 of H.png"
    , "3 of S.png", "3 of C.png", "3 of D.png", "3 of H.png"
    , "4 of S.png", "4 of C.png", "4 of D.png", "4 of H.png"
    , "5 of S.png", "5 of C.png", "5 of D.png", "5 of H.png"
    , "6 of S.png", "6 of C.png", "6 of D.png", "6 of H.png"
    , "7 of S.png", "7 of C.png", "7 of D.png", "7 of H.png"
    , "8 of S.png", "8 of C.png", "8 of D.png", "8 of H.png"
    , "9 of S.png", "9 of C.png", "9 of D.png", "9 of H.png"
    , "10 of S.png", "10 of C.png", "10 of D.png", "10 of H.png"
    , "J of S.png", "J of C.png", "J of D.png", "J of H.png"
    , "Q of S.png", "Q of C.png", "Q of D.png", "Q of H.png"
    , "K of S.png", "K of C.png", "K of D.png", "K of H.png"
    , "A of S.png", "A of C.png", "A of D.png", "A of H.png"]

listCardCalc = ["2s", "2c", "2d", "2h"
    , "3s", "3c", "3d", "3h"
    , "4s", "4c", "4d", "4h"
    , "5s", "5c", "5d", "5h"
    , "6s", "6c", "6d", "6h"
    , "7s", "7c", "7d", "7h"
    , "8s", "8c", "8d", "8h"
    , "9s", "9c", "9d", "9h"
    , "Ts", "Tc", "Td", "Th"
    , "Js", "Jc", "Jd", "Jh"
    , "Qs", "Qc", "Qd", "Qh"
    , "Ks", "Kc", "Kd", "Kh"
    , "As", "Ac", "Ad", "Ah"]

listofnames = ["Player", "Bot 1", "Bot 2", "Bot 3", "Bot 4", "Bot 5"]

# General
index = [-1] * 53  # index[x] = y có nghĩa là lá bài ở vị trí x trong listofcards có người ở vị trí y cầm, Vị trí 0 là community
thecard = ""  # Lá bài
blindMoney = number.blindMoney
taken = [False] * 53  # taken[x] = True có nghĩa là lá ở vị trí x đã được lấy rồi, False là chưa được lấy
has_not_fold = [True] * 7
list_current_money = [number.starting_money] * 7  # So tien hien tai moi nguoi choi
each_player_card = [[0 for i in range(7)] for j in range(7)]
begin_match = True
begin_round = True
your_turn = True
isCountingTime = True
waiting = False
turn = 1
allin = False
playercount = number.player_count
winner = [-1] * playercount
thefold = False
countwinner = -1
start_count = True

# Time
time_left = number.time_set

# Check, call, bet, raise, fold
ktcheckbet = True  # Kt da chay checkbetDone 1 lan chua, neu roi thi False boi vi chi can cong vo pot_money 1 lan
check = True
end_turn = False
last_bet = 0  # Số tiền cược trước đó(nếu có)
pot_money = 0
money_bet = ""  # Tiền hiện thị khi nhập số tiền bet
money_raise = ""
check_bet = False
minbet = 0
turn_bet = ""
turn_raise = ""
click_start = False
click_call = False
click_raise = False
click_check = False
check_click_fold = False
text_starting_money = str(number.starting_money)
active_player = 0

"""
Screen1 giao diện hiển thị bàn chơi các thứ
Scr2 hiển thị scr bet
Scr3 hiển thị scr raise
Biến scr 1 2 3 chỉ để dùng để cho con trỏ ko ấn ngoài mấy cái scr còn lại khi 1 cái hoạt động thôi
"""
'''screen1 = True
screen2 = False
screen3 = False'''

# số người chơi number.player_count
match = 1  # Số thứ tự trận
end_match = False
deal = 0  # Mặc định vị trí dealer ban đầu là 1
locateEllipse = [(570, 380), (310, 300), (310, 190), (570, 110), (830, 190), (830, 300)]
locateName = [(555, 545), (135, 395), (135, 195), (385, 95), (975, 195), (975, 395)]
locateMoney = [(610, 405), (350, 325), (350, 215), (610, 135), (870, 215), (870, 325)]
locateBlind = [(680, 550), (260, 400), (260, 200), (510, 100), (1100, 200), (1115, 400)]
locateWhiteflag = [(545, 505), (125, 355), (125, 155), (375, 55), (1145, 155), (1145, 355)]

# Khởi tạo biến từng trận
time_in_seconds = 0
TICK = pygame.USEREVENT + 1
pygame.time.set_timer(TICK, 1000)  # fire the event (tick) every second
turn = deal  # vị trí hành động
Round = 1  # số vòng
'''isBet = False  # đã có người đặt cược trước đó chưa
betDone = False  # vòng đó đã đặt cược xong chưa'''

# Tạo mảng chỉ số tiền cược của mỗi người chơi, có n phần tử, mỗi phần tử ban đầu bằng 0
listBet = [0] * 7
listCheck = [0] * 7


# pre_flop = True

def TableAIx():
    # while True:
    number.game_in_session = True

    # Variable
    click = False
    global Enemy1_card_1, Enemy1_card_2, Enemy2_card_1, Enemy2_card_2, Enemy3_card_1, Enemy3_card_2
    global Enemy4_card_1, Enemy4_card_2, Enemy5_card_1, Enemy5_card_2, winner, TICK
    global Community_card_1, Community_card_2, Community_card_3, Community_card_4, Community_card_5
    global thecard, deck, time_left, mini_time_left, text_timeleft, check, round_begin, time_start, count, text_count, isCountingTime
    global end_turn, bet, last_bet, pot_money, check_bet, minbet, turn_bet, turn_raise, click_call, check_click_call
    global click_raise, check_click_raise, click_check, click_fold, check_click_fold, check_click_fold_myturn
    global time_change, screen1, screen2, screen3, Player_card_1, Player_card_2, flip_card_1, flip_card_2
    global text_starting_money, end_match, has_not_fold, each_player_card, click_start, total_money
    global turn, pre_flop, betDone, Round, SBindex, BBindex, deal, match, end_match, begin_match
    global locateEllipse, locateName, locateMoney, listofnames, begin_match, turn, pot_money, money_raise
    global time_in_seconds, index, blindMoney, list_current_money, playercount, taken, allin, your_turn
    global ktcheckbet, waiting, thefold, active_player, winner, countwinner, start_count
    global HOLD, percent, listHold, listBoard, listDeck
    mouse_position = pygame.mouse.get_pos()


    # Always appear detail
    # Details
    screen.blit(background, (0, 0))
    screen.blit(setting, (1160, 50))
    screen.blit(table, (300, 30))
    screen.blit(cards_symbol, (525, 175))
    screen.blit(poker_night, (705, 150))
    screen.blit(reArrow, (0, 0))
    screen.blit(total_money, (574, 150))
    # Buttons
    pygame.draw.rect(screen, (255, 0, 0), (170, 616, 138, 66))
    rect_start = pygame.rect.Rect(170, 616, 138, 66)
    Start(200, 632)
    pygame.draw.rect(screen, (255, 0, 0), (360, 616, 138, 66))
    rect_fold = pygame.rect.Rect(360, 616, 138, 66)
    Fold(400, 632)
    pygame.draw.rect(screen, (255, 0, 0), (560, 616, 160, 66))
    rect_check = pygame.rect.Rect(560, 616, 160, 66)
    Check(600, 632)
    pygame.draw.rect(screen, (255, 0, 0), (787, 616, 190, 66))
    rect_call = pygame.rect.Rect(787, 616, 190, 66)
    Call_Bet(827, 632)
    pygame.draw.rect(screen, (255, 0, 0), (1040, 616, 150, 66))
    rect_raise = pygame.rect.Rect(1040, 616, 150, 66)
    Raise(1080, 632)

    # Start of the game
    if (begin_match == True):
        # Dealer, Small Blind, Big Blind, and who play
        for i in range(0, playercount):
            Name_White(locateName[i][0], locateName[i][1], listofnames[i])
        Name_Red(locateName[(deal + 3) % playercount][0], locateName[(deal + 3) % playercount][1],
                 listofnames[(deal + 3) % playercount])

        active_player = 0
        for i in range(0, playercount):
            if (list_current_money[i] < blindMoney * 2):
                has_not_fold[i] = False
            else:
                active_player += 1
        while (has_not_fold[deal] == False): deal = (deal + 1) % playercount
        if (active_player > 2):
            turn = (deal + 1) % playercount
            # Di chuyển qua SB để SB đặt cược
            while (list_current_money[turn] < blindMoney * 2):
                turn = (turn + 1) % playercount
            SBindex = turn  # vị trí của SB
            listBet[(SBindex) % playercount] = blindMoney
            list_current_money[SBindex % playercount] -= blindMoney
            turn = (turn + 1) % playercount

            # Di chuyển qua BB để BB đặt cược
            while (list_current_money[turn] < blindMoney * 2):
                turn = (turn + 1) % playercount
            BBindex = turn
            listBet[(BBindex) % playercount] = 2 * blindMoney
            list_current_money[(BBindex) % playercount] -= (blindMoney * 2)
            turn = (turn + 1) % playercount
            last_bet = 2 * blindMoney

        elif active_player == 2:

            while (list_current_money[turn] < blindMoney * 2):
                turn = (turn + 1) % playercount
            SBindex = turn  # vị trí của SB
            listBet[(SBindex) % playercount] = blindMoney
            list_current_money[SBindex % playercount] -= blindMoney
            turn = (turn + 1) % playercount

            while (list_current_money[turn] < blindMoney * 2):
                turn = (turn + 1) % playercount
            BBindex = turn
            listBet[(BBindex) % playercount] = 2 * blindMoney
            list_current_money[(BBindex) % playercount] -= (blindMoney * 2)
            last_bet = 2 * blindMoney
            turn = (turn + 1) % playercount

        HOLD.clear()
        # Dua 2 la bai cho tung nguoi
        Randomize(0)
        Community_card_1 = pygame.image.load(thecard)
        Community_card_1 = pygame.transform.scale(Community_card_1, (90, 120))
        Randomize(0)
        Community_card_2 = pygame.image.load(thecard)
        Community_card_2 = pygame.transform.scale(Community_card_2, (90, 120))
        Randomize(0)
        Community_card_3 = pygame.image.load(thecard)
        Community_card_3 = pygame.transform.scale(Community_card_3, (90, 120))
        Randomize(0)
        Community_card_4 = pygame.image.load(thecard)
        Community_card_4 = pygame.transform.scale(Community_card_4, (90, 120))
        Randomize(0)
        Community_card_5 = pygame.image.load(thecard)
        Community_card_5 = pygame.transform.scale(Community_card_5, (90, 120))

        Randomize(1)
        Player_card_1 = pygame.image.load(thecard)
        Player_card_1 = pygame.transform.scale(Player_card_1, (100, 130))
        Player_card_1 = pygame.transform.rotate(Player_card_1, 10)
        Randomize(1)
        Player_card_2 = pygame.image.load(thecard)
        Player_card_2 = pygame.transform.scale(Player_card_2, (100, 130))
        Player_card_2 = pygame.transform.rotate(Player_card_2, -10)

        Randomize(2)
        Enemy1_card_1 = pygame.image.load(thecard)
        Enemy1_card_1 = pygame.transform.scale(Enemy1_card_1, (100, 130))
        Enemy1_card_1 = pygame.transform.rotate(Enemy1_card_1, 10)
        Randomize(2)
        Enemy1_card_2 = pygame.image.load(thecard)
        Enemy1_card_2 = pygame.transform.scale(Enemy1_card_2, (100, 130))
        Enemy1_card_2 = pygame.transform.rotate(Enemy1_card_2, -10)

        if (playercount > 2):
            Randomize(3)
            Enemy2_card_1 = pygame.image.load(thecard)
            Enemy2_card_1 = pygame.transform.scale(Enemy2_card_1, (100, 130))
            Enemy2_card_1 = pygame.transform.rotate(Enemy2_card_1, 10)
            Randomize(3)
            Enemy2_card_2 = pygame.image.load(thecard)
            Enemy2_card_2 = pygame.transform.scale(Enemy2_card_2, (100, 130))
            Enemy2_card_2 = pygame.transform.rotate(Enemy2_card_2, -10)

        if (playercount > 3):
            Randomize(4)
            Enemy3_card_1 = pygame.image.load(thecard)
            Enemy3_card_1 = pygame.transform.scale(Enemy3_card_1, (100, 130))
            Enemy3_card_1 = pygame.transform.rotate(Enemy3_card_1, 10)
            Randomize(4)
            Enemy3_card_2 = pygame.image.load(thecard)
            Enemy3_card_2 = pygame.transform.scale(Enemy3_card_2, (100, 130))
            Enemy3_card_2 = pygame.transform.rotate(Enemy3_card_2, -10)

        if (playercount > 4):
            Randomize(5)
            Enemy4_card_1 = pygame.image.load(thecard)
            Enemy4_card_1 = pygame.transform.scale(Enemy4_card_1, (100, 130))
            Enemy4_card_1 = pygame.transform.rotate(Enemy4_card_1, 10)
            Randomize(5)
            Enemy4_card_2 = pygame.image.load(thecard)
            Enemy4_card_2 = pygame.transform.scale(Enemy4_card_2, (100, 130))
            Enemy4_card_2 = pygame.transform.rotate(Enemy4_card_2, -10)

        if (playercount > 5):
            Randomize(6)
            Enemy5_card_1 = pygame.image.load(thecard)
            Enemy5_card_1 = pygame.transform.scale(Enemy5_card_1, (100, 130))
            Enemy5_card_1 = pygame.transform.rotate(Enemy5_card_1, 10)
            Randomize(6)
            Enemy5_card_2 = pygame.image.load(thecard)
            Enemy5_card_2 = pygame.transform.scale(Enemy5_card_2, (100, 130))
            Enemy5_card_2 = pygame.transform.rotate(Enemy5_card_2, -10)

        listHold, listBoard, listDeck = createListHB(Round)
        percent = calc.run_simulation(listHold, listBoard, listDeck)

        begin_match = False

    # Fold thi ko di dc
    while (has_not_fold[turn] == False): turn = (turn + 1) % playercount

    # Neu con lai 1 nguoi thi nguoi ay thang
    cnt = 0
    for i in range(playercount):
        if (has_not_fold[i] == True): cnt += 1
    if (cnt == 1):
        countwinner = 0
        winner[0] = turn
        end_match = True

    # Check showdown hay ko,
    if (Round == 5):

        # Showdown thi show tat ca la bai va xep hang la bai
        screen.blit(Community_card_1, (443, 240))
        screen.blit(Community_card_2, (525, 240))
        screen.blit(Community_card_3, (608, 240))
        screen.blit(Community_card_4, (688, 240))
        screen.blit(Community_card_5, (773, 240))

        # Player
        if has_not_fold[0] == True:
            screen.blit(Player_card_1, (570, 450))
            screen.blit(Player_card_2, (600, 450))
        pygame.draw.rect(screen, (142, 142, 142), (550, 540, 200, 30))
        rect_name = pygame.rect.Rect(550, 540, 200, 30)
        Name(555, 545, listofnames[0])
        pygame.draw.rect(screen, (142, 142, 142), (550, 570, 200, 30))
        rect_mon = pygame.rect.Rect(550, 570, 200, 30)
        Money(555, 575, list_current_money[0])
        screen.blit(yellow_ellipse, (570, 380))

        # Enemy Player 1
        if has_not_fold[1] == True:
            screen.blit(Enemy1_card_1, (150, 300))
            screen.blit(Enemy1_card_2, (180, 300))
        pygame.draw.rect(screen, (142, 142, 142), (130, 390, 200, 30))
        rect_name = pygame.rect.Rect(130, 390, 200, 30)
        Name(135, 395, listofnames[1])
        pygame.draw.rect(screen, (142, 142, 142), (130, 420, 200, 30))
        rect_mon = pygame.rect.Rect(130, 420, 200, 30)
        Money(135, 425, list_current_money[1])
        screen.blit(yellow_ellipse, (310, 300))

        # Enemy Player 2
        if (playercount > 2):
            if has_not_fold[2] == True:
                screen.blit(Enemy2_card_1, (150, 100))
                screen.blit(Enemy2_card_2, (180, 100))
            pygame.draw.rect(screen, (142, 142, 142), (130, 190, 200, 30))
            rect_name = pygame.rect.Rect(130, 190, 200, 30)
            Name(135, 195, listofnames[2])
            pygame.draw.rect(screen, (142, 142, 142), (130, 220, 200, 30))
            rect_mon = pygame.rect.Rect(130, 220, 200, 30)
            Money(135, 225, list_current_money[2])
            screen.blit(yellow_ellipse, (310, 190))

        # Enemy Player 3
        if (playercount > 3):
            if has_not_fold[3] == True:
                screen.blit(Enemy3_card_1, (400, 0))
                screen.blit(Enemy3_card_2, (430, 0))
            pygame.draw.rect(screen, (142, 142, 142), (380, 90, 200, 30))
            rect_name = pygame.rect.Rect(380, 90, 200, 30)
            Name(385, 95, listofnames[3])
            pygame.draw.rect(screen, (142, 142, 142), (380, 120, 200, 30))
            rect_mon = pygame.rect.Rect(380, 90, 200, 30)
            Money(385, 125, list_current_money[3])
            screen.blit(yellow_ellipse, (570, 110))

        # Enemy Player 4
        if (playercount > 4):
            if has_not_fold[4] == True:
                screen.blit(Enemy4_card_1, (970, 100))
                screen.blit(Enemy4_card_2, (1000, 100))
            pygame.draw.rect(screen, (142, 142, 142), (970, 190, 200, 30))
            rect_name = pygame.rect.Rect(970, 190, 200, 30)
            Name(975, 195, listofnames[4])
            pygame.draw.rect(screen, (142, 142, 142), (970, 220, 200, 30))
            rect_mon = pygame.rect.Rect(970, 220, 200, 30)
            Money(975, 225, list_current_money[4])
            screen.blit(yellow_ellipse, (830, 190))

        # Enemy Player 5
        if (playercount > 5):
            if has_not_fold[5] == True:
                screen.blit(Enemy5_card_1, (970, 300))
                screen.blit(Enemy5_card_2, (1000, 300))
            pygame.draw.rect(screen, (142, 142, 142), (970, 390, 200, 30))
            rect_name = pygame.rect.Rect(970, 390, 200, 30)
            Name(975, 395, listofnames[5])
            pygame.draw.rect(screen, (142, 142, 142), (970, 420, 200, 30))
            rect_mon = pygame.rect.Rect(970, 420, 200, 30)
            Money(975, 425, list_current_money[5])
            screen.blit(yellow_ellipse, (830, 300))


    else:
        # Neu khong showdown thi du nguyen hien tai va co 1 so la bai up
        # Community Card
        if (Round == 1):
            screen.blit(Flip_card, (423, 230))
            screen.blit(Flip_card, (503, 230))
            screen.blit(Flip_card, (583, 230))
            screen.blit(Flip_card, (663, 230))
            screen.blit(Flip_card, (743, 230))

        if (Round == 2):
            screen.blit(Flip_card, (423, 230))
            screen.blit(Community_card_2, (525, 240))
            screen.blit(Community_card_3, (608, 240))
            screen.blit(Community_card_4, (688, 240))
            screen.blit(Flip_card, (746, 230))

        if (Round == 3):
            screen.blit(Community_card_1, (443, 240))
            screen.blit(Community_card_2, (525, 240))
            screen.blit(Community_card_3, (608, 240))
            screen.blit(Community_card_4, (688, 240))
            screen.blit(Flip_card, (746, 230))

        if (Round == 4):
            screen.blit(Community_card_1, (443, 240))
            screen.blit(Community_card_2, (525, 240))
            screen.blit(Community_card_3, (608, 240))
            screen.blit(Community_card_4, (688, 240))
            screen.blit(Community_card_5, (773, 240))

        # Player
        if has_not_fold[0] == True:
            screen.blit(Player_card_1, (570, 450))
            screen.blit(Player_card_2, (600, 450))
        pygame.draw.rect(screen, (142, 142, 142), (550, 540, 200, 30))
        rect_name = pygame.rect.Rect(550, 540, 200, 30)
        Name(555, 545, listofnames[0])
        pygame.draw.rect(screen, (142, 142, 142), (550, 570, 200, 30))
        rect_mon = pygame.rect.Rect(550, 570, 200, 30)
        Money(555, 575, list_current_money[0])
        screen.blit(yellow_ellipse, (570, 380))

        # Enemy Player 1
        if has_not_fold[1] == True:
            screen.blit(Flip_card_1, (150, 300))
            screen.blit(Flip_card_2, (180, 300))
        pygame.draw.rect(screen, (142, 142, 142), (130, 390, 200, 30))
        rect_name = pygame.rect.Rect(130, 390, 200, 30)
        Name(135, 395, listofnames[1])
        pygame.draw.rect(screen, (142, 142, 142), (130, 420, 200, 30))
        rect_mon = pygame.rect.Rect(130, 420, 200, 30)
        Money(135, 425, list_current_money[1])
        screen.blit(yellow_ellipse, (310, 300))

        # Enemy Player 2
        if (playercount > 2):
            if has_not_fold[2] == True:
                screen.blit(Flip_card_1, (150, 100))
                screen.blit(Flip_card_2, (180, 100))
            pygame.draw.rect(screen, (142, 142, 142), (130, 190, 200, 30))
            rect_name = pygame.rect.Rect(130, 190, 200, 30)
            Name(135, 195, listofnames[2])
            pygame.draw.rect(screen, (142, 142, 142), (130, 220, 200, 30))
            rect_mon = pygame.rect.Rect(130, 220, 200, 30)
            Money(135, 225, list_current_money[2])
            screen.blit(yellow_ellipse, (310, 190))

        # Enemy Player 3
        if (playercount > 3):
            if has_not_fold[3] == True:
                screen.blit(Flip_card_1, (400, 0))
                screen.blit(Flip_card_2, (430, 0))
            pygame.draw.rect(screen, (142, 142, 142), (380, 90, 200, 30))
            rect_name = pygame.rect.Rect(380, 90, 200, 30)
            Name(385, 95, listofnames[3])
            pygame.draw.rect(screen, (142, 142, 142), (380, 120, 200, 30))
            rect_mon = pygame.rect.Rect(380, 90, 200, 30)
            Money(385, 125, list_current_money[3])
            screen.blit(yellow_ellipse, (570, 110))

        # Enemy Player 4
        if (playercount > 4):
            if has_not_fold[4] == True:
                screen.blit(Flip_card_1, (970, 100))
                screen.blit(Flip_card_2, (1000, 100))
            pygame.draw.rect(screen, (142, 142, 142), (970, 190, 200, 30))
            rect_name = pygame.rect.Rect(970, 190, 200, 30)
            Name(975, 195, listofnames[4])
            pygame.draw.rect(screen, (142, 142, 142), (970, 220, 200, 30))
            rect_mon = pygame.rect.Rect(970, 220, 200, 30)
            Money(975, 225, list_current_money[4])
            screen.blit(yellow_ellipse, (830, 190))

        # Enemy Player 5
        if (playercount > 5):
            if has_not_fold[5] == True:
                screen.blit(Flip_card_1, (970, 300))
                screen.blit(Flip_card_2, (1000, 300))
            pygame.draw.rect(screen, (142, 142, 142), (970, 390, 200, 30))
            rect_name = pygame.rect.Rect(970, 390, 200, 30)
            Name(975, 395, listofnames[5])
            pygame.draw.rect(screen, (142, 142, 142), (970, 420, 200, 30))
            rect_mon = pygame.rect.Rect(970, 420, 200, 30)
            Money(975, 425, list_current_money[5])
            screen.blit(yellow_ellipse, (830, 300))

    if (Round == 5 and end_match == False):
        dem = [0] * 7
        for i in range(53):
            if (index[i] == -1):
                pass
            elif (index[i] == 0):
                for j in range(0, playercount):
                    each_player_card[j][dem[j]] = i
                    dem[j] = dem[j] + 1
            else:
                each_player_card[index[i] - 1][dem[index[i] - 1]] = i
                dem[index[i] - 1] = dem[index[i] - 1] + 1

        '''#f = open('reso.py','w')
        with open('reso.py','w') as f:
        for i in range(0,playercount):
            for j in range(7):
                res=str(listofcards[each_player_card[i][j]])
                f.write(res +" ")
            f.write("\n")'''

        ranking = [0] * 7
        for i in range(0, playercount):
            if has_not_fold[i] == True:
                string_card = [""] * 7
            for j in range(7):
                string_card[j] = listofcards[each_player_card[i][j]]
            rankcard.setup_mang(string_card)
            if rankcard.ranking_cards() == "Royal Flush":
                ranking[i] = 10
            elif rankcard.ranking_cards() == "Straight Flush":
                ranking[i] = 9
            elif rankcard.ranking_cards() == "Quads":
                ranking[i] = 8
            elif rankcard.ranking_cards() == "Full House":
                ranking[i] = 7
            elif rankcard.ranking_cards() == "Flush":
                ranking[i] = 6
            elif rankcard.ranking_cards() == "Straight":
                ranking[i] = 5
            elif rankcard.ranking_cards() == "Three":
                ranking[i] = 4
            elif rankcard.ranking_cards() == "Two Pair":
                ranking[i] = 3
            elif rankcard.ranking_cards() == "Pair":
                ranking[i] = 2
            elif rankcard.ranking_cards() == "High Card":
                ranking[i] = 1

        maximum = -1
        winner = [-1] * playercount
        countwinner = -1
        for i in range(0, playercount):
            if has_not_fold[i] == True:
                if ranking[i] > maximum:
                    countwinner = 0
                    winner[countwinner] = i
                    maximum = ranking[i]
                if ranking[i] == maximum:
                    countwinner = countwinner + 1
                    winner[countwinner] = i

        end_match = True

    # Dua cho screen vi tri hien tai cua cac thu
    update_turn()

    # Check nguoi hay bot dang di
    if (turn == 0):
        your_turn = True
    else:
        your_turn = False
        isCountingTime = True

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == TICK:
            if (end_match == True or checkbetDone() == True or waiting == True):
                time_in_seconds += 1
            if (your_turn == True): time_left -= 1
        if e.type == pygame.MOUSEBUTTONDOWN:
            number.Sound.click_channel.play(number.Sound.click_sound)
            # turn = (turn + 1)%6
            click = True
        if e.type == pygame.KEYDOWN and click_raise == True:
            # Thay so cho slider tang tien
            if e.key == pygame.K_RETURN:
                if (money_raise != ""):
                    if int(money_raise) > last_bet - listBet[turn]:
                        list_current_money[turn] = list_current_money[turn] - int(money_raise) + listBet[turn]
                        click_raise = False
                        listBet[turn] = int(money_raise)
                        last_bet = int(money_raise)
                        turn = (turn + 1) % playercount
            if e.key == pygame.K_BACKSPACE:
                money_raise = money_raise[:-1]
            if e.key == pygame.K_0 and money_raise != "" and (int(money_raise + "0") <= list_current_money[turn]) + \
                    listBet[turn]:
                money_raise += "0"
            if e.key == pygame.K_1 and int(money_raise + "1") <= list_current_money[turn] + listBet[turn]:
                money_raise += "1"
            if e.key == pygame.K_2 and int(money_raise + "2") <= list_current_money[turn] + listBet[turn]:
                money_raise += "2"
            if e.key == pygame.K_3 and int(money_raise + "3") <= list_current_money[turn] + listBet[turn]:
                money_raise += "3"
            if e.key == pygame.K_4 and int(money_raise + "4") <= list_current_money[turn] + listBet[turn]:
                money_raise += "4"
            if e.key == pygame.K_5 and int(money_raise + "5") <= list_current_money[turn] + listBet[turn]:
                money_raise += "5"
            if e.key == pygame.K_6 and int(money_raise + "6") <= list_current_money[turn] + listBet[turn]:
                money_raise += "6"
            if e.key == pygame.K_7 and int(money_raise + "7") <= list_current_money[turn] + listBet[turn]:
                money_raise += "7"
            if e.key == pygame.K_8 and int(money_raise + "8") <= list_current_money[turn] + listBet[turn]:
                money_raise += "8"
            if e.key == pygame.K_9 and int(money_raise + "9") <= list_current_money[turn] + listBet[turn]:
                money_raise += "9"

    # Nguoi choi choi
    if (your_turn == True and waiting == False and not end_match):

        if (time_left == 0):
            #time_left = number.time_set
            has_not_fold[turn] = False
            turn = (turn + 1) % playercount
        if(isCountingTime):
            time_left = number.time_set
            isCountingTime = False
        #has_not_fold[turn] = False
        #turn = (turn + 1) % playercount
        My_turn(90, 560)
        Time_left(time_left, 230, 550)

        # Ham kiem tra fold
        if (rect_fold.collidepoint(mouse_position)):
            if (click == True and end_match == False and checkbetDone() == False):
                has_not_fold[turn] = False
                turn = (turn + 1) % playercount
                if (click_raise == True):
                    click_raise = False

        # Ham kiem tra check
        if (rect_check.collidepoint(mouse_position)):
            if (
                    click == True and Round >= 2 and click_raise == False and end_match == False and checkbetDone() == False):
                if (last_bet == 0 and list_current_money[turn] > 0):
                    listBet[turn] = 0
                    Money2(locateMoney[turn][0], locateMoney[turn][1], listBet[turn])
                    last_bet = listBet[turn]
                    turn = (turn + 1) % playercount

        # Ham kiem tra call
        if (rect_call.collidepoint(mouse_position)):
            if (click == True and click_raise == False and end_match == False and checkbetDone() == False):
                if (last_bet > 0 and list_current_money[turn] + listBet[turn] >= last_bet):
                    list_current_money[turn] = list_current_money[turn] - last_bet + listBet[turn]
                    listBet[turn] = last_bet
                    Money2(locateMoney[turn][0], locateMoney[turn][1], listBet[turn])
                    turn = (turn + 1) % playercount
                elif (last_bet == 0):
                    click_raise = True
                    pygame.draw.rect(screen, (255, 255, 255), (835, 490, 355, 96))
                    # rect_bet = pygame.rect.Rect(492, 200, 218, 176)
                    pygame.draw.rect(screen, (255, 255, 255), (867, 498, 293, 48))
                    money_raise = ""
                    # turn = (turn + 1) % playercount
            elif (click == True and click_raise == True and end_match == False and checkbetDone() == False):
                click_raise = False
                money_raise = ""

        # Ham kiem tra raise
        if (rect_raise.collidepoint(mouse_position)):
            if (
                    click == True and click_raise == False and last_bet > 0 and end_match == False and checkbetDone() == False):
                click_raise = True
                pygame.draw.rect(screen, (255, 255, 255), (835, 490, 355, 96))
                # rect_bet = pygame.rect.Rect(492, 200, 218, 176)
                pygame.draw.rect(screen, (255, 255, 255), (867, 498, 293, 48))
                money_raise = ""
            elif (click == True and click_raise == True and end_match == False and checkbetDone() == False):
                click_raise = False
                money_raise = ""
            # turn = (turn + 1) % playercount

        # Check cai slider tang tien con ton tai
        if (click_raise == True and end_match == False and checkbetDone() == False):
            pygame.draw.rect(screen, (255, 255, 255), (835, 490, 355, 96))
            pygame.draw.rect(screen, (255, 255, 255), (867, 498, 293, 48))
            Bet_Raise_Money(900, 514, money_raise)

    # Bot choi
    if (your_turn == False and waiting == False and not end_match):
        if number.current_level == "Easy" or number.current_level == "Normal":
            button = random.randint(1, 5)
            # Fold
            if (button == 1):
                if (end_match == False and checkbetDone() == False):
                    waiting = True
                    thefold = True
                    # has_not_fold[turn] = False

            # Check
            if (button == 2):
                if (Round >= 2 and end_match == False and checkbetDone() == False):
                    if (last_bet == 0 and list_current_money[turn] > 0):
                        waiting = True
                        listBet[turn] = 0
                        Money2(locateMoney[turn][0], locateMoney[turn][1], listBet[turn])
                        last_bet = listBet[turn]
                        listCheck[turn] = 1

            # Call/Bet
            if (button == 3 or button == 4):
                if (end_match == False and checkbetDone() == False):
                    if (last_bet > 0 and list_current_money[turn] + listBet[turn] >= last_bet):
                        waiting = True
                        list_current_money[turn] = list_current_money[turn] - last_bet + listBet[turn]
                        listBet[turn] = last_bet
                        Money2(locateMoney[turn][0], locateMoney[turn][1], listBet[turn])

                    elif (last_bet == 0 and list_current_money[turn] > 0):
                        waiting = True
                        bet = round(blindMoney / 2 * number.multiplier)
                        if (bet > list_current_money[turn]): bet = list_current_money[turn]
                        list_current_money[turn] -= bet
                        listBet[turn] = bet
                        last_bet = bet
                        Money2(locateMoney[turn][0], locateMoney[turn][1], listBet[turn])

            # Raise
            if (button == 5):
                if (last_bet > 0 and end_match == False and checkbetDone() == False and list_current_money[turn] +
                        listBet[turn] >= last_bet):
                    waiting = True
                    bet = round(last_bet * number.multiplier)
                    if (bet > list_current_money[turn] + listBet[turn]): bet = list_current_money[turn] + listBet[turn]
                    list_current_money[turn] = list_current_money[turn] - bet + listBet[turn]
                    listBet[turn] = bet
                    last_bet = bet
                    Money2(locateMoney[turn][0], locateMoney[turn][1], listBet[turn])

        elif number.current_level == "Hard":

            win_rate = percent[turn + 1]

            if win_rate > 0.1:
                if win_rate > 0.5:
                    button = 5
                else:
                    # If there is a chance to win, then call
                    button = 3
            else:
                button = random.randint(0, 2)
                if button == 0:
                    button = 1
                else:
                    button = 5

            while not waiting and not checkbetDone() and not end_match:

                # Fold
                if (button == 1):
                    if (end_match == False and checkbetDone() == False):
                        waiting = True
                        thefold = True
                        # has_not_fold[turn] = False

                # Check
                if (button == 2):
                    if (Round >= 2 and end_match == False and checkbetDone() == False):
                        if (last_bet == 0 and list_current_money[turn] > 0):
                            waiting = True
                            listBet[turn] = 0
                            Money2(locateMoney[turn][0], locateMoney[turn][1], listBet[turn])
                            last_bet = listBet[turn]
                            listCheck[turn] = 1

                    if not waiting:
                        button = 3

                # Call/Bet
                if (button == 3 or button == 4):
                    if (end_match == False and checkbetDone() == False):
                        if (last_bet > 0 and list_current_money[turn] + listBet[turn] >= last_bet):
                            waiting = True
                            list_current_money[turn] = list_current_money[turn] - last_bet + listBet[turn]
                            listBet[turn] = last_bet
                            Money2(locateMoney[turn][0], locateMoney[turn][1], listBet[turn])

                        elif (last_bet == 0 and list_current_money[turn] > 0):
                            waiting = True
                            bet = round(blindMoney / 2 * number.multiplier)
                            if (bet > list_current_money[turn]): bet = list_current_money[turn]
                            list_current_money[turn] -= bet
                            listBet[turn] = bet
                            last_bet = bet
                            Money2(locateMoney[turn][0], locateMoney[turn][1], listBet[turn])
                    if not waiting:
                        button = 1

                # Raise
                if (button == 5):
                    if (last_bet > 0 and end_match == False and checkbetDone() == False and list_current_money[turn] +
                            listBet[turn] >= last_bet):
                        waiting = True
                        bet = round(last_bet * number.multiplier)
                        if (bet > list_current_money[turn] + listBet[turn]): bet = list_current_money[turn] + listBet[
                            turn]
                        list_current_money[turn] = list_current_money[turn] - bet + listBet[turn]
                        listBet[turn] = bet
                        last_bet = bet
                        Money2(locateMoney[turn][0], locateMoney[turn][1], listBet[turn])
                    if not waiting:
                        button = 3

    # print("TRUE", turn, time_in_seconds)
    # Cho doi va qua luot

    if (waiting == True):
        if (time_in_seconds > 2):
            time_in_seconds = 0
            waiting = False

            if (thefold == True):
                has_not_fold[turn] = False
                thefold = False
            turn = (turn + 1) % playercount

        # Kiem tra tat ca bet da bang nhau chua, neu roi qua round tiep theo
    if (checkbetDone() == True and not end_match):
        if (ktcheckbet == True):
            for i in range(playercount):
                pot_money = pot_money + listBet[i]
                ktcheckbet = False
        if (time_in_seconds > 2):
            time_in_seconds = 0
            for i in range(playercount):
                listBet[i] = 0
                listCheck[i] = 0
            last_bet = 0
            ktcheckbet = True
            Round = Round + 1

            listHold, listBoard, listDeck = createListHB(Round)
            percent = calc.run_simulation(listHold, listBoard, listDeck)

    # Ket thuc va chuc mung nguoi chien thang, dat lai game
    if (end_match == True):
        screen.blit(crown, locateWhiteflag[turn])
        for i in range(countwinner + 1):
            screen.blit(crown, locateWhiteflag[winner[i]])
        if (rect_start.collidepoint(mouse_position) and click == True):
            time_in_seconds = 0
            for i in range(countwinner + 1):
                list_current_money[winner[i]] += pot_money
            for i in range(playercount):
                listBet[i] = 0
            match += 1
            deal = (deal + 1) % playercount
            Round = 1
            turn = deal
            index = [-1] * 53
            taken = [False] * 53
            has_not_fold = [True] * 7
            each_player_card = [[0 for i in range(7)] for j in range(7)]
            begin_round = True
            begin_match = True
            pot_money = 0
            winner = [-1] * playercount
            last_bet = 0
            end_match = False

    Setting(mouse_position, click)
    Return(mouse_position, click)

    fpsClock.tick(FPS)
    pygame.display.update()
import random, pygame, sys,number,TableAI
from itertools import combinations
pygame.init()

# Lưu ý nhớ chuyển 10 thành T
cards = [""] * 7
number = [0] * 7  # Số của lá bài(2,3,4, ... J, Q, K, A)
suit = [""] * 7  # Chất của lá bài
freqNum = [0] * 13  # Đếm số lần xuất hiện của mỗi số
freqSuit = [0] * 4  # Đếm số lần xuất hiện của mỗi chất
freqCouple = [0] * 4  # Đếm số bộ(ở vị trí 1 là số bộ 2, ở vị trí 2 là số bộ 3, ở vị trí 3 là số bộ 4)


def setup_mang(each_player_cards):
    global cards,number,suit,freqNum,freqSuit,freqCouple
    cards=each_player_cards
    number = [0] * 7  # Số của lá bài(2,3,4, ... J, Q, K, A)
    suit = [""] * 7  # Chất của lá bài
    freqNum = [0] * 13  # Đếm số lần xuất hiện của mỗi số
    freqSuit = [0] * 4  # Đếm số lần xuất hiện của mỗi chất
    freqCouple = [0] * 4  # Đếm số bộ(ở vị trí 1 là số bộ 2, ở vị trí 2 là số bộ 3, ở vị trí 3 là số bộ 4)

    for i in range(0, 7):
        cards[i] = cards[i][0:6]  # Cắt ".png"
        clean = cards[i].split(" of ")  # Cắt số và chất
        # Chuyển kí tự thành số
        if (clean[0] == "T"):
            number[i] = 10
            freqNum[8] += 1
        elif (clean[0] == "J"):
            number[i] = 11
            freqNum[9] += 1
        elif (clean[0] == "Q"):
            number[i] = 12
            freqNum[10] += 1
        elif (clean[0] == "K"):
            number[i] = 13
            freqNum[11] += 1
        elif (clean[0] == "A"):
            number[i] = 14
            freqNum[12] += 1
        else:
            number[i] = int(clean[0])
            freqNum[int(clean[0]) - 2] += 1
        suit[i] = clean[1]

    for i in range(0, 7):
        if (suit[i] == "C"):
            freqSuit[0] += 1
        if (suit[i] == "D"):
            freqSuit[1] += 1
        if (suit[i] == "H"):
            freqSuit[2] += 1
        if (suit[i] == "S"):
            freqSuit[3] += 1

    for i in range(0, 13):
        if (freqNum[i] != 0):
            freqCouple[freqNum[i] - 1] += 1


def check_lien_tiep():  # Check coi 5 lá liên tiếp không(ko tính straight flush/ royal flush)
    global cards, number, suit, freqNum, freqSuit, freqCouple
    cnt = 0
    #global start
    #start = 2  # Số bắt đầu chuỗi liên tiếp(chuỗi 5 lá liên tiếp)
    for i in range(0, 13):
        if (freqNum[i] >= 1):
            #if (cnt == 0):
            cnt += 1
            if (cnt == 5):
                return True
        else:
            cnt = 0
    return False


def check_dong_chat():  # Check coi 5 lá có đồng chất không
    global cards, number, suit, freqNum, freqSuit, freqCouple
    for i in range(0, 4):
        if (freqSuit[i] >= 5):
            return True
    return False


def check_straightflush():  # Check coi có phải straight flush không
    global cards, number, suit, freqNum, freqSuit, freqCouple
    s = ""  # Chất mà có 5 lá
    cont = []  # Mảng chứa những số mà có chất s
    for i in range(0, 4):
        if (freqSuit[i] >= 5):
            if i == 0:
                s = "C"
                break
            if i == 1:
                s = "D"
                break
            if i == 2:
                s = "H"
                break
            if i == 3:
                s = "S"
                break
    if s == "":
        return False
    for i in range(0, 7):
        if (suit[i] == s):
            cont.append(number[i])

    # Check coi 5 lá có liên tiếp không
    cont.sort()
    if (len(cont) == 7):
        a = (cont[1] - cont[0] == 1) and (cont[2] - cont[1] == 1) and (cont[3] - cont[2] == 1) and (
                    cont[4] - cont[3] == 1)
        b = (cont[2] - cont[1] == 1) and (cont[3] - cont[2] == 1) and (cont[4] - cont[3] == 1) and (
                    cont[5] - cont[4] == 1)
        c = (cont[3] - cont[2] == 1) and (cont[4] - cont[3] == 1) and (cont[5] - cont[4] == 1) and (
                    cont[6] - cont[5] == 1)
        if (a or b or c):
            return True
        else:
            return False
    if (len(cont) == 6):
        a = (cont[1] - cont[0] == 1) and (cont[2] - cont[1] == 1) and (cont[3] - cont[2] == 1) and (
                    cont[4] - cont[3] == 1)
        b = (cont[2] - cont[1] == 1) and (cont[3] - cont[2] == 1) and (cont[4] - cont[3] == 1) and (
                    cont[5] - cont[4] == 1)
        if (a or b):
            return True
        else:
            return False
    if (len(cont) == 5):
        a = (cont[1] - cont[0] == 1) and (cont[2] - cont[1] == 1) and (cont[3] - cont[2] == 1) and (
                    cont[4] - cont[3] == 1)
        if (a):
            return True
        else:
            return False


def check_royalflush():
    global cards, number, suit, freqNum, freqSuit, freqCouple
    s = ""
    cont = []
    for i in range(0, 4):
        if (freqSuit[i] >= 5):
            if i == 0:
                s = "C"
                break
            if i == 1:
                s = "D"
                break
            if i == 2:
                s = "H"
                break
            if i == 3:
                s = "S"
                break
    if s == "":
        return False

    for i in range(0, 7):
        if (suit[i] == s):
            cont.append(number[i])
    cont.sort()
    if (cont[0] == 10 and cont[1] == 11 and cont[2] == 12 and cont[3] == 13 and cont[4] == 14):
        return True
    else:
        return False


def ranking_cards():
    global cards, number, suit, freqNum, freqSuit, freqCouple
    if (check_royalflush()):
        return "Royal Flush"
    if (check_straightflush()):
        return "Straight Flush"
    if (freqCouple[3] >= 1):
        return "Quads"
    if (freqCouple[1] >= 1 and freqCouple[2] >= 1):
        return "Full House"
    if (check_dong_chat()):
        return "Flush"
    if (check_lien_tiep()):
        return "Straight"
    if (freqCouple[2] >= 1):
        return "Three"
    if (freqCouple[1] >= 2):
        return "Two Pair"
    if (freqCouple[1] >= 1):
        return "Pair"
    return "High Card"


'''setup_mang()
print(number)
print(suit)
print(freqNum)
print(freqSuit)
print(check_lien_tiep())
print(start)
print(check_dong_chat())
print(freqCouple)
print(ranking_cards())'''













'''def RoyalFlush(array):
    with open('reso.py', 'w') as f:
        comb = combinations([1,2,3,4,5,6,7], 5)
        for i in list(comb):
            place=i
            newarray=[]
            for j in place:
                newarray.append(array[j-1])

            for k in range(5):
                res = str(newarray[k])
                f.write(res + " ")
            f.write("\n")

    comb = combinations([1, 2, 3, 4, 5, 6, 7], 5)
    for i in list(comb):
        place = i
        newarray = []
        for j in place:
            newarray.append(array[j - 1])



def StraightFlush():
    pass

def FourofaKind():
    pass

def FxullHouse():
    pass

def Flush():
    pass

def Straight():
    pass

def ThreeofaKind():
    pass

def TwoPairs():
    pass

def Pair():
    pass

def HighCard():
    pass
'''
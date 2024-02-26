#Lưu ý: Đếm từ 1

#Những biến không thay đổi sau mỗi trận đấu
mem = 6 #số người chơi
blindMoney = 5 #số tiền đặt cược tối thiểu của bàn chơi
match = 1 #Số thứ tự trận
dealer = 1 #Mặc định vị trí dealer ban đầu là 1
exit = False

while(not exit):
    #Khởi tạo biến từng trận
    turn = dealer; # vị trí hành động
    round = 1; # số vòng
    isBet = False; # đã có người đặt cược trước đó chưa
    betDone = False; # vòng đó đã đặt cược xong chưa

    #Tạo mảng chỉ số tiền cược của mỗi người chơi, có n phần tử, mỗi phần tử ban đầu bằng 0
    listBet = []
    i = mem
    while i >= 1:
	    listBet.append(0)
	    i -= 1
	    
    #Animation: đặt dealer trước mặt người có vị trí là biến dealer
    
    #Di chuyển qua SB để SB đặt cược
    turn += 1
    SBindex = turn #vị trí của SB
    isBet = True
    listBet[turn - 1] = blindMoney
    
    #Animation: Đặt SB trước mặt người có vị trí là biến SBindex

    #Di chuyển qua BB để BB đặt cược
    turn += 1
    BBindex = turn
    listBet[turn - 1] = 2 * blindMoney
    
    #Animation: Đặt BB trước mặt người có vị trí là biến BBindex
    
    #Animation: Chia 2 lá bài tẩy

    #Hàm check coi tất cả phần tử trong mảng có bằng nhau và tất cả phần tử có lớn hơn 0 ko
    def checkBetDone():
        mini = 100
        maxi = -1
    
        for element in listBet:
    	    if(element != 0 and element != -1):
    		    mini = min(mini, element)
    		    maxi = max(maxi, element)
        if(mini == maxi):
    	    betDone = True
        else: 
    	    betDone = False
        return betDone
            
    while(round <= 3):
        #Check xem vòng này không phải vòng preflop phải không
        if round != 1: 
    	    isBet = False
    	    betDone = False
    	    cnt = 0
            #Tìm vị trí bắt đầu hành động các vòng sau(tính từ SB trở đi)
    	    for x in range(SBindex - 1, len(listBet)):
    		    cnt += 1
    		    if(listBet[x] >= 0):
    			    turn = x - 1
    			    break
    	    if(cnt == (len(listBet) - SBindex + 1)):
    		    for x in range(0, SBindex - 1):
    			    if(listBet[x] >= 0):
    				    turn = x - 1
        while(not checkbetDone()):
            turn += 1
    	    if(isBet):
    		    if(Fold()):
    			    #Animation: Fold
                    listBet[turn - 1] = -1
                if(Call()):
    			    #Animation: Call
                if(Raise()):
    			    #Animation: Raise
    		    if(Allin()):
    			    while(not checkbetDone()):
    				    i = i + 1
    			    
    	    else:
                if(Fold()):
    			    #Animation: Fold
                    listBet[turn - 1] = -1
                if(Bet()):
    			    #Animation: Bet
                if(Check()):
    			    #Animation: Check
                if(Raise()):
    			    #Animation: Raise
    		    if(Allin()):
    			    while(not checkbetDone()):
    				    i = i + 1
        
    	#Animation: Thu tiền đặt cược vào pot() 
    	if(round == 1):
    		#Show 3 lá Flop()
    		round += 1
    	elif(round == 2):
    		#Show 1 lá Turn()
    		round += 1
    	elif(round == 3):
    		#Show 1 lá River()
    		#So sánh các lá bài với nhau()
    		#Chia tiền pot
            round += 1
    dealer += 1
    match += 1

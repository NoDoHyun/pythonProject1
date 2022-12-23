import random

def menu2(cost,turn,turn2):

    money3=0 #주문총액
    menudic={1:18000,2:19000,3:19000,4:17000,5:18000,6:18000,7:8000,8:15000,9:5000,10:7000,
          11:12000,12:5000,13:4000,14:4500,15:4500,16:2500,17:2000,18:1000,19:7000,20:7000}
    menudic2={1:"후라이드 치킨",2:"양념치킨",3:"간장치킨",4:"후라이드 순살",5:"양념치킨 순살",6:"간장치킨 순살",7:
              "마른오징어",8:"과일안주",9:"포테이토 후라이",10:"쥐포",11:"모둠튀김",12:"테라",13:"카스",14:"오비라거",
              15:"클라우드",16:"콜라",17:"사이다",18:"쿨피스",19:"오뎅탕",20:"떡볶이"}
    for k in range(1,cost+1):
        print("%d주차 %d일 손님 %d번"%(turn,turn2,k))
        money2=0 #인당총액
        black=random.randrange(1, 101)#블랙컨슈머 할당
        select2 = random.randrange(1, 6)#메뉴갯수
        print("손님수",cost)
        f=open("C:/pythonProject/pythonProject/pythonProject/total.txt",'a')
        if (black<=15):
            f.write("%d주차 %d일 손님 %d번\n" % (turn, turn2, k))
        for l in range(1,select2+1):
            select = random.randrange(1, 21)  # 메뉴번호
            money2+=menudic[select]
            print(menudic2[select],"구매",menudic[select],"원")
            if(black<=15):
                f.write(str(menudic2[select]))
                f.write(":")
                f.write(str(menudic[select]))
                f.write("\n")
        if black<=15:
            money3+=money2*-2

            print("클레임! %d원 환불"% (money2*2))
            f.write("클레임! %d원 환불\n\n"% (money2*2))
        if black>15:
            money3+=money2
            print("총 %d 원 결제완료"% money2)
            # f.write("총 %d 원 결제완료\n\n"% money2)
        f.close()
        print("현재 총액:",money3)
        print("\n")
    return money3

def work(arbeit,turn,turn2):
    cost=0
    if arbeit==0:
        cost+=random.randrange(1, 101)
    if arbeit>=1:
        cost+=random.randrange(1, 101)*arbeit
    return menu2(cost,turn,turn2)

def menu():
    print("1 후라이드 치킨 18000",end=' ')
    print("2 양념치킨 19000",end=' ')
    print("3 간장치킨 19000",end=' ')
    print("4 후라이드 순살 17000")
    print("5 양념치킨 순살 18000",end=' ')
    print("6 간장치킨 순살 18000",end=' ')
    print("7 마른오징어 8000",end=' ')
    print("8 과일안주 15000")
    print("9 포테이프 후라이 5000",end=' ')
    print("10 쥐표 7000",end=' ')
    print("11 모듬튀김 12000",end=' ')
    print("12 테라 5000")
    print("13 카스 4000",end=' ')
    print("14 오비라거 4500",end=' ')
    print("15 클라우드 4500",end=' ')
    print("16 콜라 2500")
    print("17 사이다 2000",end=' ')
    print("18 쿨피스 1000",end=' ')
    print("19 오뎅탕 7000",end=' ')
    print("20 떡볶이 7000")

money=0
turn=1
arbeit=0
while(1):
    if(turn>4):
        break
    money-=1500000*arbeit    #주 시작시 알바 선불
    print("현재 금액:\n",money)
    print("%d주차\n"%turn)
    select=(int(input("1.메뉴판,2.알바고용,3.영업시작\n")))
    if(select==1):
        menu()
        turn-=1
        money += 1500000 * arbeit  #주 시작시 알바 수만큼 돈 빠지기때문에 방지
    if(select==2):
        if(turn>1 and money>=1500000):
            arbeit+=1
            money-=1500000      #고용주 알바 선불
            money += 1500000 * arbeit  # 주 시작시 알바 수만큼 돈 빠지기때문에 방지
            turn-=1
            print("알바%d명\n"%arbeit)
        else:
            print("알바고용불가")
            money += 1500000 * arbeit  # 주 시작시 알바 수만큼 돈 빠지기때문에 방지
            turn-=1
    if(select==3):
        print("영업시작")
        for j in range (1,8):
            turn2=j
            money+=work(arbeit,turn,turn2)
            print(money)
    # else:
    #     turn-=1
    #     money += 1500000 * arbeit
    turn+=1


if money>=500000000:
    print("해피엔딩")
else:
    print("베드엔딩")

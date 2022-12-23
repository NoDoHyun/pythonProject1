def menu2(cost):
    print("계산자리2")
def work(alba):
    print("계산1")
def menu():
    print("메뉴자리")

money=0
turn=1
alba=0
while(1):
    if(turn>4):
        break
    print("현재 금액:\n",money)
    print("%d주차\n"%turn)
    select=(int(input("1.메뉴판,2.알바고용,3.영업시작\n")))
    if(select==1):
        menu()
    if(select==2):
        if(turn>1 and money>=1500000):
            alba+=1
    if(select==3):
        print("영업시작")
        for j in range (1,8):
            money+=work(alba)
            print(money)
    turn+=1

if money>=500000000:
    print("해피엔딩")
else:
    print("베드엔딩")

cocoa=800
yuza=1200
coffee=500
cocoanum=0
yuzanum=0
coffeenum=0
money=0
spin=0
while(1):
    select = (int(input("1,돈투입,2.최대경우의수,3.물건선택,4.계산,5.잔돈반환\n")))
    if(select==1):
        money+=int(input("금액입력\n"))
    if(select==2):
        spin=money/cocoa
        for i in range(0,int(spin)):
            money2=money
            money2-=cocoa*i
            spin2=money2/cocoa
            for j in range(0,int(spin2)):
                money3=money2
                turn=0
                money3-=yuza*j
                spin3=money2/yuza
                if(money3>0):
                    for k in range(0,int(spin3)):
                            spin4=money3/coffee
                            if(turn==0):
                                if(spin4>0):
                                    turn+=1
                                    print("최대 경우의 수:코코아%d,유자%d,커피%d"%(i,j,spin4))
                                if(spin4<=0):
                                    print("최대 경우의 수:코코아%d,유자%d,커피0" % (i, j))
    if(select==3):
        select2=int(input("물건선택:1.코코아, 2.유자, 3.커피\n"))
        if(select2==1):
            print("코코아 선택\n")
            cocoanum+=1
        if(select2==2):
            print("유자\n")
            yuzanum+=1
        if(select2==3):
            print("커피\n")
            coffeenum+=1
    if(select==4):
        print("계산\n")
        money-=(cocoa*cocoanum)+(yuza*yuzanum)+(coffee*coffeenum)
        print("남은돈%d\n"%money)
    if(select==5):
        print("잔돈반환:%d\n"%money)
        money=0

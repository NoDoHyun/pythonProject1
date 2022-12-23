import random

def arbeitnum(money):           #인자는 호출때 사용한 인자랑 이름달라도 자리만 맞으면 작동합니다            # 도현
    if(money>=1500000):
        arbeit1=money/1500000   #고용가능한 알바수 구하기,메인의 진짜 arbeit과 혼동 피하기 위해 1 붙임
        while(1):
            print("%d명 고용가능"%arbeit1)
            select=(int(input("고용할 알바수 : ")))
            if(select<=arbeit1):
                return select       #고용가능수와 선택수가 같을경우 그만큼 리턴
            else:
                print("그만큼 고용하기엔 돈이 부족합니다")
    else:
        print("돈부족, 고용불가")


def claim(menu_price_claim):                                            # 4 성경누나

    claim_price=[]
    claim_price_sum = 0
    for i in range(len(menu_price_claim)):

        rand = random.randrange(100)

        if rand < 15:
            claim_price.append(menu_price_claim[i]*2)
            claim_price_sum = sum(claim_price)
    print(f'클레임 환불 금액은 {claim_price_sum}원 입니다.')

    return claim_price_sum


def finish(total_money):                                                 # 6 성경누나

    if total_money >= 500000000:
        print("프랜차이즈화~")

    else :
        print("GAME OVER")


def day(arbeit):
    day_menu = []   # 하루방문 손님 리스트
    day_money = []  # 손님 매출 총합
    day_total = []  # 하루 매출 총합
    day_sum = 0     # 하루 매출 총합
    menu_list= ['후라이드치킨','양념치킨','간장치킨','후라이드순살','양념치킨순살','간장치킨순살','마른오징어','과일안주','포테이토후라이','쥐포','모듬튀김','테라','카스','오비라거','클라우드','콜라','사이다','쿨피스','오뎅탕','떡볶이']
    menu_price = [18000,19000,19000,17000,18000,18000,8000,15000,5000,7000,12000,5000,4000,4500,4500,2500,2000,1000,7000,7000]
    customer= random.randrange(100)
    n = customer+100*arbeit
    for i in range(n): # 1~5개 메뉴 선택
        for j in range(random.randrange(1,6)):
            menu_choice = random.randrange(20)
            day_money.append(menu_price[menu_choice])
            day_menu.append(menu_list[menu_choice]) # 손님이 선택한 메뉴 저장
        print(f'주문하신 음식은 {day_menu}입니다.')
        print(f'{sum(day_money)}원 입니다')
        day_total.append(sum(day_money))
        day_menu.clear()
        day_money.clear()  # 다음손님 합을 초기화
        youtube(n)
    day_sum = sum(day_total)
    return day_sum, day_total

def youtube(n):
    youtuber = random.randrange(100)
    if youtuber == 0:
        print("*********유투버 등장*********")
        taste = random.randrange(2)
        if taste == 0:
            print(f'유튜버가 먹방에서 맛있다고 함')
            n = round(n + n*0.5)
            print(f'{n} 손님 증가')
        else:
            print(f'유튜버가 먹방에서 맛없다고 함')
            n = round(n - n*0.5)
            print(f'{n} 손님 감소')
    return n


def incentive(i, day_sum): # 인센티브
    if i == 1:
        if day_sum>10000000:
            a=random.randrange(10)
            print (f'{a}% 인센티브 발생')
            return round(day_sum*0.01*a)

    if i == 2:
        if day_sum > 100000000:
            a=random.randrange(10)
            print (f'{a}% 인센티브 발생')
            return round(day_sum*0.01*a)

    if i == 3:
        if day_sum > 300000000:
            a = random.randrange(10)
            print (f'{a}% 인센티브 발생')
            return round(day_sum*0.01*a)

def tax(menu_price_claim):
    cash = 0 #현금 사용자 수
    card = 0 #카드 사용자 수
    tax_e = 0 #탈세액

    for i in range(len(menu_price_claim)):
        rand = random.randrange(2)
        if rand == 0:
            cash += 1
            temp=menu_price_claim[i] * 0.1
            tax_e += int(temp)
        else :
            card += 1
    return cash, card, tax_e

def back_total(tax_e):
    back = 0
    rand = random.randrange(3)
    if rand == 0 :
        back = tax_e * 10
        print(f'탈세걸림! 10배로 {back}원 토해냅니다 ')
    return back

def roto():
    num=[]
    win=0

    print("1~20 원하는 번호 5개 입력")
    for i in range(0,5):
        num.append(int(input()))
    print("내 번호",num)

    while(1):
        rotonum1 = []
        for j in range(0,5):
            rotonum1.append((random.randrange(1, 20)))
        if len(rotonum1) == len(set(rotonum1)):
            break
        else:
            continue

    for k in rotonum1:
        for l in num:
            if(k==l):
                win+=1

    print("정답 번호",rotonum1)
    print("맞춘수:",win)
    return win

########################## main 함수 시작

arbeit = 0
total_money = 0
tax_e = 0

for i in range(4):                                      # 4주 반복문
    if i != 0:
        arbeit += arbeitnum(total_money)               # 아르바이트 고용 함수
        total_money -= arbeit*1500000

    for j in range(7):                                  # 7일 반복문
        print(f'{i+1}주차 {j+1}일/////')
        day_total_money, claim_list = day(arbeit)       # 1일 매출 함수
        total_money += day_total_money                  # 1일 총매출액을 total_money에 더함
        print(f'하루 매출액 : {day_total_money}원')

        cash, card, tax_e = tax(claim_list)             # 탈세 함수
        print(f'현금 {cash}명, 카드 {card}명 결제')
        tax_e += tax_e
        print(f'총 탈세액 : {tax_e}원')

        back = back_total(tax_e)
        total_money -= back
        print(f'총 금액 : {total_money}')

        # print(claim_list)
        claim_money = claim(claim_list)                 # 1일 클레임 함수
        total_money -= claim_money                      # total_money에서 클레임 비용 빼기
        print("")
        print(f'총 금액 : {total_money}')

    if i != 0:
        incen = incentive(i, total_money)               # 인센티브 지급 함수
        print(f'알바생에게 인센티브 {incen}원 지급')
        total_money -= incen
        print(f'총 금액 : {total_money}')

    count = roto()                                     # 로또 맞춘 개수 * 500만원
    print(f'5개 중 {count}개 맞췄음. 상금 {5000000*count}원')
    total_money += 5000000*count
    print(f'총 금액 : {total_money}')

finish(total_money)                                      # 매출액 비교 함수

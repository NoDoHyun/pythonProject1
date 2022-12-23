import os
from time import sleep

def mol():

    print("                   ,.,..\n")
    print("                  . ,~:-  ...\n")
    print("                  .:    - ::.:,  -\n")
    print("                   .   .-    ..     \n")
    print("                  .::,     . ::~:,\n")
    print("                  .  .     ::  :..,\n")
    print("                 .,,,::~  -    .:---\n")
    print("                   --,,       ,  .-\n")
    print("                  .:,.~   ,    ~~:,.\n")
    print("                  ....          ,\n")
    print("                     ~.         \n")
    print("            -:.                  ~\n")
    print("             . ~\n")
    print("     :~~     -  -:\n")
    print("     :  --   ~   ::\n")
    print("     ~    --  ,-,,:\n")
    print("      ,   .,: ::- ...,        ..\n")
    print("      ~    .::~-,:    -:.      .\n")
    print("       :::,  :          .       .\n")
    print("                          .:\n")
    print("     .                      ~       .\n")
    print("   ,,        ,         -     :.     .\n")
    print("  -         .,         .     :\n")
    print("  ,          ~ -               -\n")
    print("  -         : , -       ,:-    -.\n")
    print(" ,        .: :-, -      .~,     -\n")
    print(" .        .  :~  -.~::,~:    - .\n")
    print(" .      :~.  :,~       , ,.: ,,   .\n")
    print(" ,     -:. ~ ..~   ,:..   ..  .- :::i\n")
    print(" .      -.~  ,.               .- ..-~-\n")
    print(" ,      -  --                   -   : -\n")
    print(" ~     .-,  .                  -   .\n")
    print("-     .~~~,,                  .-   : .\n")
    print(", .   .  :: ~,....      .....:~    \n")
    print(",, ,  ~:: . -,-:::~.      \n")
    print("  .  .~.     :..   .:  -,   .     ,  .\n")
    print("    :-              :  -:-  .  ,~:, ..,\n")
    print("       -             ,.~.~.,~   -     .\n")
    print("       ~-   -         ,..,:~   .-\n")


def menu():

    print("1.콜라:1200원\n2.우주맛 콜라:1900원\n3.제로콜라:1200원\n4.스프라이트:1100원\n5.환타:900원\n6.닥터페퍼:1100원\n7.몬스터:1800원\n8.파워에이드:1900원\n9.네스티:1600원\n")
    print("10.글라소 비타민 워터:2100\n11.미닛메이드:1700원\n12:조지아 커피:900원\n13.암바사:900원\n14.마테차:1700\n")

def pay():

    money=0
    select2=0
    print("주문할 음료 번호 입력\n")
    select2=int(input())

    if(select2==1):
        print("콜라선택,1200원\n")
        money+=1200
        return money

    if (select2 == 2):
        print("우주맛콜라선택,1900원\n")
        money+=1900
        return money

    if (select2 == 3):
        print("제로콜라선택,1200원\n")
        money+=1200
        return money

    if (select2 == 4):
        print("스프라이트선택,1200원\n")
        money+=1100
        return money

    if (select2 == 5):
        print("환타선택,900원\n")
        money+=900
        return money

    if (select2 == 6):
        print("닥터페퍼선택,1100원\n")
        money+=1100
        return money

    if (select2 == 7):
        print("몬스터선택,1800원\n")
        money+=1800
        return money

    if (select2 == 8):
        print("파워에이드선택,1900원\n")
        money+=1900
        return money

    if (select2 == 9):
        print("네스티선택,1600원\n")
        money+=1600
        return money

    if (select2 ==10):
        print("글라소 비타민 워터선택,2100원\n")
        money+=2100
        return money

    if (select2 == 11):
        print("미닛메이드선택,1700원\n")
        money+=1700
        return money

    if (select2 == 12):
        print("조지아선택,900원\n")
        money+=900
        return money

    if (select2 == 13):
        print("암바사선택,900원\n")
        money+=900
        return money

    if (select2 == 14):
        print("마테차선택,1700원\n")
        money+=1700
        return money

i=0
money=0
paymon=0
while(1):
    print("1.메뉴보기, 2.돈 투입, 3.음료 선택, s.결제 x.종료\n")
    select=(input())

    if(select=="1"):
        menu()

    if(select=="2"):
        print("투입할 돈:\n")
        money=int(input())
        print("%d원 충전 완료\n" %money)

    if(select=="3"):
        paymon+=pay()
        print("누적금액:%d\n" %paymon)

    if(select=="s"):
        if(money-paymon>=0):
            while(i<3):
                os.system('cls')
                sleep(1)
                mol()
                sleep(1)
                os.system('cls')
                i+=1
            print("%d원 결제, 잔액:%d원" %(paymon, money-paymon))
            break
        else:
            print("잔액부족\n")
            break
    if(select=="x"):
        print("종료\n")
        break
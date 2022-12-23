import random
from time import sleep
def inc(si):
    inc=random.randrange(50, 2501)
    print("증가폭%d\n" %inc)
    si+=inc
    return si


i=0
si2=0
spin=0
gudok=0
div=0
chan=input()
print("채널명 입력:%s\n" %chan)

while(i<20):
    si=0
    si2=0
    print("오늘의 컨텐츠 입력\n")
    con=input()
    print("방송 송출~!\n")

    while(spin<10):
        print("%s오늘의 컨텐츠:%s\n" %(chan, con))
        si2+=inc(si)
        print("%d\n" %si2)
        spin+=1
        # sleep(1)

    div=random.randrange(1, 5)
    gudok+=si2/div
    print("구독자수: %d\n" %gudok)
    si=0
    spin=0
    i += 1

if(gudok>=100000):
    print("실버버튼!")

else:
    print("10만구독 실패, 유튜브 폭파!")

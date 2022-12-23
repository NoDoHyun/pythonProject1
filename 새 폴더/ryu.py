import random
import time
def mi():
    a = random.randrange(1, 5)
    return a
def add():
    b = random.randrange(1, 5)
    return b

ryua = 0
ryub = 0
spin2 = 0
turn = 0
add1 = 0
mi1 = 0
rand1 = 0
count1 = 0
coun2 = 0
spin = 0
add1 = 0
add1 += add()
ryua += add1
ryub += add1
turn +=1
print("물고기 이름 입력\n")
ryu1=input()
ryu2=input()
print("1턴\n")
print("%s:%d, %s:%d\n" %(ryu1, ryua, ryu2, ryub))

while (ryua < 500):

    turn +=1
    print("%d턴\n" %turn)
    spin2 = 0
    spin2 += ryua
    while (spin < spin2):
        add1=add()
        ryua += add1
        ryub += add1
        count1 += add1
        spin+=1
        if (ryua >= 500):
            break
            time.sleep(1)

    print("태어난 물고기%d쌍\n" %count1)
    count1 = 0
    if (ryua >= 500):
        print("%s:%d, %s:%d\n" %(ryu1, ryua, ryu2, ryub))
        print("브레이크!")
        break

    mi1 = mi()
    if (ryua - mi1 > 0):
        ryua -= mi1
        ryub -= mi1
        print("죽은물고기%d쌍\n" %mi1)

    else:
        print("대멸종")
        print("%s:%d, %s:%d\n" %(ryu1, ryua, ryu2, ryub))




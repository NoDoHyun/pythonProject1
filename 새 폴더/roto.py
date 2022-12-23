import random
def roto():
    num=[]
    win=0

    print("1~20원하는 번호 5개 입력")
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

select=int(input())
if (select==1):
    roto()
import random
def smode():
    num=0
    pai=0
    kko=0
    pika=0
    meta=0
    num5=0
    meta2=0
    trash=0
    while(num5<10):

        print("뽑기=아무숫자")
        trash=int(input())
        num=random.randrange(1, 101)
        if(num<=25):

            print("파이리\n")
            pai+=1

        if(26<=num and num<=50):

            print("꼬부기\n")
            kko+=1

        if(51<=num and num<=75):

            print("피카츄\n")
            pika+=1

        else:
            print("메타몽\n")
            meta+=1

        num5+=1

    print("파이리%d, 꼬부기%d, 피카츄%d, 메타몽%d \n", pai, kko, pika, meta)
    num5=0
    meta2=meta
    meta=0
    while(num5<meta2):

        num=random.randrange(0, 3)
        if(num==0):
            pai+=1
        if(num==1):
            kko+=1
        if(num==2):
            meta+=1
        if (num >= 76):
            pika+=1
        num5+=1

    print("메타몬 변신후 갯수=파이리%d, 꼬부기%d, 피카츄%d, 메타몽%d", pai, kko, pika, meta)



def amode():

    num=0
    pai=0
    kko=0
    pika=0
    meta=0
    meta2=0
    num5=0
    while(num5<100):

        num=random.randrange(1, 101)
        if(num<=25):
            pai+=1
        if(26<=num and num<=50):
            kko+=1
        if(51<=num and num<=75):
            pika+=1
        if(num>=76):
            meta+=1
        num5+=1

    print("파이리%d, 꼬부기%d, 피카츄%d, 메타몽%d \n", pai, kko, pika, meta)
    num5=0
    meta2=meta
    meta=0
    while(num5<meta2):

        num=random.randrange(0, 3)
        if(num==0):
            pai+=1
        if(num==1):
            kko+=1
        if(num==2):
            meta+=1
        else:
            pika+=1
        num5+=1

    print("메타몬 변신후 갯수=파이리%d, 꼬부기%d, 피카츄%d, 메타몽%d", pai, kko, pika, meta)


select=0
print("자동모드:1, 수동모드:2")
select=int(input())
if(select==1):
    amode()
if(select==2):
    smode()


import random
def smode():

    trash = 0
    sung = 0
    jae = 0
    win1 = 0
    win2 = 0

    team = random.randrange(0, 2)

    while (sung < 10 and jae < 10):

        rock = random.randrange(0, 3)
        if (team == 0):
            print("재일-연재, 성일-의용\n")
            trash = int(input())

            if (rock == 0):
                print("연재 승, 재일+\n")
                sung += 1

            if (rock == 1):
                print("의용 승, 성일+\n")
                jae += 1

            if (rock == 2):
                print("무승부\n")

            win1 = jae / (jae + sung) * 100
            win2 = sung / (jae + sung) * 100
            print("현재 승률 연재%f, 성일%f\n" % (win1, win2))

        if (team == 1):
            print("재일-의용, 성일-연재\n")
            trash = int(input())
            if (rock == 0):
                print("연재 승, 재일+\n")
                sung += 1

            if (rock == 1):
                print("의용 승, 성일+\n")
                jae += 1

            if (rock == 2):
                print("무승부\n")

            win1 = jae / (jae + sung) * 100
            win2 = sung / (jae + sung) * 100
            print("현재 승률 연재%f, 성일%f\n" % (win1, win2))

    print("총 승률=연재%f, 성일%f\n" % (win1, win2))
    if (jae > sung):
        print("연재 최종 승")
    else:
        print("성일 최종 승")

def amode():

    sung = 0
    jae = 0
    win1 = 0
    win2 = 0

    team = random.randrange(0,2)

    while (sung < 10 and jae < 10):

        rock = random.randrange(0, 3)
        if (team == 0):
            print("재일-연재, 성일-의용\n")

            if (rock == 0):
                print("연재 승, 재일+\n")
                sung+=1

            if (rock == 1):
                print("의용 승, 성일+\n")
                jae+=1

            if (rock == 2):
                print("무승부\n")

            win1=jae / (jae+sung) * 100
            win2=sung / (jae+sung) * 100
            print("현재 승률 연재%f, 성일%f\n" %(win1, win2))

        if (team == 1):
            print("재일-의용, 성일-연재\n")
            if (rock == 0):
                print("연재 승, 재일+\n")
                sung+=1

            if (rock == 1):
                print("의용 승, 성일+\n")
                jae+=1

            if (rock == 2):
                print("무승부\n")

            win1=jae / (jae+sung) * 100
            win2=sung / (jae+sung) * 100
            print("현재 승률 연재%f, 성일%f\n" %(win1, win2))

    print("총 승률=연재%f, 성일%f\n" %(win1, win2))
    if (jae > sung):
        print("연재 최종 승")
    else:
        print("성일 최종 승")



print("자동1, 수동2")
select=int(input())
if (select == 1):
    print("자동모드")
    amode()
if (select == 2):
    smode()


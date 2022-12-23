import random

def match(FA,T):
    s=[]                                                               #16강 대진표를 만드는데 사용하는 함수
    num = [1, 2, 3, 4]                                                  #1234를 부여하며 1등은 2등이 될수 없기에 1등을 DEL로 지워버리며 출력,반복
    for i in num:
        num2 = [1, 2, 3, 4]
        if (FA[0] == i):
            s.append(T[i - 1])
            s.append(FA[1])
            del num2[i-1]
            for j in num2:
                if(FA[2]==j):
                    s.append(T[j-1])
                    s.append(FA[3])
    return s

def ematch(A,B):
    team1=0                                                             #16강이후부터 사용하는 토너먼트함수,비교해서 이긴쪽을 리턴
    team2=0
    aa=str(A)
    bb=str(B)
    while(1):
        win = random.randrange(1, 101)
        if ('1' in aa):
            team1 = random.randrange(1, 71)
        if ('2' in aa):
            team1 = random.randrange(1, 61)
        if ('3' in aa):
            team1 = random.randrange(1, 41)
        if ('4' in aa):
            team1 = random.randrange(1, 21)

        if ('1' in bb):
            team2 = random.randrange(1, 71)
        if ('2' in bb):
            team2 = random.randrange(1, 61)
        if ('3' in bb):
            team2 = random.randrange(1, 41)
        if ('4' in bb):
            team2 = random.randrange(1, 21)

        if (win <= team1 and win > team2):
            return [A]
        if (win > team1 and win <= team2):
            return [B]
        else:
            continue

def fmatch():
    team1=0
    team2=0
    team3=0
    team4=0
    goal1=0
    goal2=0
    goal3=0
    goal4=0
    for i in range(1,5):
        A=[" "," "," "," "," "]                                                                             #i값을 증가시켜가며 1,2,3,4팀의 승점을 구한다 승+3 무승부 각팀+1
        if(i==1):
            while(1):
                A[1] = random.randrange(1, 71)                                                              #시드별 승률 고정,절대범위와 비교해서 둘다 절대범위보다 크면 무승부, 한쪽만크면 그팀의 승리
                A[2] = random.randrange(1, 61)
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                goal1 += random.randrange(0, 4)
                goal2 += random.randrange(0, 4)
                if (win<=A[i] and win<=A[i+1]):
                    team1+=1
                    team2+=1
                    goal1 = goal2
                    break
                if (win>A[i] and win>A[i+1]):
                    continue
                if (win<=A[i] and win>A[i+1]):
                    team1+=3
                    goal1 += goal2
                    break
                if (win>A[i] and win<=A[i+1]):
                    team2+=3
                    goal2 += goal1
                    break

        if(i==1):
            while (1):
                A[1] = random.randrange(1, 71)
                A[2] = random.randrange(1, 61)
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                goal1 += random.randrange(0,4)
                goal3 += random.randrange(0, 4)
                if (win <= A[i] and win <= A[i + 2]):
                    team1 += 1
                    team3 += 1
                    goal1=goal3
                    break
                if (win > A[i] and win > A[i + 2]):
                    continue
                if (win <= A[i] and win > A[i + 2]):
                    team1 += 3
                    goal1 += goal3
                    break
                if (win > A[i] and win <= A[i + 2]):
                    team3 += 3
                    goal3 += goal1
                    break

        if (i == 1):
            while (1):
                A[1] = random.randrange(1, 71)
                A[2] = random.randrange(1, 61)
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                goal1 += random.randrange(0, 4)
                goal4 += random.randrange(0, 4)
                if (win <= A[i] and win <= A[i + 3]):
                    team1 += 1
                    team4 += 1
                    goal1 = goal4
                    break
                if (win > A[i] and win > A[i + 3]):
                    continue
                if (win <= A[i] and win > A[i + 3]):
                    team1 += 3
                    goal1 += goal4
                    break
                if (win > A[i] and win <= A[i + 3]):
                    team4 += 3
                    goal4 += goal1
                    break

        if (i == 2):
            while (1):
                A[2] = random.randrange(1, 61)
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                goal2 += random.randrange(0, 4)
                goal3 += random.randrange(0, 4)
                if (win <= A[i] and win <= A[i + 1]):
                    team2 += 1
                    team3 += 1
                    goal2 =goal3
                    break
                if (win > A[i] and win > A[i + 1]):
                    continue
                if (win <= A[i] and win > A[i + 1]):
                    team2 += 3
                    goal2 += goal3
                    break
                if (win > A[i] and win <= A[i + 1]):
                    team3 += 3
                    goal2 += goal4
                    break

        if (i == 2):
            while(1):
                A[2] = random.randrange(1, 61)
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                goal2 += random.randrange(0, 4)
                goal4 += random.randrange(0, 4)
                if (win <= A[i] and win <= A[i + 2]):
                    team2 += 1
                    team4 += 1
                    goal2 = goal4
                    break
                if (win > A[i] and win > A[i + 2]):
                    continue
                if (win <= A[i] and win > A[i + 2]):
                    team2 += 3
                    goal2 += goal4
                    break
                if (win > A[i] and win <= A[i + 2]):
                    team4 += 3
                    goal4 += goal2
                    break

        if (i == 3):
            while (1):
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                goal3 += random.randrange(0, 4)
                goal4 += random.randrange(0, 4)
                if (win <= A[i] and win <= A[i + 1]):
                    team3 += 1
                    team4 += 1
                    goal3 = goal4
                    break
                if (win > A[i] and win > A[i + 1]):
                    continue
                if (win <= A[i] and win > A[i + 1]):
                    team3 += 3
                    goal3 += goal4
                    break
                if (win > A[i] and win <= A[i + 1]):
                    team4 += 3
                    goal4 += goal3
                    break

            print(team1,team2,team3,team4,"goal")
            while(team1==team2 or team1==team3 or team1==team4 or team2==team3 or team2==team4 or team3==team4):
                if(team1==team2 or team1==team3 or team1==team4):
                    if(goal1>goal2 or goal1>goal3 or goal1>goal4):
                        print("1팀골우세")
                        team1+=1                                                                                        #중복 구제용 식,높은시드승점감소
                    else:
                        print("타팀우세")
                        team1-=1
                if(team2==team3 or team2==team4):
                    if(goal2>goal3 or goal2>goal4):
                        print("1팀골우세")
                        team2+=1
                    else:
                        print("타팀우세")
                        team2-=1
                if(team3==team4):
                    if(goal3>goal4):
                        print("1팀골우세")
                        team3+=1
                    else:
                        print("타팀우세")
                        team3-=1

            if(team1>team2):
                if(team1>team3):
                    if(team1>team4):
                        last=[1,team1]
                        if(team4>team2):
                            last+=[4,team4]
                            return last                                                                             #1,2위를 알아내는 식
                        else:
                            if(team2>team3):
                                last+=[2,team2]
                                return last
                            else:
                                last+=[3,team3]
                                return last
                    else:
                        last=[4,team4]
                        last+=[1,team1]
                        return last
                else:
                    if(team3>team4):
                        last=[3,team3]
                        if(team4>team2):
                            last+=[4,team4]
                            return last
                        else:
                            last+=[2,team2]
                            return last
                    else:
                        last=[4,team4]
                        if(team3>team2):
                            last+=[3,team3]
                            return last
                        else:
                            last+=[2,team2]
                            return last
            else:
                if (team2 > team3):
                    if (team2 > team4):
                        last = [2, team2]
                        if (team4 > team1):
                            last += [4, team4]
                            return last
                        else:
                            if(team1>team3):
                                last += [1, team1]
                                return last
                            else:
                                last += [3, team3]
                                return last
                    else:
                        last = [4, team4]
                        last += [2, team2]
                        return last
                else:
                    if (team3 > team4):
                        last = [3, team3]
                        if (team4 > team1):
                            last += [4, team4]
                            return last
                        else:
                            if(team1>team2):
                                last += [1, team1]
                                return last
                            else:
                                last += [2, team2]
                                return last
                    else:
                        last = [4, team4]
                        if (team3 > team1):
                            last += [3, team3]
                            return last
                        else:
                            if(team1>team2):
                                last += [1, team1]
                                return last
                            else:
                                last += [2, team2]
                                return last

turn=0                                                                                                          #메인함수
while(1):
    AT=['1:네덜란드','2:세내갈','3:에콰도르','4:카타르']
    BT=['1:잉글랜드','2:웨일스','3:미국','4:이란']
    CT=['1:아르헨티나','2:사우디아라비아','3:멕시코','4:폴란드']
    DT=['1:프랑스','2:튀니지','3:덴마크','4:호주']
    ET=['1:스페인','2:독일','3:일본','4:코스타리카']
    FT=['1:벨기에','2:크로아티아','3:모로코','4:캐나다']
    GT=['1:스위스','2:세르비아','3:카메룬','4:스위스']
    HT=['1:포르투갈','2:우루과이','3:가나','4:대한민국']
    SIX=[]
    EIG=[]
    FOUR=[]
    TWO=[]
    ONE=[]
    W=""
    all=[AT,BT,CT,DT,ET,FT,GT,HT]

    for i in all:
        FA=fmatch()
        SIX+=(match(FA,i))

    print("16강:",SIX)
    AA=str(SIX[0])                                                                                              #16강부터 시드별 승률 추적을위해 리스트를 문자열로 받아 사용할 값을 받았다
    BB=str(SIX[2])

    for j in range(0,32,4):
        EIG+=ematch(SIX[j],SIX[j+2])
    print("8강",EIG)

    for k in range(0,8,2):
        FOUR += ematch(EIG[k], EIG[k + 1])
    print("4강",FOUR)

    for m in range(0,4,2):
        TWO += ematch(FOUR[m], FOUR[m + 1])
    print("결승",TWO)

    ONE += ematch(TWO[0], TWO[1])
    print("우승",ONE)
    spin = str(ONE)
    turn+=1

    if ('1' in spin):                                                                                        #특정팀이 이기면 멈추게 할수있음
        print(turn,"번째 평행세계")
        break
import random

def ematch(A,B):
    print(A,B)


def fmatch():
    team1=0
    team2=0
    team3=0
    team4=0
    o=0
    last=[]
    for i in range(1,5):
        A=[" "," "," "," "," "]
        if(i==1):
            while(1):
                A[1] = random.randrange(1, 71)
                A[2] = random.randrange(1, 61)
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                if (win<=A[i] and win<=A[i+1]):
                    print(A[i],A[i+1],win)
                    team1+=1
                    team2+=1
                    break
                if (win>A[i] and win>A[i+1]):
                    continue
                if (win<=A[i] and win>A[i+1]):
                    print(A[i], A[i+1], win)
                    team1+=3
                    break
                if (win>A[i] and win<=A[i+1]):
                    print(A[i], A[i+1], win)
                    team2+=3
                    break

        if(i==1):
            while (1):
                A[1] = random.randrange(1, 71)
                A[2] = random.randrange(1, 61)
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                if (win <= A[i] and win <= A[i + 2]):
                    print(A[i], A[i + 1], win)
                    team1 += 1
                    team3 += 1
                    break
                if (win > A[i] and win > A[i + 2]):
                    continue
                if (win <= A[i] and win > A[i + 2]):
                    print(A[i], A[i + 1], win)
                    team1 += 3
                    break
                if (win > A[i] and win <= A[i + 2]):
                    print(A[i], A[i + 1], win)
                    team3 += 3
                    break

        if (i == 1):
            while (1):
                A[1] = random.randrange(1, 71)
                A[2] = random.randrange(1, 61)
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                if (win <= A[i] and win <= A[i + 3]):
                    print(A[i], A[i + 1], win)
                    team1 += 1
                    team4 += 1
                    break
                if (win > A[i] and win > A[i + 3]):
                    continue
                if (win <= A[i] and win > A[i + 3]):
                    print(A[i], A[i + 1], win)
                    team1 += 3
                    break
                if (win > A[i] and win <= A[i + 3]):
                    print(A[i], A[i + 1], win)
                    team4 += 3
                    break

        if (i == 2):
            while (1):
                A[2] = random.randrange(1, 61)
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                if (win <= A[i] and win <= A[i + 1]):
                    print(A[i], A[i + 1], win)
                    team2 += 1
                    team3 += 1
                    break
                if (win > A[i] and win > A[i + 1]):
                    continue
                if (win <= A[i] and win > A[i + 1]):
                    print(A[i], A[i + 1], win)
                    team2 += 3
                    break
                if (win > A[i] and win <= A[i + 1]):
                    print(A[i], A[i + 1], win)
                    team3 += 3
                    break

        if (i == 2):
            while(1):
                A[2] = random.randrange(1, 61)
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                if (win <= A[i] and win <= A[i + 2]):
                    print(A[i], A[i + 2], win)
                    team2 += 1
                    team4 += 1
                    break
                if (win > A[i] and win > A[i + 2]):
                    continue
                if (win <= A[i] and win > A[i + 2]):
                    print(A[i], A[i + 2], win)
                    team2 += 3
                    break
                if (win > A[i] and win <= A[i + 2]):
                    print(A[i], A[i + 2], win)
                    team4 += 3
                    break

        if (i == 3):
            while (1):
                A[3] = random.randrange(1, 41)
                A[4] = random.randrange(1, 21)
                win = random.randrange(1, 101)
                if (win <= A[i] and win <= A[i + 1]):
                    print(A[i], A[i + 1], win)
                    team3 += 1
                    team4 += 1
                    break
                if (win > A[i] and win > A[i + 1]):
                    continue
                if (win <= A[i] and win > A[i + 1]):
                    print(A[i], A[i + 1], win)
                    team3 += 3
                    break
                if (win > A[i] and win <= A[i + 1]):
                    print(A[i], A[i + 1], win)
                    team4 += 3
                    break

            while(team1==team2 or team1==team3 or team1==team4 or team2==team3 or team2==team4 or team3==team4):
                if(team1==team2 or team1==team3 or team1==team4):
                    team1+=1
                if(team2==team3 or team2==team4):
                    team2+=1
                if(team3==team4):
                    team3+=1
            print("1팀%d 2팀%d 3팀%d 4팀%d" % (team1, team2, team3, team4))

            if(team1>team2):
                if(team1>team3):
                    if(team1>team4):
                        last=[1,team1]
                        if(team4>team2):
                            last+=[4,team4]
                            return last
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

AT=['1:카타르','2:에콰도르2','3:새내갈','4:네덜란드']
BT=['1:잉글랜드','2:이란','3:미국','4:웨일스']
CT=['1:아르헨티나','2:사우디아라비아','3:멕시코','4:폴란드']
DT=['1:덴마크','2:튀니지','3:프랑스','4:호주']
ET=['1:독일','2:일본','3:스페인','4:코스타리카']
FT=['1:모로코','2:크로아티아','3:벨기에','4:캐나다']
GT=['1:스위스','2:카메룬','3:브라질','4:세르비아']
HT=['1:포르투갈','2:대한민국','3:우루과이','4:가나']
SIX=[]

FA=fmatch()
if(FA[0]==1):
    SIX.append(AT[0])
    SIX.append(FA[1])
    if(FA[2]==2):
        SIX.append(AT[1])
        SIX.append(FA[3])
    if(FA[2] == 3):
        SIX.append(AT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(AT[3])
        SIX.append(FA[3])
if(FA[0]==2):
    SIX.append(AT[1])
    SIX.append(FA[1])
    if (FA[2] == 1):
        SIX.append(AT[0])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(AT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(AT[3])
        SIX.append(FA[3])
if(FA[0]==3):
    SIX.append(AT[2])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(AT[1])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(AT[0])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(AT[3])
        SIX.append(FA[3])
if(FA[0]==4):
    SIX.append(AT[3])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(AT[1])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(AT[2])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(AT[0])
        SIX.append(FA[3])


FA=fmatch()
if(FA[0]==1):
    SIX.append(BT[0])
    SIX.append(FA[1])
    if(FA[2]==2):
        SIX.append(BT[1])
        SIX.append(FA[3])
    if(FA[2] == 3):
        SIX.append(BT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(BT[3])
        SIX.append(FA[3])
if(FA[0]==2):
    SIX.append(BT[1])
    SIX.append(FA[1])
    if (FA[2] == 1):
        SIX.append(BT[0])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(BT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(BT[3])
        SIX.append(FA[3])
if(FA[0]==3):
    SIX.append(BT[2])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(BT[1])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(BT[0])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(BT[3])
        SIX.append(FA[3])
if(FA[0]==4):
    SIX.append(BT[3])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(BT[1])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(BT[2])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(BT[0])
        SIX.append(FA[3])

FA=fmatch()
if(FA[0]==1):
    SIX.append(CT[0])
    SIX.append(FA[1])
    if(FA[2]==2):
        SIX.append(CT[1])
        SIX.append(FA[3])
    if(FA[2] == 3):
        SIX.append(CT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(CT[3])
        SIX.append(FA[3])
if(FA[0]==2):
    SIX.append(CT[1])
    SIX.append(FA[1])
    if (FA[2] == 1):
        SIX.append(CT[0])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(CT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(CT[3])
        SIX.append(FA[3])
if(FA[0]==3):
    SIX.append(CT[2])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(CT[1])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(CT[0])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(CT[3])
        SIX.append(FA[3])
if(FA[0]==4):
    SIX.append(CT[3])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(CT[1])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(CT[2])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(CT[0])
        SIX.append(FA[3])

FA=fmatch()
if(FA[0]==1):
    SIX.append(DT[0])
    SIX.append(FA[1])
    if(FA[2]==2):
        SIX.append(DT[1])
        SIX.append(FA[3])
    if(FA[2] == 3):
        SIX.append(DT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(DT[3])
        SIX.append(FA[3])
if(FA[0]==2):
    SIX.append(DT[1])
    SIX.append(FA[1])
    if (FA[2] == 1):
        SIX.append(DT[0])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(DT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(DT[3])
        SIX.append(FA[3])
if(FA[0]==3):
    SIX.append(DT[2])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(DT[1])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(DT[0])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(DT[3])
        SIX.append(FA[3])
if(FA[0]==4):
    SIX.append(DT[3])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(DT[1])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(DT[2])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(DT[0])
        SIX.append(FA[3])

FA=fmatch()
if(FA[0]==1):
    SIX.append(AT[0])
    SIX.append(FA[1])
    if(FA[2]==2):
        SIX.append(ET[1])
        SIX.append(FA[3])
    if(FA[2] == 3):
        SIX.append(ET[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(ET[3])
        SIX.append(FA[3])
if(FA[0]==2):
    SIX.append(ET[1])
    SIX.append(FA[1])
    if (FA[2] == 1):
        SIX.append(ET[0])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(ET[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(ET[3])
        SIX.append(FA[3])
if(FA[0]==3):
    SIX.append(ET[2])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(ET[1])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(ET[0])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(ET[3])
        SIX.append(FA[3])
if(FA[0]==4):
    SIX.append(ET[3])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(ET[1])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(ET[2])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(ET[0])
        SIX.append(FA[3])

FA=fmatch()
if(FA[0]==1):
    SIX.append(AT[0])
    SIX.append(FA[1])
    if(FA[2]==2):
        SIX.append(FT[1])
        SIX.append(FA[3])
    if(FA[2] == 3):
        SIX.append(FT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(FT[3])
        SIX.append(FA[3])
if(FA[0]==2):
    SIX.append(FT[1])
    SIX.append(FA[1])
    if (FA[2] == 1):
        SIX.append(FT[0])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(FT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(FT[3])
        SIX.append(FA[3])
if(FA[0]==3):
    SIX.append(FT[2])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(FT[1])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(FT[0])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(FT[3])
        SIX.append(FA[3])
if(FA[0]==4):
    SIX.append(FT[3])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(FT[1])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(FT[2])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(FT[0])
        SIX.append(FA[3])

FA=fmatch()
if(FA[0]==1):
    SIX.append(FT[0])
    SIX.append(FA[1])
    if(FA[2]==2):
        SIX.append(FT[1])
        SIX.append(FA[3])
    if(FA[2] == 3):
        SIX.append(FT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(FT[3])
        SIX.append(FA[3])
if(FA[0]==2):
    SIX.append(FT[1])
    SIX.append(FA[1])
    if (FA[2] == 1):
        SIX.append(FT[0])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(FT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(FT[3])
        SIX.append(FA[3])
if(FA[0]==3):
    SIX.append(FT[2])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(FT[1])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(FT[0])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(FT[3])
        SIX.append(FA[3])
if(FA[0]==4):
    SIX.append(FT[3])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(FT[1])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(FT[2])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(FT[0])
        SIX.append(FA[3])

FA=fmatch()
if(FA[0]==1):
    SIX.append(AT[0])
    SIX.append(FA[1])
    if(FA[2]==2):
        SIX.append(GT[1])
        SIX.append(FA[3])
    if(FA[2] == 3):
        SIX.append(GT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(GT[3])
        SIX.append(FA[3])
if(FA[0]==2):
    SIX.append(GT[1])
    SIX.append(FA[1])
    if (FA[2] == 1):
        SIX.append(GT[0])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(GT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(GT[3])
        SIX.append(FA[3])
if(FA[0]==3):
    SIX.append(GT[2])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(GT[1])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(GT[0])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(GT[3])
        SIX.append(FA[3])
if(FA[0]==4):
    SIX.append(GT[3])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(GT[1])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(GT[2])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(GT[0])
        SIX.append(FA[3])

FA=fmatch()
if(FA[0]==1):
    SIX.append(HT[0])
    SIX.append(FA[1])
    if(FA[2]==2):
        SIX.append(HT[1])
        SIX.append(FA[3])
    if(FA[2] == 3):
        SIX.append(HT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(HT[3])
        SIX.append(FA[3])
if(FA[0]==2):
    SIX.append(HT[1])
    SIX.append(FA[1])
    if (FA[2] == 1):
        SIX.append(HT[0])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(HT[2])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(HT[3])
        SIX.append(FA[3])
if(FA[0]==3):
    SIX.append(HT[2])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(HT[1])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(HT[0])
        SIX.append(FA[3])
    if (FA[2] == 4):
        SIX.append(HT[3])
        SIX.append(FA[3])
if(FA[0]==4):
    SIX.append(HT[3])
    SIX.append(FA[1])
    if (FA[2] == 2):
        SIX.append(HT[1])
        SIX.append(FA[3])
    if (FA[2] == 3):
        SIX.append(HT[2])
        SIX.append(FA[3])
    if (FA[2] == 1):
        SIX.append(HT[0])
        SIX.append(FA[3])

SA=ematch(SIX[0],SIX[2])

print("16강:",SIX)


import random

class party:
    def __init__(self,win,potion,elix):
        self.potion = potion
        self.elix = elix
        self.win = win
        self.rand = random.randrange(2,6)
    def party1(self):
        self.attack1_1 = 100
        self.attack1_2 = 150
        self.hp1 = 500
        self.mp1 = 300
        return ["초코의용군😁",self.attack1_1, self.attack1_2, self.hp1, self.mp1]
    def party2(self):
        self.attack2_1 = 100
        self.attack2_2 = 150
        self.hp2 = 500
        self.mp2 = 300
        return ["킹기태🧙🏼‍♀️", self.attack2_1,self.attack2_2, self.hp2, self.mp2]
    def party3(self):
        self.attack3_1 = 100
        self.attack3_2 = 150
        self.hp3 = 500
        self.mp3 = 300
        return ["약범규🏄🏼‍♀️", self.attack3_1, self.attack3_2, self.hp3, self.mp3]
    def party4(self):
        self.attack4_1 = 100
        self.attack4_2 = 150
        self.hp4 = 500
        self.mp4 = 300
        return ["보우연재🧛🏼‍♂️", self.attack4_1, self.attack4_2, self.hp4, self.mp4]
    def inven(self):
        return self.potion, self.elix


class Mon_Status:
    def Diablo(self):
        self.name = '디아복로👹'
        self.attack = random.randrange(2500, 8001)
        self.hp = random.randrange(10000, 20001)
        return [self.name, self.attack, self.hp]

    def Wuyeon(self):
        self.name = '우연🤨'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def Ilsungkim(self):
        self.name = '일성킴👺'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def MinJuSeok(self):
        self.name = '민주석😏'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def KyuBeom(self):
        self.name = '규범👽'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def ChulMoom(self):
        self.name = '철몸😾'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def Ado(self):
        self.name = '아르헨도⚽'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]


    def BugBear(self):
        self.name = '버그베어👾'
        self.attack = random.randrange(350, 351)
        self.hp = random.randrange(550, 901)
        return [self.name, self.attack, self.hp]

    def Skull(self):
        self.name = '해골💀'
        self.attack = random.randrange(220, 221)
        self.hp = random.randrange(480, 801)
        return [self.name, self.attack, self.hp]

    def Gull(self):
        self.name = '구울🤢'
        self.attack = random.randrange(180, 181)
        self.hp = random.randrange(450, 701)
        return [self.name, self.attack, self.hp]

    def Zombie(self):
        self.name = '좀비😈'
        self.attack = random.randrange(100, 101)
        self.hp = random.randrange(300, 501)
        return [self.name, self.attack, self.hp]

def Mon_Per():
    a = random.randrange(1, 1001)
    number = a
    MON=Mon_Status()
    if number <= 2:
        return MON.Diablo()
    elif 3 <= number <= 12:
        return MON.Wuyeon()
    elif 13 <= number <= 22:
        return MON.Ilsungkim()
    elif 23 <= number <= 32:
        return MON.MinJuSeok()
    elif 33 <= number <= 42:
        return MON.KyuBeom()
    elif 43 <= number <= 52:
        return MON.ChulMoom()
    elif 53 <= number <= 62:
        return MON.Ado()
    elif 63 <= number <= 102:
        return MON.BugBear()
    elif 103 <= number <= 122:
        return MON.Skull()
    elif 123 <= number <= 422:
        return MON.Gull()
    else:
        return MON.Zombie()

class skill:
    def __init__(self,party1,party2,party3,party4):
        self.party1 = party1
        self.party2 = party2
        self.party3 = party3
        self.party4 = party4

    def skill1(self,mobhp):
        print("초코의용군 스킬1")
        return [2000,1]

    def skill2(self,hpmax):
        print("초코의용군 스킬2",hpmax)
        return [hpmax,2]

    def skill3(self,mobhp):
        print("초코의용군 스킬3")
        return [mobhp-4000,3]

    def skill4(self, mobhp):
        print("킹기태 스킬1")
        return [3000,1]

    def skill5(self, hpmax):
        print("킹기태 스킬2")
        return [hpmax,2]

    def skill6(self, mobhp):
        print("킹기태 스킬3")
        return [mobhp - 4000,3]

    def skill7(self, mobhp):
        print("약범규 스킬1")
        return [1000,1]

    def skill8(self,hpmax):
        print("약범규 스킬2")
        return [hpmax,2]

    def skill9(self, mobhp):
        print("약범규 스킬3")
        return [mobhp - 4000,3]

    def skill10(self, mobhp):
        print("보우연재 스킬1")
        return [4000,1]

    def skill11(self, hpmax):
        print("보우연재 스킬2")
        return [hpmax,2]

    def skill12(self, mobhp):
        print("보우연재 스킬3")
        return [mobhp - 4000,3]

def skillcheck(num,win,potion,elix,mon):                                    #인자생성에 필요한 win,포션,엘릭서와구분을 위한 num값,계산을위한mob값
    partys=party(win,potion,elix)                                           #파티정보 받아오기위한준비
    allskill = skill(partys.party1(),partys.party2(),partys.party3(),partys.party4())
    partys2=partys.party1()
    if num==1:
        print("초코의용군 스킬,1,2,3")
        select=int(input())                      #제안:1번은 다 공격스킬, 2번은 회복스킬
        if select==1:
            return allskill.skill1(mon[2])
        if select==2:
            return allskill.skill2(partys2[3])
        if select==3:
            return allskill.skill3(mon[2])
    if num==2:
        print("킹기태 스킬,1,2,3")
        select = int(input())
        if select == 1:
            return allskill.skill4(mon[2])
        if select == 2:
            return allskill.skill5(partys2[3])
        if select == 3:
            return allskill.skill6(mon[2])
    if num==3:
        print("약범규 스킬,1,2,3")
        select = int(input())
        if select == 1:
            return allskill.skill7(mon[2])
        if select == 2:
            return allskill.skill8(partys2[3])
        if select == 3:
            return allskill.skill9(mon[2])
    if num==4:
        print("보우연재 스킬,1,2,3")
        select = int(input())
        if select == 1:
            return allskill.skill10(mon[2])
        if select == 2:
            return allskill.skill11(partys2[3])
        if select == 3:
            return allskill.skill12(mon[2])

def printstat(mon,uy,king,yak,bow,potion,elix):
    print(f"{mon[0]} 출현!!")
    print(f"{mon[0]} 공격력:{mon[1]} 체력:{mon[2]}")
    print("")
    print(f"{uy[0]} 최소 공격력:{uy[1]} 최대 공격력:{uy[2]} 체력:{uy[3]} 마력:{uy[4]} // 포션:{potion} 엘릭서:{elix}")
    print("")
    print(f"{king[0]} 최소 공격력:{king[1]} 최대 공격력:{king[2]} 체력:{king[3]} 마력:{king[4]} // 포션:{potion} 엘릭서:{elix}")
    print("")
    print(f"{yak[0]} 최소 공격력:{yak[1]} 최대 공격력:{yak[2]} 체력:{yak[3]} 마력:{yak[4]} // 포션:{potion} 엘릭서:{elix}")
    print("")
    print(f"{bow[0]} 최소 공격력:{bow[1]} 최대 공격력:{bow[2]} 체력:{bow[3]} 마력:{bow[4]} // 포션:{potion} 엘릭서:{elix}")
    print("")
    print("")
#부두목들이랑 디아복로 죽인거 카운팅 하는 식 추가해야됨
def battle(win):
    mon = Mon_Per()
    potion = elix = 0
    partys=party(win, potion, elix)
    uy = partys.party1()
    king = partys.party2()
    yak = partys.party3()
    bow = partys.party4()
    uy[3]-=200
    king[3]-=200
    yak[3]-=200
    bow[3]-=200
    players = [uy, king, yak, bow]
    # hpmax = uy[2] = king[2] = yak[2] = bow[2]
    # mpmax = uy[3] = king[3] = yak[3] = bow[3]
    elix_status = 0

    while True:
        playercheck=1
        printstat(mon, uy, king, yak, bow, potion, elix)
        #의용군 파티가 몬스터를 공격
        print("1.공격 2.스킬 3.도망 4.물약 / 넷 중 하나를 선택하십시오")
        select = int(input())
        if select == 1:
            print(f"{uy[0]}이 {mon[0]}(를)을 공격했습니다.")
            print("")
            if mon[2] >= 0:
                atk_uy = random.randint(uy[1], uy[2]+1)
                print(f"{mon[0]}의 체력이 {atk_uy}만큼 줄었습니다.")
                mon[2] -= atk_uy
                print("")
                print(f"현재 몬스터 체력:{mon[2]}")

        elif select == 2:                                                           #스킬
            skill = skillcheck(playercheck, win, potion, elix, mon)
            if skill[1] == 1:
                mon[2] -= skill[0]
            if skill[1] == 2:
                uy[3] = skill[0]
                if mon[2] <= 0:
                    print("=" * 50)
                    print("의용군 파티의 승리입니다!")
                    win += 1

        if mon[2] <= 0:
            print(f"{mon[0]}의 체력이 {mon[2]}만큼 줄었습니다.")
            mon[2] = 0
            print(f"{mon[0]}의 체력이 {mon[2]}이 됐습니다.")
            print("")
            for i in range(1, 5):
                x = random.randint(2, 6)
                uy[i] += round((uy[i] * x / 100))
                king[i] += round((king[i] * x / 100))
                yak[i] += round((yak[i] * x / 100))
                bow[i] += round((bow[i] * x / 100))

                print(f"{uy[0]}의 레벨:{win}\n{uy[0]}의 최소 공격력:{uy[1]}\n{uy[0]}의 최대 공격력:{uy[2]}\n{uy[0]}의 체력:{uy[3]}\n{uy[0]}의 마력:{uy[4]}")
                print(f"{king[0]}의 레벨:{win}\n{king[0]}의 최소 공격력:{king[1]}\n{king[0]}의 최대 공격력:{king[2]}\n{king[0]}의 체력:{king[3]}\n{king[0]}의 마력:{king[4]}")
                print(f"{yak[0]}의 레벨:{win}\n{yak[0]}의 최소 공격력:{yak[1]}\n{yak[0]}의 최대 공격력:{yak[2]}\n{yak[0]}의 체력:{yak[3]}\n{yak[0]}의 마력:{yak[4]}")
                print(f"{bow[0]}의 레벨:{win}\n{bow[0]}의 최소 공격력:{bow[1]}\n{bow[0]}의 최대 공격력:{bow[2]}\n{bow[0]}의 체력:{bow[3]}\n{bow[0]}의 마력:{bow[4]}")
                print("=" * 50)
                # 부두목 6인과 디아복로까지 죽였을때 엔딩 여기 넣어야 됨
                return 1

        elif select == 3:
            print(f"{uy[0]}이 도망을 선택했습니다.")
            escape = random.randrange(1, 101)
            if escape <= 10:
                print("도망가는데 성공했습니다.")
                return 0
            else:
                print("도망가는데 실패했습니다.")

        elif select == 4:
                print("1.포션 2.엘릭서 3.라면")
                select2 = int(input())
                if select2 == 1:
                    potion -= 1
                    k = random.randrange(30, 81)
                    k1 = uy[3] * k // 100
                    uy[3] += k1
                    print(f"체력이 {k1}만큼 올랐습니다.")

                elif select2 == 2:
                    elix_status += 10
                    elix -= 1

                elif select2 == 3:
                    print("라면!")

                else:
                    print("잘못된 입력입니다.")

        playercheck = 2
        printstat(mon, uy, king, yak, bow, potion, elix)
        print("1.공격 2.스킬 3.도망 4.물약 / 넷 중 하나를 선택하십시오")
        select = int(input())
        if select == 1:
            print(f"{king[0]}가 {mon[0]}(를)을 공격했습니다.")
            print("")
            if mon[2] >= 0:
                    atk_king = random.randint(king[1], king[2] + 1)
                    print(f"{mon[0]}의 체력이 {atk_king}만큼 줄었습니다.")
                    mon[2] -= atk_king
                    print("")
                    print(f"현재 몬스터 체력:{mon[2]}")

            if mon[2] <= king[1]:
                print(f"{mon[0]}의 체력이 {mon[2]}만큼 줄었습니다.")
                mon[2] = 0
                print(f"{mon[0]}의 체력이 {mon[2]}이 됐습니다.")
                print("")
        elif select == 2:
            skill = skillcheck(playercheck, win, potion, elix, mon)
            if skill[1] == 1:
                mon[2] -= skill[0]

                if mon[2] <= 0:
                    print("=" * 50)
                    print("의용군 파티의 승리입니다!")
                    win += 1

                    for i in range(1, 5):
                        x = random.randint(2, 6)
                        uy[i] += round((uy[i] * x / 100))
                        king[i] += round((king[i] * x / 100))
                        yak[i] += round((yak[i] * x / 100))
                        bow[i] += round((bow[i] * x / 100))

                    print(
                        f"{uy[0]}의 레벨:{win}\n{uy[0]}의 최소 공격력:{uy[1]}\n{uy[0]}의 최대 공격력:{uy[2]}\n{uy[0]}의 체력:{uy[3]}\n{uy[0]}의 마력:{uy[4]}")
                    print(
                        f"{king[0]}의 레벨:{win}\n{king[0]}의 최소 공격력:{king[1]}\n{king[0]}의 최대 공격력:{king[2]}\n{king[0]}의 체력:{king[3]}\n{king[0]}의 마력:{king[4]}")
                    print(
                        f"{yak[0]}의 레벨:{win}\n{yak[0]}의 최소 공격력:{yak[1]}\n{yak[0]}의 최대 공격력:{yak[2]}\n{yak[0]}의 체력:{yak[3]}\n{yak[0]}의 마력:{yak[4]}")
                    print(
                        f"{bow[0]}의 레벨:{win}\n{bow[0]}의 최소 공격력:{bow[1]}\n{bow[0]}의 최대 공격력:{bow[2]}\n{bow[0]}의 체력:{bow[3]}\n{bow[0]}의 마력:{bow[4]}")
                    print("=" * 50)
                    # 부두목 6인과 디아복로까지 죽였을때 엔딩 여기 넣어야 됨
                    return 1

        elif select == 3:
            print(f"{king[0]}가 도망을 선택했습니다.")
            escape = random.randrange(1, 101)
            if escape <= 10:
                print("도망가는데 성공했습니다.")
                return 0
            else:
                print("도망가는데 실패했습니다.")

        elif select == 4:
            print("1.포션 2.엘릭서 3.라면")
            select2 = int(input())
            if select2 == 1:
                potion -= 1
                u = random.randrange(30, 81)
                u1 = king[3] * u // 100
                king[3] += u1
                print(f"체력이 {u1}만큼 올랐습니다.")

            elif select2 == 2:
                elix_status += 10
                elix -= 1

            elif select2 == 3:
                print("라면!")

            else:
                print("잘못된 입력입니다.")

        playercheck = 3
        printstat(mon, uy, king, yak, bow, potion, elix)
        print("1.공격 2.스킬 3.도망 4.물약 / 넷 중 하나를 선택하십시오")
        select = int(input())
        if select == 1:
            print(f"{yak[0]}가 {mon[0]}(를)을 공격했습니다.")
            print("")
            if mon[2] >= 0:
                atk_yak = random.randint(yak[1], yak[2] + 1)
                print(f"{mon[0]}의 체력이 {atk_yak}만큼 줄었습니다.")
                mon[2] -= atk_yak
                print("")
                print(f"현재 몬스터 체력:{mon[2]}")

            elif mon[2] <= yak[1]:
                print(f"{mon[0]}의 체력이 {mon[2]}만큼 줄었습니다.")
                mon[2] = 0
                print(f"{mon[0]}의 체력이 {mon[2]}이 됐습니다.")
                print("")
        elif select == 2:
            skill = skillcheck(playercheck, win, potion, elix, mon)
            if skill[1] == 1:
                mon[2] -= skill[0]

                if mon[2] <= 0:
                    print("=" * 50)
                    print("의용군 파티의 승리입니다!")
                    win += 1

                    for i in range(1, 5):
                        x = random.randint(2, 6)
                        uy[i] += round((uy[i] * x / 100))
                        king[i] += round((king[i] * x / 100))
                        yak[i] += round((yak[i] * x / 100))
                        bow[i] += round((bow[i] * x / 100))

                    print(f"{uy[0]}의 레벨:{win}\n{uy[0]}의 최소 공격력:{uy[1]}\n{uy[0]}의 최대 공격력:{uy[2]}\n{uy[0]}의 체력:{uy[3]}\n{uy[0]}의 마력:{uy[4]}")
                    print(f"{king[0]}의 레벨:{win}\n{king[0]}의 최소 공격력:{king[1]}\n{king[0]}의 최대 공격력:{king[2]}\n{king[0]}의 체력:{king[3]}\n{king[0]}의 마력:{king[4]}")
                    print(f"{yak[0]}의 레벨:{win}\n{yak[0]}의 최소 공격력:{yak[1]}\n{yak[0]}의 최대 공격력:{yak[2]}\n{yak[0]}의 체력:{yak[3]}\n{yak[0]}의 마력:{yak[4]}")
                    print(f"{bow[0]}의 레벨:{win}\n{bow[0]}의 최소 공격력:{bow[1]}\n{bow[0]}의 최대 공격력:{bow[2]}\n{bow[0]}의 체력:{bow[3]}\n{bow[0]}의 마력:{bow[4]}")
                    print("=" * 50)
                    # 부두목 6인과 디아복로까지 죽였을때 엔딩 여기 넣어야 됨
                    return 1

        elif select == 3:
            print(f"{yak[0]}이 도망을 선택했습니다.")
            escape = random.randrange(1, 101)
            if escape <= 10:
                print("도망가는데 성공했습니다.")
                return 0
            else:
                print("도망가는데 실패했습니다.")

        elif select == 4:
            print("1.포션 2.엘릭서 3.라면")
            select2 = int(input())
            if select2 == 1:
                potion -= 1
                h = random.randrange(30, 81)
                h1 = yak[3] * h // 100
                yak[3] += h1
                print(f"체력이 {h1}만큼 올랐습니다.")

            elif select2 == 2:
                elix_status += 10
                elix -= 1

            elif select2 == 3:
                print("라면!")

            else:
                print("잘못된 입력입니다.")

        playercheck = 4
        printstat(mon, uy, king, yak, bow, potion, elix)
        print("1.공격 2.스킬 3.도망 4.물약 / 넷 중 하나를 선택하십시오")
        select = int(input())
        if select == 1:
            print(f"{bow[0]}가 {mon[0]}(를)을 공격했습니다.")
            print("")
            if mon[2] >= 0:
                atk_bow = random.randint(bow[1], bow[2] + 1)
                print(f"{mon[0]}의 체력이 {atk_bow}만큼 줄었습니다.")
                mon[2] -= atk_bow
                print("")
                print(f"현재 몬스터 체력:{mon[2]}")

            elif mon[2] <= bow[1]:
                print(f"{mon[0]}의 체력이 {mon[2]}만큼 줄었습니다.")
                mon[2] = 0
                print(f"{mon[0]}의 체력이 {mon[2]}이 됐습니다.")
                print("")
        elif select == 2:
            skill = skillcheck(playercheck, win, potion, elix, mon)
            if skill[1] == 1:
                mon[2] -= skill[0]
                if mon[2] <= 0:
                    print("=" * 50)
                    print("의용군 파티의 승리입니다!")
                    win += 1

                    for i in range(1, 5):
                        x = random.randint(2, 6)
                        uy[i] += round((uy[i] * x / 100))
                        king[i] += round((king[i] * x / 100))
                        yak[i] += round((yak[i] * x / 100))
                        bow[i] += round((bow[i] * x / 100))

                    print(f"{uy[0]}의 레벨:{win}\n{uy[0]}의 최소 공격력:{uy[1]}\n{uy[0]}의 최대 공격력:{uy[2]}\n{uy[0]}의 체력:{uy[3]}\n{uy[0]}의 마력:{uy[4]}")
                    print(f"{king[0]}의 레벨:{win}\n{king[0]}의 최소 공격력:{king[1]}\n{king[0]}의 최대 공격력:{king[2]}\n{king[0]}의 체력:{king[3]}\n{king[0]}의 마력:{king[4]}")
                    print(f"{yak[0]}의 레벨:{win}\n{yak[0]}의 최소 공격력:{yak[1]}\n{yak[0]}의 최대 공격력:{yak[2]}\n{yak[0]}의 체력:{yak[3]}\n{yak[0]}의 마력:{yak[4]}")
                    print(f"{bow[0]}의 레벨:{win}\n{bow[0]}의 최소 공격력:{bow[1]}\n{bow[0]}의 최대 공격력:{bow[2]}\n{bow[0]}의 체력:{bow[3]}\n{bow[0]}의 마력:{bow[4]}")
                    print("=" * 50)
                    # 부두목 6인과 디아복로까지 죽였을때 엔딩 여기 넣어야 됨
                    return 1


        elif select == 2:
            skillcheck(playercheck, win, potion, elix, mon)

        elif select == 3:
            print(f"{bow[0]}이 도망을 선택했습니다.")
            escape = random.randrange(1, 101)
            if escape <= 10:
                print("도망가는데 성공했습니다.")
                return 0
            else:
                print("도망가는데 실패했습니다.")

        elif select == 4:
            print("1.포션 2.엘릭서 3.라면")
            select2 = int(input())
            if select2 == 1:
                potion -= 1
                l = random.randrange(30, 81)
                l1 = bow[3] * l // 100
                bow[3] += l1
                print(f"체력이 {l1}만큼 올랐습니다.")

            elif select2 == 2:
                elix_status += 10
                elix -= 1

            elif select2 == 3:
                print("라면!")

            else:
                print("잘못된 입력입니다.")




win=1
battle(win)
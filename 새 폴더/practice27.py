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
        return ["초코의용군",self.attack1_1, self.attack1_2, self.hp1, self.mp1]
    def party2(self):
        self.attack2_1 = 100
        self.attack2_2 = 150
        self.hp2 = 500
        self.mp2 = 300
        return ["킹기태", self.attack2_1,self.attack2_2, self.hp2, self.mp2]
    def party3(self):
        self.attack3_1 = 100
        self.attack3_2 = 150
        self.hp3 = 500
        self.mp3 = 300
        return ["약범규", self.attack3_1, self.attack3_2, self.hp3, self.mp3]
    def party4(self):
        self.attack4_1 = 100
        self.attack4_2 = 150
        self.hp4 = 500
        self.mp4 = 300
        return ["보우연재", self.attack4_1, self.attack4_2, self.hp4, self.mp4]
    def inven(self):
        return self.potion, self.elix


class Mon_Status:
    def Diablo(self):
        self.name = '디아복로'
        self.attack = random.randrange(2500, 8001)
        self.hp = random.randrange(10000, 20001)
        return [self.name, self.attack, self.hp]

    def Wuyeon(self):
        self.name = '우연'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def Ilsungkim(self):
        self.name = '일성킴'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def MinJuSeok(self):
        self.name = '민주석'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def KyuBeom(self):
        self.name = '규범'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def ChulMoom(self):
        self.name = '철몸'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def Ado(self):
        self.name = '아르헨도'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]


    def BugBear(self):
        self.name = '버그베어'
        self.attack = random.randrange(350, 351)
        self.hp = random.randrange(550, 901)
        return [self.name, self.attack, self.hp]

    def Skull(self):
        self.name = '해골'
        self.attack = random.randrange(220, 221)
        self.hp = random.randrange(480, 801)
        return [self.name, self.attack, self.hp]

    def Gull(self):
        self.name = '구울'
        self.attack = random.randrange(180, 181)
        self.hp = random.randrange(450, 701)
        return [self.name, self.attack, self.hp]

    def Zombie(self):
        self.name = '좀비'
        self.attack = random.randrange(100, 101)
        self.hp = random.randrange(3000, 5001)
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
        return mobhp-2000

    def skill2(self,mobhp):
        print("초코의용군 스킬2")
        return mobhp-3000

    def skill3(self,mobhp):
        print("초코의용군 스킬3")
        return mobhp-4000

    def skill4(self, mobhp):
        print("킹기태 스킬1")
        print(mobhp - 2000)

    def skill5(self, mobhp):
        print("킹기태 스킬2")
        return mobhp - 3000

    def skill6(self, mobhp):
        print("킹기태 스킬3")
        return mobhp - 4000

    def skill7(self, mobhp):
        print("약범규 스킬1")
        print(mobhp - 2000)

    def skill8(self, mobhp):
        print("약범규 스킬2")
        return mobhp - 3000

    def skill9(self, mobhp):
        print("약범규 스킬3")
        return mobhp - 4000

    def skill10(self, mobhp):
        print("보우연재 스킬1")
        print(mobhp - 2000)

    def skill11(self, mobhp):
        print("보우연재 스킬2")
        return mobhp - 3000

    def skill12(self, mobhp):
        print("보우연재 스킬3")
        return mobhp - 4000

def skillcheck(num,win,potion,elix,mon):                                    #인자생성에 필요한 win,포션,엘릭서와구분을 위한 num값,계산을위한mob값
    partys=party(win,potion,elix)                                       #파티정보 받아오기위한준비
    allskill = skill(partys.party1(),partys.party2(),partys.party3(),partys.party4())
    if num==1:
        select=int(input(print("초코의용군 스킬,1,2,3")))                      #제안:1번은 다 공격스킬, 2번은 회복스킬
        if select==1:
            allskill.skill1(mon[2])
        if select==2:
            allskill.skill2(party)
        if select==3:
            allskill.skill1(mon[2])
    if num==2:
        select = int(input(print("킹기태 스킬,1,2,3")))
        if select == 1:
            allskill.skill4(mon[2])
        if select == 2:
            allskill.skill5(mon[2])
        if select == 3:
            allskill.skill6(mon[2])
    if num==3:
        select = int(input(print("약범규 스킬,1,2,3")))
        if select == 1:
            allskill.skill7(mon[2])
        if select == 2:
            allskill.skill8(mon[2])
        if select == 3:
            allskill.skill9(mon[2])
    if num==4:
        select = int(input(print("보우연재 스킬,1,2,3")))
        if select == 1:
            allskill.skill10(mon[2])
        if select == 2:
            allskill.skill11(mon[2])
        if select == 3:
            allskill.skill12(mon[2])




#부두목들이랑 디아복로 죽인거 카운팅 하는 식 추가해야됨
def battle(win):
    num=4                                                                               #스킬번호 임시설정
    mon = Mon_Per()
    potion = elix = 0
    partys=party(win, potion, elix)
    uy = partys.party1()
    king = partys.party2()
    yak = partys.party3()
    bow = partys.party4()
    players = [uy, king, yak, bow]
    # hpmax = uy[2] = king[2] = yak[2] = bow[2]
    # mpmax = uy[3] = king[3] = yak[3] = bow[3]
    print(f"{mon[0]} 출현!!")
    print("")
    elix_status = 0
    while True:
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

        print("1.공격 2.도망 3.물약 / 셋 중 하나를 선택하십시오")
        select = int(input())
        if select == 1:
            print(f"{uy[0]}이 {mon[0]}(를)을 공격했습니다.")
            print("")
            if mon[2] <= uy[1]:

                print(f"{mon[0]}의 체력이 {mon[2]}만큼 줄었습니다.")
                mon[2] = 0
                print(f"{mon[0]}의 체력이 {mon[2]}이 됐습니다.")
                print("")
                if mon[2] <= 0:
                    print("=" * 50)
                    print("의용군 파티의 승리입니다!")
                    win += 1
                    x = random.randint(2, 6)

                    uy[1] += round((uy[1] * x / 100))
                    uy[2] += round((uy[2] * x / 100))
                    uy[3] += round((uy[3] * x / 100))
                    uy[4] += round((uy[4] * x / 100))

                    king[1] += round((king[1] * x / 100))
                    king[2] += round((king[2] * x / 100))
                    king[3] += round((king[3] * x / 100))
                    king[4] += round((king[4] * x / 100))

                    yak[1] += round((yak[1] * x / 100))
                    yak[2] += round((yak[2] * x / 100))
                    yak[3] += round((yak[3] * x / 100))
                    yak[4] += round((yak[4] * x / 100))

                    bow[1] += round((bow[1] * x / 100))
                    bow[2] += round((bow[2] * x / 100))
                    bow[3] += round((bow[3] * x / 100))
                    bow[4] += round((bow[4] * x / 100))

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
                    return mon

            else:
                atk_uy = random.randint(uy[1], uy[2]+1)
                print(f"{mon[0]}의 체력이 {atk_uy}만큼 줄었습니다.")
                mon[2] -= atk_uy
                print("")
                print(f"몬스터의 피가 {mon[2]} 남음")

            print(f"{king[0]}가 {mon[0]}(를)을 공격했습니다.")
            print("")
            if mon[2] <= king[1]:

                print(f"{mon[0]}의 체력이 {mon[2]}만큼 줄었습니다.")
                mon[2] = 0
                print(f"{mon[0]}의 체력이 {mon[2]}이 됐습니다.")
                print("")
                if mon[2] <= 0:
                    print("=" * 50)
                    print("의용군 파티의 승리입니다!")
                    win += 1
                    x = random.randint(2, 6)

                    uy[1] += round((uy[1] * x / 100))
                    uy[2] += round((uy[2] * x / 100))
                    uy[3] += round((uy[3] * x / 100))
                    uy[4] += round((uy[4] * x / 100))

                    king[1] += round((king[1] * x / 100))
                    king[2] += round((king[2] * x / 100))
                    king[3] += round((king[3] * x / 100))
                    king[4] += round((king[4] * x / 100))

                    yak[1] += round((yak[1] * x / 100))
                    yak[2] += round((yak[2] * x / 100))
                    yak[3] += round((yak[3] * x / 100))
                    yak[4] += round((yak[4] * x / 100))

                    bow[1] += round((bow[1] * x / 100))
                    bow[2] += round((bow[2] * x / 100))
                    bow[3] += round((bow[3] * x / 100))
                    bow[4] += round((bow[4] * x / 100))

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

            else:
                atk_king = random.randint(king[1], king[2]+1)
                print(f"{mon[0]}의 체력이 {atk_king}만큼 줄었습니다.")
                mon[2] -= atk_king
                print("")
                print(f"몬스터의 피가 {mon[2]} 남음")

            print(f"{yak[0]}가 {mon[0]}(를)을 공격했습니다.")
            print("")
            if mon[2] <= yak[1]:
                print(f"{mon[0]}의 체력이 {mon[2]}만큼 줄었습니다.")
                mon[2] = 0
                print(f"{mon[0]}의 체력이 {mon[2]}이 됐습니다.")
                print("")
                if mon[2] <= 0:
                    print("=" * 50)
                    print("의용군 파티의 승리입니다!")
                    win += 1
                    x = random.randint(2, 6)

                    uy[1] += round((uy[1] * x / 100))
                    uy[2] += round((uy[2] * x / 100))
                    uy[3] += round((uy[3] * x / 100))
                    uy[4] += round((uy[4] * x / 100))

                    king[1] += round((king[1] * x / 100))
                    king[2] += round((king[2] * x / 100))
                    king[3] += round((king[3] * x / 100))
                    king[4] += round((king[4] * x / 100))

                    yak[1] += round((yak[1] * x / 100))
                    yak[2] += round((yak[2] * x / 100))
                    yak[3] += round((yak[3] * x / 100))
                    yak[4] += round((yak[4] * x / 100))

                    bow[1] += round((bow[1] * x / 100))
                    bow[2] += round((bow[2] * x / 100))
                    bow[3] += round((bow[3] * x / 100))
                    bow[4] += round((bow[4] * x / 100))

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

            else:
                atk_yak = random.randint(yak[1], yak[2]+1)
                print(f"{mon[0]}의 체력이 {atk_yak}만큼 줄었습니다.")
                mon[2] -= atk_yak
                print("")
                print(f"몬스터의 피가 {mon[2]} 남음")

            print(f"{bow[0]}가 {mon[0]}(를)을 공격했습니다.")
            print("")
            if mon[2] <= bow[1]:

                print(f"{mon[0]}의 체력이 {mon[2]}만큼 줄었습니다.")
                mon[2] = 0
                print(f"{mon[0]}의 체력이 {mon[2]}가 됐습니다.")
                print("")
                if mon[2] <= 0:
                    print("=" * 50)
                    print("의용군 파티의 승리입니다!")
                    win += 1
                    x = random.randint(2, 6)

                    uy[1] += round((uy[1] * x / 100))
                    uy[2] += round((uy[2] * x / 100))
                    uy[3] += round((uy[3] * x / 100))
                    uy[4] += round((uy[4] * x / 100))

                    king[1] += round((king[1] * x / 100))
                    king[2] += round((king[2] * x / 100))
                    king[3] += round((king[3] * x / 100))
                    king[4] += round((king[4] * x / 100))

                    yak[1] += round((yak[1] * x / 100))
                    yak[2] += round((yak[2] * x / 100))
                    yak[3] += round((yak[3] * x / 100))
                    yak[4] += round((yak[4] * x / 100))

                    bow[1] += round((bow[1] * x / 100))
                    bow[2] += round((bow[2] * x / 100))
                    bow[3] += round((bow[3] * x / 100))
                    bow[4] += round((bow[4] * x / 100))

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

                #여기에 승리 조건문 넣어야되나?
            else:
                atk_bow = random.randint(bow[1], bow[2]+1)
                print(f"{mon[0]}의 체력이 {atk_bow}만큼 줄었습니다.")
                print("")
                mon[2] -= atk_bow
                print(f"몬스터의 피가 {mon[2]} 남음")
            print("")

            z = random.randint(1, 3)
            print(f"{mon[0]}(이)가 {players[z][0]}(를)을 공격했습니다.")
            if elix_status == 0:
                if players[z][3] <= mon[1]:
                    players[z][3] = 0 # 요걸 먼저 써야 될 지 프린팅을 먼저해야 될지 고민해봐야 됨
                    print(f"{players[z][0]}체력이 {players[z][3]}만큼 줄었습니다.")

                else:
                    print(f"{players[z][0]}의 체력이 {mon[1]}만큼 줄었습니다.")
                    players[z][3] -= mon[1]

            else:
                print(f"엘릭서로 인해 무적 효과 발동!! 10턴간 무적입니다. {elix_status -1}남음")
                elix_status -= 1
            print(f"{players[z][0]}의 체력이 {players[z][3]}만큼 남았습니다.")
            print("=" * 50)

            if mon[2] <= 0:
                print("=" * 50)
                print("의용군 파티의 승리입니다!")
                win += 1
                x = random.randint(2, 6)

                uy[1] += round((uy[1] * x / 100))
                uy[2] += round((uy[2] * x / 100))
                uy[3] += round((uy[3] * x / 100))
                uy[4] += round((uy[4] * x / 100))

                king[1] += round((king[1] * x / 100))
                king[2] += round((king[2] * x / 100))
                king[3] += round((king[3] * x / 100))
                king[4] += round((king[4] * x / 100))

                yak[1] += round((yak[1] * x / 100))
                yak[2] += round((yak[2] * x / 100))
                yak[3] += round((yak[3] * x / 100))
                yak[4] += round((yak[4] * x / 100))

                bow[1] += round((bow[1] * x / 100))
                bow[2] += round((bow[2] * x / 100))
                bow[3] += round((bow[3] * x / 100))
                bow[4] += round((bow[4] * x / 100))

                print(f"{uy[0]}의 레벨:{win}\n{uy[0]}의 최소 공격력:{uy[1]}\n{uy[0]}의 최대 공격력:{uy[2]}\n{uy[0]}의 체력:{uy[3]}\n{uy[0]}의 마력:{uy[4]}")
                print(f"{king[0]}의 레벨:{win}\n{king[0]}의 최소 공격력:{king[1]}\n{king[0]}의 최대 공격력:{king[2]}\n{king[0]}의 체력:{king[3]}\n{king[0]}의 마력:{king[4]}")
                print(f"{yak[0]}의 레벨:{win}\n{yak[0]}의 최소 공격력:{yak[1]}\n{yak[0]}의 최대 공격력:{yak[2]}\n{yak[0]}의 체력:{yak[3]}\n{yak[0]}의 마력:{yak[4]}")
                print(f"{bow[0]}의 레벨:{win}\n{bow[0]}의 최소 공격력:{bow[1]}\n{bow[0]}의 최대 공격력:{bow[2]}\n{bow[0]}의 체력:{bow[3]}\n{bow[0]}의 마력:{bow[4]}")

                print("=" * 50)
                return 1

            elif uy[2] <= 0:
                print(f"{mon[0]}(이)가 이겼습니다.\n 게임오버....")
                exit()

        elif select == 2:
            print("의용군 파티가 도망을 선택했습니다.")
            escape=random.randrange(1, 101)
            if escape <= 10:
                print("도망가는데 성공했습니다.")
                return 0
            else:
                print("도망가는데 실패했습니다.")
                continue

        elif select == 3:
            print("1.포션 2.엘릭서")
            select2=int(input())
            if select2 == 1:
                potion -= 1
                continue
            elif select2 == 2:
                elix_status += 10
                elix -= 1
            else:
                print("잘못된 입력입니다.")
        elif select == 4:
            skillcheck(num, win, potion, elix, mon)
        else:
            print("잘못된 입력입니다.")




win=1
battle(win)
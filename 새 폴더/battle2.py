
import random
class party:
    def __init__(self,win,potion,elix):
        self.attack1 = None
        self.attack2 = None
        self.attack3 = None
        self.attack4 = None
        self.hp1 = None
        self.hp2 = None
        self.hp3 = None
        self.hp4 = None
        self.mp1 = None
        self.mp2 = None
        self.mp3 = None
        self.mp4 = None
        self.potion = potion
        self.elix = elix
        self.win = win
        self.rand = random.randrange(2,6)
    def party1(self):
        self.attack1 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp1 = round(500 * ((self.win * self.rand/100)+1))
        self.mp1 = round(300 * ((self.win * self.rand/100)+1))
        return ["의용군",self.attack1, self.hp1, self.mp1]
    def party2(self):
        self.attack2 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp2 = round(500 * ((self.win * self.rand/100)+1))
        self.mp2 = round(300 * ((self.win * self.rand / 100) + 1))
        return self.attack2, self.hp2, self.mp2
    def party3(self):
        self.attack3 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp3 = round(500 * ((self.win * self.rand/100)+1))
        self.mp3 = round(300 * ((self.win * self.rand / 100) + 1))
        return self.attack3, self.hp3, self.mp3
    def party4(self):
        self.attack4 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp4 = round(500 * ((self.win * self.rand/100)+1))
        self.mp4 = round(300 * ((self.win * self.rand / 100) + 1))
        return self.attack4, self.hp4, self.mp4
    def inven(self):
        return self.potion, self.elix


def mob():
    moblist=['임시몹',100,500]
    return moblist

def battle():
    win = 0
    potion = elix = 0
    ch_monster=mob()
    partys=party(win,potion,elix)
    uy=partys.party1()
    potion, elix=partys.inven()
    print(f"{ch_monster[0]} 공격력 {ch_monster[1]} 체력 {ch_monster[2]}출현!")  # 몬스터 랜덤으로 출현
    elixir_status = 0
    while True:  # 싸움 반복문 열기
        print(f"{ch_monster[0]} 공격력 {ch_monster[1]} 체력 {ch_monster[2]}")
        print(f"{uy[0]}: {uy[1]}, {uy[2]} // 포션: {potion}, 엘릭서: {elix}")
        print("1.공격 2.도망 3.물약 / 셋 중 하나를 선택하십시오:")  # 공격하거나 도망가거나 선택하는 인풋
        select=int(input())
        if select == 1:  # 공격을 선택했을때
            print(f"{uy[0]}이 {ch_monster[0]}를 공격했습니다.")  # 의용이가 랜덤의 몬스터를 공격한다.
            if ch_monster[2] <= uy[1]:
                print(f"{ch_monster[0]}의 체력이 {ch_monster[2]}만큼 줄었습니다.")  # 몬스터 피가 공격력만큼 줄어듦
            else:
                print(f"{ch_monster[0]}의 체력이 {uy[1]}만큼 줄었습니다.")  # 몬스터 피가 공격력만큼 줄어듦
            ch_monster[2] -= uy[1]
            print(ch_monster[2],"남음")

            if ch_monster[2] <= 0:  # 몬스터 체력이 0에 수렴하면 의용이의 승리
                print("-" * 50)
                print(f"{uy[0]}의 승리입니다.")
                win += 1
                if ch_monster[0] == "디아복로👹":
                    print(f"{uy[0]}이 {ch_monster[0]}을 물리치고 세상을 구했습니다.")
                    exit()
                print(f"{uy[0]}의 레벨:{win}\n{uy[0]}의 \n{uy[0]}의 공격력:{uy[1]}\n")
                break

            print("-" * 50)

            print(f"{ch_monster[0]}이 {uy[0]}을 공격했습니다.")  # 몬스터가 의용이를 공격
            if elixir_status == 0:
                if uy[2] <= ch_monster[2]:
                    print(f"{uy[0]}의 체력이 {uy[2]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                else:
                    print(f"{uy[0]}의 체력이 {ch_monster[2]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                uy[2] -= ch_monster[1]  # 의용이 체력에서 몬스터 공격력만큼 빼줌
            else:
                print(f"엘릭서로 인한 무적 효과 발동중... 데미지를 입지 않습니다. {elixir_status - 1}턴 남음.")
                elixir_status -= 1
            print("-" * 50)

            if ch_monster[2] <= 0:  # 몬스터 체력이 0에 수렴하면 의용이의 승리
                print("-" * 50)
                print(f"{uy[0]}의 승리입니다.")
                win += 1
                print(f"{uy[0]}의 레벨:{win}\n{uy[0]}의 \n{uy[0]}의 공격력:{uy[1]}\n")
                print("-" * 50)
                break
            elif uy[2] <= 0:
                print(f"{ch_monster[0]}(이)가 이겼습니다.\n 게임오버....")  # 몬스터가 이기면 게임 끝
                exit()
        elif select == 2:
            print(f"{uy[0]}이 도망을 선택했습니다.")  # 도망 시나리오
            escape_rate=random.randrange(1,101)
            if escape_rate <= 10:  # 도망 성공
                print("도망가는데 성공했습니다.")
                return ch_monster
            else:  # 도망 실패
                print("도망가는데 실패했습니다.")
                print(f"{ch_monster[0]}이 {uy[0]}을 공격했습니다.")  # 몬스터가 의용이를 공격
                if elixir_status == 0:
                    if uy[2] <= ch_monster[2]:
                        print(f"{uy[0]}의 체력이 {uy[2]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                    else:
                        print(f"{uy[0]}의 체력이 {ch_monster[2]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                    uy[2] -= ch_monster[1]  # 의용이 체력에서 몬스터 공격력만큼 빼줌
                else:
                    print(f"엘릭서로 인한 무적 효과 발동중... 데미지를 입지 않습니다. {elixir_status - 1}턴 남음.")
                    elixir_status -= 1
                print(uy[1],"남음")
                print("-" * 50)
                if uy[2] <= 0:
                    print(f"{ch_monster[0]}(이)가 이겼습니다.\n 게임오버....")  # 몬스터가 이기면 게임 끝
                    exit()
                else:
                    continue
        elif select == 3:
            print("1. 포션 2. 엘릭서")
            select2=int(input())
            if select2 == 1:
                potion-=1
                continue
            elif select2 == 2:
                elixir_status += 10
                elix-=1
            else:
                print("잘못된 입력입니다.")
        else:
            print("잘못된 입력입니다.")
battle()
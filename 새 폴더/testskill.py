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
import random
class party:
    def __init__(self,win,potion,alix):
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
        self.alix = alix
        self.win = win
        self.rand = random.randrange(2,6)
    def party1(self):
        self.attack1 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp1 = round(500 * ((self.win * self.rand/100)+1))
        self.mp1 = round(300 * ((self.win * self.rand/100)+1))
        return [self.attack1, self.hp1, self.mp1]
    def party2(self):
        self.attack2 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp2 = round(500 * ((self.win * self.rand/100)+1))
        self.mp2 = round(300 * ((self.win * self.rand / 100) + 1))
        return [self.attack2, self.hp2, self.mp2]
    def party3(self):
        self.attack3 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp3 = round(500 * ((self.win * self.rand/100)+1))
        self.mp3 = round(300 * ((self.win * self.rand / 100) + 1))
        return [self.attack3, self.hp3, self.mp3]
    def party4(self):
        self.attack4 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp4 = round(500 * ((self.win * self.rand/100)+1))
        self.mp4 = round(300 * ((self.win * self.rand / 100) + 1))
        return [self.attack4, self.hp4, self.mp4]
    def inven(self):
        return self.potion, self.alix

class skill:
    def __init__(self,party1,party2,party3,party4):
        self.party1 = party1
        self.party2 = party2
        self.party3 = party3
        self.party4 = party4

    def test(self,mobhp):
        return mobhp-self.party1[0]

def mob():
    moblist=['임시몹',100,500]
    return moblist

def imsi():
    win=2
    potion=alix=0
    i=0
    while(i<3):
        a=party(win,potion,alix)
        moblist=mob()
        b=skill(a.party1(),a.party2(),a.party3(),a.party4())
        # potion,alix=a.inven()
        # print(potion)
        # potion+=1

        # attack1,hp1,mp1=a.party1()
        # attack2,hp2,mp2=a.party2()
        # attack3,hp3,mp3=a.party3()
        # attack4,hp4,mp4=a.party4()
        #
        # print("공격력",attack1,attack2,attack3,attack4)
        # print("hp",hp1,hp2,hp3,hp4)
        # print("mp", mp1, mp2, mp3, mp4)
        # print("포션,엘릭서",potion,alix)
        # print("스킬테스트",b.test())
        print(b.test(moblist[2]))
        i+=1
imsi()
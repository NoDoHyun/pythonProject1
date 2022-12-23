import random
import keyboard as keyboard
import time

class Mon_Status:
    def __init__(self, name, atk_min, atk_max, hp_min, hp_max, number):

        self.name = name
        self.atk_min = atk_min
        self.atk_max = atk_max
        self.hp_min = hp_min
        self.hp_max = hp_max
        self.number = number

    def atk(self):
            atk = random.randint(self.atk_min, self.atk_max)
            return atk

    def hp(self):
            hp = random.randint(self.hp_min, self.hp_max)
            return hp




def Mon_Per():
    a = random.randrange(1, 1001)
    number = a
    if number <= 2:
        return Diablo()
    elif 3 <= number <= 12:
        return Wuyeon()
    elif 13 <= number <= 22:
        return IlsungKim()
    elif 23 <= number <= 32:
        return MinJuSeok()
    elif 33 <= number <= 42:
        return KyuBeom()
    elif 43 <= number <= 52:
        return ChulMoom()
    elif 53 <= number <= 62:
        return Ado()
    elif 63 <= number <= 102:
        return BugBear()
    elif 103 <= number <= 122:
        return Skull()
    elif 123 <= number <= 422:
        return Guell()
    else:
        return Zombie()






class Diablo(Mon_Status):
    def __init__(self):
        self.name = '디아복로'
        self.atk_min = 2500
        self.atk_max = 8000
        self.hp_min = 10000
        self.hp_max = 20000
        print(f"{self.name}가 등장했다. 이젠 길고 긴 악연을 끊어야 될 때...  ")
        print(f"{self.name}가 공격한다! {self.atk()}의 피해를 입었다.")
        print(f"{self.number}")
    def diablo(self):
        return [self.name,self.atk_max,self.hp_max]
class Wuyeon(Mon_Status):
    def __init__(self):
        self.name = '우연'
        self.atk_min = 1000
        self.atk_max = 3000
        self.hp_min = 5000
        self.hp_max = 10000
        print(f"디아복로의 복심 {self.name}이 등장했다.\n 우연히 디아복로에게 간택을 받은 자다")
        print(f"{self.name}가 공격한다! {self.atk()}의 피해를 입었다.")
    def wuyeon(self):
        return [self.name, self.atk_max, self.hp_max]
class IlsungKim(Mon_Status):
    def __init__(self):
        self.name = '일성킴'
        self.atk_min = 1000
        self.atk_max = 3000
        self.hp_min = 5000
        self.hp_max = 10000
        print(f"디아복로의 복심 {self.name}이 등장했다.\n마계 북부지역을 무력으로 지배하는 자.")
        print(f"{self.name}이 공격한다! {self.atk()}의 피해를 입었다.")
    def ilsungkim(self):
        return [self.name,self.atk_max,self.hp_max]
class MinJuSeok(Mon_Status):
    def __init__(self):
        self.name = '민주석'
        self.atk_min = 1000
        self.atk_max = 3000
        self.hp_min = 5000
        self.hp_max = 10000
        print(f"디아복로의 복심 {self.name}이 등장했다.\n마계의 민주적인 통치를 선호한다.")
        print(f"{self.name}이 공격한다! {self.atk()}의 피해를 입었다.")
    def minjuseok(self):
        return [self.name,self.atk_max,self.hp_max]
class KyuBeom(Mon_Status):
    def __init__(self):
        self.name = '규범'
        self.atk_min = 1000
        self.atk_max = 3000
        self.hp_min = 5000
        self.hp_max = 10000
        print(f"디아복로의 복심 {self.name}이 등장했다.\n마계에서 가장 외골수다.")
        print(f"{self.name}이 공격한다! {self.atk()}의 피해를 입었다.")
    def kyubeom(self):
        return [self.name,self.atk_max,self.hp_max]
class ChulMoom(Mon_Status):
    def __init__(self):
        self.name = '철몸'
        self.atk_min = 1000
        self.atk_max = 3000
        self.hp_min = 5000
        self.hp_max = 10000
        print(f"디아복로의 복심 {self.name}이 등장했다.\n마계의 책략가. 디아복로의 최측근 참모다.")
        print(f"{self.name}이 공격한다! {self.atk()}의 피해를 입었다.")
    def chulmoom(self):
        return [self.name,self.atk_max,self.hp_max]
class Ado(Mon_Status):
    def __init__(self):
        self.name = '아르헨도'
        self.atk_min = 1000
        self.atk_max = 3000
        self.hp_min = 5000
        self.hp_max = 10000
        print(f"디아복로의 복심 {self.name}가 등장했다.\n메시를 좋아하고 축구를 사랑하는 자.")
        print(f"{self.name}가 공격한다! {self.atk()}의 피해를 입었다.")
    def ado(self):
        return [self.name,self.atk_max,self.hp_max]

class BugBear(Mon_Status):
    def __init__(self):
        self.name = '버그베어'
        self.atk_min = 350
        self.atk_max = 350
        self.hp_min = 550
        self.hp_max = 900
        print(f"{self.name}가 등장했다.")
        print(f"{self.name}가 공격한다! {self.atk()}의 피해를 입었다.")
    def bugbear(self):
        return [self.name,self.atk_max,self.hp_max]


class Skull(Mon_Status):
    def __init__(self):
        self.name = '해골'
        self.atk_min = 220
        self.atk_max = 200
        self.hp_min = 480
        self.hp_max = 800
        print(f"{self.name}가 등장했다.")
        print(f"{self.name}가 공격한다! {self.atk()}의 피해를 입었다.")
    def skull(self):
        return [self.name,self.atk_max,self.hp_max]


class Guell(Mon_Status):
    def __init__(self):
        self.name = '구울'
        self.atk_min = 180
        self.atk_max = 180
        self.hp_min = 450
        self.hp_max = 700
        print(f"{self.name}이 등장했다.")
        print(f"{self.name}이 공격한다! {self.atk()}의 피해를 입었다.")



class Zombie(Mon_Status):
    def __init__(self):
        self.name = '좀비'
        self.atk_min = 100
        self.atk_max = 100
        self.hp_min = 300
        self.hp_max = 500
        print(f"{self.name}가 등장했다.")

Mon_Per()
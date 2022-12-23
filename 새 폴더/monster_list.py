import random

#초코 의용군의 구조 설계
def choco_info():
    choco = ['초코의용군',500]   # 초코의용군 = [이름, 1hit(랜덤), hp(500), 포션갯수, 엘릭서갯수]
    choco.insert(1,random.randint(100,150))  #초코의용군 1hit 랜덤 배정
    # print(choco)
    return choco

#몬스터의 구조 설계
def mob_info(num):

    monster = []    # monster = [ [좀비],[구울],[해골],[버그베어],[동혀니],[홍거리],[디아복로] ]

    zombie = ['좀비',100]   #좀비 = [이름, 1hit(100), hp(랜덤)]
    zombie.insert(2, random.randint(300, 500))  # 좀비 hp 랜덤 배정
    monster.append(zombie)

    ghoul = ['구울',180]   #구울 = [이름, 1hit(180), hp(랜덤)]
    ghoul.insert(2, random.randint(450, 700))  # 구울 hp 랜덤 배정
    monster.append(ghoul)

    skull = ['해골',220]   #해골 = [이름, 1hit(220), hp(랜덤)]
    skull.insert(2, random.randint(480, 800))  # 해골 hp 랜덤 배정
    monster.append(skull)

    bugbear = ['버그베어',350] #버그베어 = [이름, 1hit(350), hp(랜덤)]
    bugbear.insert(2, random.randint(500, 900))  # 버그베어 hp 랜덤 배정
    monster.append(bugbear)

    donghyeoni = ['동혀니'] #동혀니 = [이름, 1hit(랜덤), hp(랜덤)]
    donghyeoni.insert(1, random.randint(1000, 3000))  # 동혀니 1hit 랜덤 배정
    donghyeoni.insert(2, random.randint(3000, 8000))  # 동혀니 hp 랜덤 배정
    monster.append(donghyeoni)

    honggeoli = ['홍거리']  #홍거리 = [이름, 1hit(랜덤), hp(랜덤)]
    honggeoli.insert(1, random.randint(1000, 3000))  # 홍거리 1hit 랜덤 배정
    honggeoli.insert(2, random.randint(3000, 8000))  # 홍거리 hp 랜덤 배정
    monster.append(honggeoli)

    diaboklo = ['디아복로']   #디아복로 = [이름, 1hit(랜덤), hp(랜덤)]
    diaboklo.insert(1,random.randint(2500,8000))    #디아복로 1hit 랜덤 배정
    diaboklo.insert(2,random.randint(5000,15000))    #디아복로 hp 랜덤 배정
    monster.append(diaboklo)

    # print(monster)
    return()



#전투 종료 시 50% 확률로 포션/ 0.5확률로 엘릭서 획득 이벤트
def item_get(choco):
    potionget = 1
    elixirget = 1
    potion = random.randint(1,100)
    if potion < 50:         #포션 50% 확률 획득
        choco.insert(3,potionget)
        print('포션 획득')
        elixir = random.randint(1,100)
        if elixir < 0.5:     #엘릭서 포션 발동시 0.5%확률로 획득
            choco.insert(4,elixirget)
            print('엘릭서 획득')
    return choco



print()
print(choco_info()[0],'\thp',choco_info()[2])

print(item_get(choco_info())[0])




#랜덤으로 몬스터를 만났을 때 몬스터 이름과 체력 표시

# print(mob_info()[0])
















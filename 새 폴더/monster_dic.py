import random

choco = {'name':'초코의용군','hp':500}  #초코의용: 1hit(랜덤), hp(500)
choco['hit'] = random.randint(100,150)  #초코의용군 1hit 랜덤 배정

# 몬스터의 구조 설계
# def mob_info():
#     zombie = {'name':'좀비','hit':100}   #좀비 = 1hit(100), hp(랜덤)
#     zombie['hp'] = random.randint(300,500)  #좀비 hp 랜덤 배정
#
#     ghoul = {'name':'구울','hit':180}   #구울 = 1hit(180), hp(랜덤)
#     ghoul['hp'] = random.randint(450,700)    #구울 hp 랜덤 배정
#
#     skull = {'name':'해골','hit':220}   #해골 = 1hit(220), hp(랜덤)
#     skull['hp'] = random.randint(480,800)  #해골 hp 랜덤 배정
#
#     bugbear = {'name':'버그베어','hit':350} #버그베어 = 1hit(350), hp(랜덤)
#     bugbear['hp'] = random.randint(500,900)  #버그베어 hp 랜덤 배정
#
#     donghyeoni = {'name':'동혀니'} #동혀니 = 1hit(랜덤), hp(랜덤)
#     donghyeoni['hit'] = random.randint(1000,3000)  #동혀니 1hit 랜덤 배정
#     donghyeoni['hp'] = random.randint(3000,8000)  #동혀니 hp 랜덤 배정
#
#     honggeoli = {'name':'홍거리'}  #홍거리 = 1hit(랜덤), hp(랜덤)
#     honggeoli['hit'] = random.randint(1000,3000)   #홍거리 1hit 랜덤 배정
#     honggeoli['hp'] = random.randint(3000,8000)    #홍거리 hp 랜덤 배정
#
#     diaboklo = {'name':'디아복로'}   #디아복로 = 1hit(랜덤), hp(랜덤)
#     diaboklo['hit'] = random.randint(2500,8000)   #디아복로 1hit 랜덤 배정
#     diaboklo['hp'] = random.randint(5000,15000)    #디아복로 hp 랜덤 배정
#
#     return(monster)


#랜덤으로 몬스터를 만났을 때 몬스터 이름과 체력 표시
i = random.randrange(1) #임시 랜덤함수
def mob(i):
    if i == 0:
        zombie = ['좀비', 100]  # 좀비 = [이름, 1hit(100), hp(랜덤)]
        zombie.insert(2, random.randint(300, 500))  # 좀비 hp 랜덤 배정
        print(zombie)
    return i

print(mob(i))

    # elif monster == 1:
    #     print(ghoul['name'],'hp',ghoul['hp'])
    # elif monster == 2:
    #     print(skull['name'],'hp',skull['hp'])
    # elif monster == 3:
    #     print(bugbear['name'],'hp',bugbear['hp'])
    # elif monster == 4:
    #     print(donghyeoni['name'],'hp',donghyeoni['hp'])
    # elif monster == 5:
    #     print(honggeoli['name'],'hp',honggeoli['hp'])
    # elif monster == 6:
    #     print(diaboklo['name'],'hp',diaboklo['hp'])


























# #전투 종료 시 50% 확률로 포션/ 0.5확률로 엘릭서 획득 이벤트
# def item_get():
#     potionGet = 1
#     elixirGet = 1
#     potion = random.randint(1,100)
#     if potion < 50:         #포션 50% 확률 획득
#         choco.insert(2,potionGet)
#         print('포션 획득')
#
#         elixir = random.randint(1,100)
#         if elixir < 0.5:     #엘릭서 포션 발동시 0.5%확률로 획득
#             choco.insert(3,elixirGet)
#             print('엘릭서 획득')
















import random
import time
import copy
# 키보드 입력을 받기 위함
import keyboard as keyboard


# 장은희
def player_create():  # 캐릭터 정보 (딕셔너리)
    choco = {'minDmg': 100, 'maxDmg': 150, 'winCnt': 0, 'maxHp': 500, 'hp': 500, 'potion': 0, 'elixir': 0}
    return choco


# 전투 종료 시 50% 확률로 포션/ 0.5확률로 엘릭서 획득 이벤트
def item_drop(player, win):  # 이길 때 마다 포션+엘릭서 드롭 함수
    print()
    if win == 1:
        potion = random.randint(1, 200)
        if potion <= 100:  # 포션 50% 확률 획득
            player['potion'] += 1  # player[3] (=choco[3]=포션 갯수) 에 1개 추가
            print("🧪\033[32m포션 획득🧪")
            if potion <= 1:  # 엘릭서 포션 발동시 0.5%확률로 획득
                player['elixir'] += 1  # player[4] (=choco[4]=엘릭서 갯수) 에 1개 추가
                print("🧪\033[32m엘릭서 획득🧪")
    print(f"\033[32m현재 보유 중인 포션: {player['potion']} 개")
    print(f"\033[32m현재 보유 중인 엘릭서: {player['elixir']} 개\033[0m")
    return player


# 전투 종료(승리)시 공격력/hp가 5%씩 성장하는 이벤트
def level_up(player):  # 이길 때 마다 공격력(1hit)+hp 증가 함수
    print()
    print('\033[96m공격력과 hp가 5% 증가 합니다')
    print(f"\033[93mhp: {player['maxHp']} →", end=' ')
    player['maxHp'] = round(player['maxHp'] * 1.05)  # player['maxHp'] (=최대공격력) 에 5% 증가한 '값'을 추가
    print(f"\033[96m{player['maxHp']}")
    player['hp'] = player['maxHp']
    print(f"\033[93matk: {round(player['minDmg'] * (1 + player['winCnt'] * 0.05))}"
          f"~{round(player['maxDmg'] * (1 + player['winCnt'] * 0.05))} →", end=' ')
    player['winCnt'] += 1  # win 카운트
    print(
        f"\033[96m{round(player['minDmg'] * (1 + player['winCnt'] * 0.05))}"
        f"~{round(player['maxDmg'] * (1 + player['winCnt'] * 0.05))}")
    return player


def mob_info(mobSpin):  # 결정 함수를 토대로 정보 리턴하는 함수
    mob = {'name': None, 'minDmg': 0, 'maxDmg': 0, 'maxHp': 0, 'hp': 0}
    if mobSpin == 1:
        mob['name'] = '좀비'
        mob['maxHp'] = random.randint(300, 500)
        mob['hp'] = mob['maxHp']
        mob['minDmg'] = 100
        mob['maxDmg'] = 100
    elif mobSpin == 2:
        mob['name'] = '구울'
        mob['maxHp'] = random.randint(450, 700)
        mob['hp'] = mob['maxHp']
        mob['minDmg'] = 180
        mob['maxDmg'] = 180
    elif mobSpin == 3:
        mob['name'] = '해골'
        mob['maxHp'] = random.randint(480, 800)
        mob['hp'] = mob['maxHp']
        mob['minDmg'] = 220
        mob['maxDmg'] = 220
    elif mobSpin == 4:
        mob['name'] = '버그베어'
        mob['maxHp'] = random.randint(550, 900)
        mob['hp'] = mob['maxHp']
        mob['minDmg'] = 350
        mob['maxDmg'] = 350
    elif mobSpin == 5:
        mob['name'] = '동혀니'
        mob['maxHp'] = random.randint(3000, 8000)
        mob['hp'] = mob['maxHp']
        mob['minDmg'] = 1000
        mob['maxDmg'] = 3000
    elif mobSpin == 6:
        mob['name'] = '홍거리'
        mob['maxHp'] = random.randint(3000, 8000)
        mob['hp'] = mob['maxHp']
        mob['minDmg'] = 1000
        mob['maxDmg'] = 3000
    elif mobSpin == 7:
        mob['name'] = '디아복로'
        mob['maxHp'] = random.randint(5000, 15000)
        mob['hp'] = mob['maxHp']
        mob['minDmg'] = 2500
        mob['maxDmg'] = 8000
    return mob


# 노도현
def img(mob):  # 이미지 출력
    clear()
    if mob['name'] == '좀비' or mob['name'] == '구울':
        print("                                        ,~-,")
        print("                                      ,;=;::.")
        print("                                      ,;=;::.")
        print("                                      ,;=;::.")
        print("                     *$*-            ~!*=!;:,")
        print("                     :;~..           =*==**!,.")
        print("                    ,-~!,--   :;,:-~*!#$=###;,")
        print("                 .-::;;;*;-,~:;;;*==#$#=!;=#**:")
        print("                 ~:!**!:*;~~~:!!$$$=###=$=!!!~")
        print("               ,!*==*!;~=$:--:;;$$$$@######$$!")
        print("            .;!;*=$$=!::=$*~-::!$$$$#######$*!")
        print("           :=!*$*===*!!!$$**:~;*$##=$#####@@$~")
        print("         .!==****!*=***;*$=-:::*$#$==#####@@:")
        print("         *=$$==!;!;!*$==!!=---~=#$=*$#@@$$##~")
        print("        *=###=*:~:;-!$$=**$=!~:=#$=*$###$#$=*~.")
        print("     .;**=$#$***;;;*:*=$==!=***$#$*=$$#@####$:,.")
        print("   .*=*=*!*#$=*!;;;!*!=##$=$=$=$#=**=#####$#*~--")
        print("  .=$$=**!;*$==**!!*$*$@###$$==$#$*!=###=$##*~-,.")
        print("  =#$$=!!;!!$$==$====*#@#$#$====##*;*##$=##$;:-,-.")
        print(" ,####=**=;;*$#$==***@@#@#====**=#*=$=**$##!-~~:=:")
        print(" !$$##$***;;=###=====@@@@@#*!!!;!==@!**;=#=:---;=~")

    elif mob['name'] == '해골':
        print("         .        ,!==$:      .            .")
        print("                  :*$$$!")
        print("                  ;#$#$:")
        print("                  ,*$$*")
        print(".            .    .-**$,  .    .  .    .    .")
        print("                   ,!;#*.")
        print("                    . ;@-.")
        print("                   ...;#!~---.")
        print("    .    .       ..--:~=*;$!!-.    .       .    .")
        print("             .    -=!=!*!-=#*=")
        print("                  ==!=;!*:==~:,")
        print("                  *.!*:*=*!=-,~")
        print("                  *.~~~=*=;:: :")
        print("                  !.:,~!*=!-! ;")
        print("                  ; :-~,$*=~~ --")
        print("                  : ~!~;#*;=, .;.")
        print("                  : -::~$=~*,  *,")
        print("             .    ; .!-.*$,~, .;~      .")
        print("                 .*, ;  *$     ,~")
        print("                 -!,.:..*#.     ;")

    elif mob['name'] == '버그베어' or mob['name'] == '동혀니' or mob['name'] == '홍거리':
        print("   ;$==$!")
        print("    ;:=#=.    ,.  .-")
        print("    ~:==..  ~*=!;!*.")
        print("    -:*   ,!!!,;:-*:.")
        print("    ~::    ;;-;$;===;~,.")
        print("    ~!-  .!;~:$=!:~:!~--~.")
        print("    ~;,   ~*$:$$;-~--,,,~;,")
        print("    :!.    ~=;$#:,,-,.--~;;")
        print("   .*=  .  -:!##:-,...,:;;!,")
        print("   ,:*   ~,*###$!:....,;=!!-")
        print("   :!; , !*=#$$*;~-,,-:*=*!;.")
        print("   !=~ -*=;=$*$==$=*!!*!**!;: .")
        print("  --;-.,$$!=$$=::$=$$##$=*;;;;;!.")
        print("  ;~;*:,#$*##$:-,-,,-;=$$!!!;~:*~")
        print(" ,;~;*-~#$=$#$!::,,!=*;*;.~*!!**$:")
        print(" ,;:*=:~#=!$##=;~-====$##  !***!$$-")
        print("  !*=$=:$==$#$=*!#*==$$##..!=$=;==;")
        print("  ~=###*;::;=;!=#$==$=$##. :$$=*!$=:")

    elif mob['name'] == '디아복로':
        print("#@###$=;*$####$$#@@#######$*=#$$=;~*=$#=*$########@@@####@#$=$#@@@")
        print("######@$*;*###$$#@@######===*=$=**:~!====!=$=$###$#@@#####@#:$#@@@")
        print("#######$=$#$$$$####$$*;!:;!;$$;!!~~;**==;*;;*!=$$$#@@@##$#@##@@@@@")
        print("$#####@####$$$##$===!:~:;~:!$=**;--~*==*;*~;!;!=$$$#@@##$##@@@@@@@")
        print("$#####@##$$$$$#=*=!:=;~,~-~!~!=*~-.:*=*=**~;::;**=$$###$$$#@@@@@##")
        print("$#######$==$$$**=*==!!,,--~;,~!!-,.-;*!**;::-~!===$$==##$$$#@@@@$$")
        print("##$$$##$==$$***=!$*=!;.-,,,;:;::,.,,~;!;=:----;*==$*$===$#$$$@@@##")
        print("####$##=*=====$!*;;;~:.--.,;!!!~., .~;;**-,---;:;!***====$$$$#@###")
        print("######$****==$**;~*=$=*;*;,~;*!:....~!**:,:*;!$#=*!!**=!===$=$@###")
        print("######=!!$$=*==~=#@##$$*=!-.-;!~....:**~--*=*$#@@@#=!===!=$===@###")
        print("######=!=$$==*!$##@##$$=$*;- .-~-. ,:~-,:!===###@@@@#**!*=====####")
        print("#####$!*====;$##@@@@##$=$=::,..~-,,--,,-;*=$$#@@@@@@@@$***;*$=####")
        print("#$=$$$!=$==*$##@##$=***$##:;*~...-~-,.-!*!##@@@@@@@@@@@#*=!;!=$@@@")
        print("#$$$=;=$$=!$####$=*!!**==#!-*;- .,,.--:*~;##@@@@##@@@@@@#!=!;!!$@#")
        print("$==**;$$$=$###$$=*!**====$*.-!;~ -,.-!*~,!##@@@@@@@@@@@##@=$*!;==$")
        print("====;*$$=$###=*===*=*=$$##*-.~:;:-,;!!~-,*$@@@@@@@@@@@@#@@=$$===#$")
        print("**!!;*$$$$@$=*======$$###$=**=:--, ~~;*$=*$#@@@@@@@@@@@@@@#$#$==$=")
        print("=*!*;!!**$#=*==$$$$$######=$=$!~~,.;-!#$$=$@@@@@@@@@@@@###$$$=*$==")
        print("$=*=!:!*$$$=**$$$$########$#=$=;:::;!=#$$$#@@@@@@@@@@@@##$*===$@$*")
        print("$=$$!;****=====$$$$#@####$$$*=$*:~~:=$==#$##@@@@@@@@###$====$##@$$")
        print("=#$*!$$=****===$=$##$$====$;;*!!!;**=*!$$$$=$####$$$$$$=$$#@@@@###")


def mob_rand():  # 몬스터 결정 함수
    mobRand = random.randint(1, 100)
    if mobRand <= 48:
        return 1
    if 48 < mobRand <= 78:
        return 2
    if 78 < mobRand <= 90:
        return 3
    if 90 < mobRand <= 95:
        return 4
    if 95 < mobRand <= 97:
        return 5
    if 97 < mobRand <= 99:
        return 6
    if mobRand == 100:
        return 7


def clear():  # 단순 화면 클리어 용도 : 노도현
    for i in range(1, 30):
        print()


def battle(player):  # 캐릭터,몹 정보 인자로 가져옴 : 노도현
    mobSpin = mob_rand()  # 몹 결정함수 호출
    alixTurn = 0  # 엘릭서 지속시간
    turn = 1  # 전투 턴 체크
    mob = mob_info(mobSpin)  # 몹 함수에서 결정함수를 인자로 보내어 몬스터 정보 받아옴
    img(mob)  # 몹 이미지
    while 1:
        run = random.randrange(0, 10)  # 도주확률
        print("---" * 40)
        print("---" * 40)
        print("🧭:\033[31m%d턴\033[0m" % turn)
        print(
            "초코의용군🤺\n⚔️ \033[32m%d ~ %d\t🤍 \033[33m%d / %d\t🧴 \033[34m%d개\t🏺 \033[35m%d개\033[0m"
            % (player['minDmg'] * (1 + player['winCnt'] * 0.05), player['maxDmg'] * (1 + player['winCnt'] * 0.05),
               player['hp'], player['maxHp'], player['potion'], player['elixir']))  # 0:공격력 1:체력 2:포션수 3:엘릭서 수
        print(mob['name'], "👾\n\033[32m⚔️ %d ~ %d\t🖤 \033[33m%d / %d\033[0m"
              % (mob['minDmg'], mob['maxDmg'], mob['hp'], mob['maxHp']))  # 0:공격력 1:체력
        if alixTurn >= 1:
            print("\033[0;35m남은 엘릭서 턴: %d" % alixTurn)  # 남은 엘릭서 턴 존재시 공지

        select = input("\033[0m1. \033[0;31m전투  \033[0m2. \033[0;34m아이템  \033[0m3. \033[0;37m도주\n\033[0m")
        print("---" * 40)

        if select == '1':
            playerDmg = random.randint(player['minDmg'], player['maxDmg']) * (
                    1 + player['winCnt'] * 0.05)  # 플레이어 대미지 산출
            mob['hp'] -= playerDmg
            print("⚔\033[0;31m플레이어의 공격\033[0m⚔")
            print("⚔️\033[0;32m%d데미지!\t\033[0;31m몹 \033[0;33m남은체력 💔%d\033[0m" % (playerDmg, mob['hp']))

        elif select == '2':
            clear()
            select2 = int(input("1. 회복  2. 엘릭서  3. 뒤로가기"))
            if select2 == 1 and player['potion'] == 0:
                print("❌\033[34m포션부족❌\033[0m")
            if select2 == 1 and player['potion'] >= 1:
                print("🩸\033[33m풀회복🩸\033[0m")
                player['hp'] = player['maxHp']  # 체크한 최대 hp를 현재 hp에 적용
                player['potion'] -= 1  # 포션 수 감소
            if select2 == 2 and player['elixir'] == 0:
                print("❌\033[35m엘릭서 부족❌\033[0m")
            if select2 == 2 and player['elixir'] >= 1:
                print("🍷\033[35m엘릭서 사용🍷\033[0m")
                alixTurn += 10  # 엘릭서 턴 10 증가
                player['elixir'] -= 1  # 엘릭서 수 감소
            continue

        elif select == '3' and run >= 2:
            print("도주성공")
            win = 0
            return player, win

        elif select == '3' and run < 2:
            print("도주 실패")

        else:  # 숫자 오입력 방지
            continue

        if mob['hp'] <= 0:
            print("🎉\033[32m처치완료🎉\033[0m")  # 포션 증가
            player['hp'] = player['maxHp']  # 전투 종료 후 hp값 원상복구
            if mob['name'] == '디아복로':
                print("🎉\033[32m디아복로를 물리쳤다!🎉\033[0m")
                win = 2
            else:
                win = 1
            return player, win

        print("---" * 40)
        if alixTurn == 0:  # 엘릭서 턴이 없을때 몬스터 공격
            mobDmg = random.randint(mob['minDmg'], mob['maxDmg'])  # 몹 대미지 산출
            player['hp'] -= mobDmg  # 캐릭터 체력을 몹 공격려만큼 감소
            print("⚔\033[0;31m몹의 공격\033[0m⚔")
            print("⚔️\033[0;32m%d데미지!\t\033[0;31m플레이어 \033[0;33m남은체력 💔%d\033[0m" % (mobDmg, player['hp']))
        if alixTurn >= 1:  # 엘릭서 턴 존재시 몹공격x 구문출력
            print("👾\033[0;30m몹의 공격")
            print(
                "🛡\033[31m엘\033[0;37m\033[32m릭\033[0;37m\033[33m서\033[0;37m \033[34m무\033[0;37m\033[35m적!🛡\033[0m")
            alixTurn -= 1  # 엘릭서 턴 감소

        if player['hp'] <= 0:  # 플레이어 hp가 0일때
            print("💀사망💀")
            print()
            print("⛈GAME OVER⛈")
            win = 3
            return player, win

        turn += 1  # 턴 증가


# 맵 : 이여름
# 표층 맵
# 기본 타일 : 0
# 플레이어 : 11
# 시야 : 12
# 시야에 몬스터나 아이템이 있을 때는 이벤트 함수와 대조하여 출력

# 이벤트 맵
# 몹 : 1
# 아이템 : 2
# 포탈up : 3
# 포탈down : 4

# 랜덤 좌표 반환 (행, 열) --- (col, row)
def random_point(width: int, height: int):
    col = random.randrange(height)
    row = random.randrange(width)
    return col, row


# 플레이어 위치를 제외한 곳의 랜덤 좌표 반환 (맵, 플레이어 시작 위치) --- (col, row)
def event_point(eventMap: list, startPoint: tuple = (1, 1)):
    while True:
        eventPoint = random_point(len(eventMap), len(eventMap[0]))
        if eventPoint != startPoint:
            return eventPoint


# 맵 생성(가로 크기, 세로 크기, 기본 타일) --- map
def map_create(width: int, height: int, tile=0):
    map = []
    temp = []
    for i in range(height):
        temp.append(tile)
    for i in range(width):
        map.append(temp[:])
    return map


# 이벤트맵 생성 (이벤트맵, 포탈 좌표 리스트, 층 - 기본값 1) --- eventMap
def floor_create(eventMap: list, portalPoint: list, floor: int = 1):
    # 층에 따라 up, down 포탈 삽입
    if floor == 1:
        eventMap = map_mark_append(eventMap, portalPoint[0], 3)
    elif floor == 2:
        eventMap = map_mark_append(eventMap, portalPoint[0], 4)
        eventMap = map_mark_append(eventMap, portalPoint[1], 3)
    elif floor == 3:
        eventMap = map_mark_append(eventMap, portalPoint[1], 4)
    return eventMap


# 좌표 리스트 생성(콘솔 맵, 생성할 수, 플레이어 시작 위치) --- eventPointList
def event_list_create(consolMap: list, num: int, startPoint: tuple = (1, 1)):
    eventPointList = []
    while len(eventPointList) < num:
        temp = event_point(consolMap, startPoint)
        if temp not in eventPointList:
            eventPointList.append(temp)
    return eventPointList


# 몬스터 배치 (이벤트맵, 몬스터 수) --- [이벤트 맵]
def monster_create(eventMap: list, enemy: int):
    count = 0
    while count <= enemy:
        monsPoint = random_point(len(eventMap[0]), len(eventMap))
        col = monsPoint[0]
        row = monsPoint[1]
        if eventMap[col][row] == 0:
            eventMap[col][row] = 1  # 몬스터 식별번호
            count += 1
    return eventMap


# 아이템 배치 (이벤트맵, 아이템 좌표 리스트) --- itemMap
def item_create(eventMap: list, itemPoint: list):
    itemMap = copy.deepcopy(eventMap)
    for i in range(len(itemPoint)):
        # 맵에 아이템 삽입
        itemMap = map_mark_append(itemMap, itemPoint[i], 2)
    return itemMap


# 좌표에 mark 추가 (맵, 좌표, 마크) --- map
def map_mark_append(map: list, coordinates: tuple, mark):
    col = coordinates[0]
    row = coordinates[1]
    map[col][row] = mark
    return map


# mark의 좌표를 튜플 반환 (맵, 마크) --- (col, row)
def map_mark_coordinates(map: list, mark):
    for col in range(len(map)):
        for row in range(len(map[col])):
            if map[col][row] == mark:
                return col, row


# 플레이어의 좌표 삽입 (맵, 좌표) --- 맵
def map_player_append(map: list, coordinates: tuple):
    col = coordinates[0]
    row = coordinates[1]
    map[col][row] = 11
    return map


# 플레이어의 좌표 튜플 반환 (맵) --- (col, row)
def map_player_coordinates(map: list):
    for col in range(len(map)):
        for row in range(len(map[col])):
            if map[col][row] == 11:
                return col, row


# 플레이어 주위 3*3 시야 삽입 (맵, 플레이어 좌표) --- 맵
def map_player_sight(map: list, player: tuple):
    # 플레이어의 열, 행 좌표
    plCol = player[0]
    plRow = player[1]
    # 시야의 범위를 지정 :
    # 시작 열,행 그리고 끝나는 열,행이 list의 범위를 넘지 않도록 삼항연산자 사용
    sightCol = (plCol - 1) if (plCol - 1) > 0 else 0
    sightRow = (plRow - 1) if (plRow - 1) > 0 else 0
    sightCEnd = plCol if (plCol + 1) >= len(map) else (plCol + 1)
    sightREnd = plRow if (plRow + 1) >= len(map[0]) else (plRow + 1)

    # 시야 삽입
    for col in range(sightCol, sightCEnd + 1):
        for row in range(sightRow, sightREnd + 1):
            if map[col][row] != 11:
                map[col][row] = 12
    return map


# 시야 제거 (맵) --- map
def sight_del(map: list):
    for col in range(len(map)):
        for row in range(len(map[col])):
            if map[col][row] == 12:
                map[col][row] = 10
    return map


# 플레이어 좌표 이동(맵, 기존의 좌표, 이동할 좌표) --- map
def player_move(map: list, prePoint: tuple, postPoint: tuple):
    # 플레이어 기존 좌표
    preCol = prePoint[0]
    preRow = prePoint[1]

    # 이동 후 좌표
    postCol = postPoint[0]
    postRow = postPoint[1]

    # 기존 좌표를 기본타일로 변경
    map[preCol][preRow] = 10
    # 새 좌표를 플레이어 마크로 변경
    map[postCol][postRow] = 11
    return map


# 플레이어 이동 제어(맵, 플레이어 좌표) --- map, True / False
def map_player_move(map: list, player: tuple):
    # 움직이는 방향을 할당할 변수
    moveCol = 0
    moveRow = 0
    # 플레이어 좌표의 열과 행
    plCol = player[0]
    plRow = player[1]

    # 키입력을 받는 부분. 연속 눌림을 방지하기 위해 time.sleep(0.3)
    key = keyboard.read_key()
    time.sleep(0.3)
    # 플레이어 위치가 맵의 제일 끝일 경우 움직이지 않는다
    if key == 'right':
        if plRow == len(map[0]) - 1:
            return [map, False]
        else:
            moveRow = 1
    elif key == 'up':
        if plCol == 0:
            return [map, False]
        else:
            moveCol = -1
    elif key == 'left':
        if plRow == 0:
            return [map, False]
        else:
            moveRow = -1
    elif key == 'down':
        if plCol == len(map) - 1:
            return [map, False]
        else:
            moveCol = 1
    else:
        return [map, False]

    # 플레이어가 이동할 좌표
    plCol = player[0] + moveCol if player[0] + moveCol < len(map) else (len(map) - 1)
    plRow = player[1] + moveRow if player[1] + moveRow < len(map[0]) else (len(map[0]) - 1)
    # 좌표 이동, 시야 제거 함수 호출
    sight_del(player_move(map, player, (plCol, plRow)))
    return [map, True]


# 맵을 콘솔에 출력 (표층맵, 이벤트맵) --- map
def map_view(map: list, event: list):
    clear()
    frame = '⬜'
    frameEdge = '💮'
    print(frameEdge + frame * len(map[0]) + frameEdge)
    for col in range(len(map)):
        print(frame, end='')
        for row in range(len(map[col])):
            if map[col][row] == 12:
                # 시야 범위의 이벤트 맵을 조회하여 출력 제어
                if event[col][row] == 1:  # 몬스터
                    print('💀', end='')
                elif event[col][row] == 2:  # 아이템
                    print('🧊', end='')
                elif event[col][row] == 3:  # up 포탈
                    print('💫', end='')
                elif event[col][row] == 4:  # down 포탈
                    print('🕳', end='')
                else:  # 시야
                    print('⬛', end='')  # 시야 어둡게
                    # print('☀', end='')            # 시야 밝게

            elif map[col][row] == 11:  # 플레이어 위치
                print('⚔️', end='')
            else:  # 기본 타일
                print('⬛', end='')
        print(frame)
    print(frameEdge + frame * len(map[0]) + frameEdge)


# 숫자맵 확인용 테스트 함수
def event_view(map: list):
    for col in map:
        print(col)


# ----------------------------------------------------------------------------------------------------------------------
# 맵 통합
def main(width: int, height: int):
    enemy = 6  # 몬스터 수
    itemNum = 5  # 아이템 수
    startPoint = (1, 1)  # 플레이어 시작 위치
    numOfSteps = 0  # 걸음 수
    floor = 1  # 현재 층
    player = player_create()  # 플레이어

    # 맵생성
    consolMap = map_create(width, height)  # 표층 맵
    eventBasic = copy.deepcopy(consolMap)  # 이벤트 기본 맵

    # 층이 변경되면 > 포탈, 플레이어 좌표를 제외하고 이벤트 맵을 층에 맞게 새로 생성한다.
    # 이동 함수를 실행하다가 층이 변경되면 플레이어 좌표를 리턴, 이벤트 맵 새로 불러오기

    # 포탈, 아이템 좌표 생성
    portalPoint = event_list_create(consolMap, 2, startPoint)
    # print('포탈 좌표 1-2 : %s, 2-3: %s' % (portalPoint[0], portalPoint[1]))
    itemPoint = event_list_create(consolMap, itemNum, startPoint)
    # print('아이템 좌표 : %s' % itemPoint[:])

    # 이벤트 맵에 아이템좌표 추가하는 식으로
    # 해당 좌표 아이템 먹으면 리스트에서 그 값을 삭제하고 갱신

    # 모든 층의 이벤트 맵 생성
    eventMap = {1: floor_create(copy.deepcopy(eventBasic), portalPoint, 1),
                2: floor_create(copy.deepcopy(eventBasic), portalPoint, 2),
                3: floor_create(copy.deepcopy(eventBasic), portalPoint, 3)}

    # 현재의 맵 지정, 아이템 배치
    nowEvent = item_create(eventMap[floor], itemPoint)
    # event_view(nowEvent)
    print('%s 층 탐험 시작' % floor)

    # 플레이어 시작 좌표 및 시야 설정
    consolMap = map_player_sight(map_player_append(consolMap, startPoint), startPoint)

    # 기본 이벤트맵을 복사해 몬스터 추가
    nowEvent = monster_create(copy.deepcopy(nowEvent), enemy)
    map_view(consolMap, nowEvent)

    # 이동
    while True:
        # 키 값에 따라 이동 함수를 실행
        time.sleep(0.3)
        # *좌표함수를 호출해 플레이어의 좌표를 반환 >
        # 맵과 플레이어 좌표를 *이동함수에 전달해 이동 >
        # *반환값(map, True or False)을 moveCheck에 할당
        moveCheck = map_player_move(consolMap, map_player_coordinates(consolMap))
        consolMap = moveCheck[0]
        # 맵을 이동 후로 갱신
        consolMap = map_player_sight(consolMap, map_player_coordinates(consolMap))
        # *좌표함수를 호출해 플레이어의 좌표를 반환 >
        # 맵과 플레이어 좌표를 *시야함수에 전달해 시야 추가 > *반환값을 맵에 할당

        # 이동했을 때 콘솔 출력, 발걸음 증가, 플레이어의 좌표를 조회
        if moveCheck[1]:
            map_view(consolMap, nowEvent)
            numOfSteps += 1
            playerPoint = map_player_coordinates(consolMap)

            # 플레이어 좌표를 이벤트맵에서 조회해서 1이면 몬스터 2는 아이템 3, 4는 포탈
            if nowEvent[playerPoint[0]][playerPoint[1]] == 1:
                # 전투 이벤트 연결부
                player, win = battle(player)
                if win == 1:
                    player = level_up(player)
                    # player['winCnt'] += 1
                    # player['maxHp'] = round(player['maxHp'] * 1.05)
                    # player['hp'] = player['maxHp']
                    player = item_drop(player, win)
                    # if random.randint(1, 100) <= 50:
                    #     if random.randint(1, 1000) <= 5:
                    #         player['elixir'] += 1
                    #     else:
                    #         player['potion'] += 1
                elif win == 2 or win == 3:
                    return
                # 승리 시 몬스터 제거
                nowEvent[playerPoint[0]][playerPoint[1]] = 0
            elif nowEvent[playerPoint[0]][playerPoint[1]] == 2:
                # 아이템 획득, 타일을 기본 타일로
                print('포션을 주웠습니다.')
                player['potion'] += 1
                print(f"현재 보유 중인 포션: {player['potion']} 개")
                # 아이템 좌표 리스트에서 좌표 제거
                itemPoint.remove(playerPoint)
                # 맵의 아이템 갱신
                nowEvent = item_create(eventMap[floor], itemPoint)
                # print('아이템 좌표 : %s' % itemPoint[:])
                # event_view(nowEvent)
            elif nowEvent[playerPoint[0]][playerPoint[1]] == 3:
                # up 포탈로 이벤트 맵 갱신, 발걸음 수 리셋
                print('위층으로 올라갑니다.')
                floor += 1
                nowEvent = eventMap[floor]
                numOfSteps = 0
                print('%s 층 탐험 시작' % floor)
            elif nowEvent[playerPoint[0]][playerPoint[1]] == 4:
                # down 포탈로 이벤트 맵 갱신, 발걸음 수 리셋
                print('아래층으로 내려갑니다.')
                floor -= 1
                nowEvent = eventMap[floor]
                numOfSteps = 0
                print('%s 층 탐험 시작' % floor)

            # 이동 중 우연히 아이템 획득
            fortune_item = lambda x: True if x <= 1 else False
            if fortune_item(random.randrange(100)):
                print('숨겨진 포션을 주웠습니다.')
                player['potion'] += 1
                print(f"현재 보유 중인 포션: {player['potion']} 개")

            # 3걸음마다 이벤트맵 몬스터 위치 재생성
            if numOfSteps % 3 == 0:
                nowEvent = item_create(eventMap[floor], itemPoint)
                nowEvent = monster_create(copy.deepcopy(nowEvent), enemy)


# 타이틀 출력 : 류가미
def title_view():
    title = 'Dungeon Master Choco'
    print("\t\033[96m⚔️┌──────────────────────────────────────────────────────┐⚔️")
    print("\t\033[93m👿│{0:·^54}│👿".format(''))
    print("\t\033[96m⚔️│{0:^54}│⚔️".format(title))
    print("\t\033[93m👿│{0:^54}│👿".format('▼▼'))
    print("\t\033[96m⚔️│{0:^54}│⚔️".format('▼▼'))
    print("\t\033[93m👿│{0:^54}│👿".format('▽▽'))
    print("\t\033[96m⚔️│{0:^54}│⚔️".format(':: Save the Coding Village ::'))
    print("\t\033[93m👿│{0:·^54}│👿".format("Let's Go!"))
    print("\t\033[96m⚔️└──────────────────────────────────────────────────────┘⚔️\033[0m")


title_view()
time.sleep(3)
main(15, 15)

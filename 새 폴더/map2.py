import random
import keyboard as keyboard
import time

class mapinfo:
    def __init__(self):
        self.rows = 16
        self.cols = 16
    def maping(self,):                                       #맵 기조 배열 생성
        return [[0 for j in range(self.cols)] for i in range(self.rows)]
    def rand(self):                                                   #배열내 랜덤좌표값
        randcol = random.randrange(0, 15)
        randrow = random.randrange(0, 15)
        return randcol, randrow
    def rand2(self):                                                  #1~100까지 랜덤값
        return random.randrange(1, 101)
    def mapimg(self,map):                                             #심층 정보 토대로 콘솔 맵 출력
        for i in range(0,15):
            for j in range(0,15):
                if (map[i][j] == 0 or map[i][j]==10 or map[i][j]==11):
                    print("\033[37;47m⬜\033[0;38m",end="")
                if (map[i][j] == 1):
                    print("🤺",end="")
                if (map[i][j] == 2):
                    print("⬛",end="")
                if (map[i][j] == 3):
                    print("👾",end="")
                if (map[i][j] == 4):
                    print("🏴󠁧󠁢󠁷󠁬󠁳󠁿",end="")
            print("")
    def sight(self,map,col,row):                                       #시야
        for i in range (-1,2):
            for j in range (-1,2):
                if i==0 and j==0:
                    continue
                if col > 0 or col < 14 or row > 0 or row < 14:
                    if map[col+i][row+j] == 10:
                        map[col+i][row+j] = 3
                    elif map[col+i][row+j] == 11:
                        map[col+i][row+j] = 4
                    else:
                        map[col+i][row+j] = 2

def battle():
    for i in range(0,10):                                               #임시배틀함수
        return int(input())

def map():                                                              #맵총괄함수
    col=0
    row=0
    step=0
    colrow = []
    floor = 1
    floorcnt=1
    battlecnt=0
    win=1
    portcol=portrow=0
    while (1):
        dummy = mapinfo()                                               #클래스 사용을 위해 더미변수에 담음
        map = dummy.maping()
        potionrand=dummy.rand2()                                        #rand2클래스에서 랜덤값 받아옴

        for j in range (0,16):                                          #오류있어서 안보이는 16번째줄 배열만듬
            map[j][15]=99

        if potionrand<=4:
            print("이동중 포션 드랍")

        if(step%3==0):                                 #몬스터 갱신
            print("갱신")
            colrow = []
            for i in range(0,21):
                randcol,randrow=dummy.rand()
                colrow.append(randcol)
                colrow.append(randrow)

        for i in range (0,39,2):
            map[colrow[i]][colrow[i+1]] = 10                            #몬스터 위장
        if floor<5:
            if battlecnt/10==1 or step==0:
                portcol,portrow=dummy.rand()
                battlecnt=0
            map[portcol][portrow] = 11                        #포탈 위장

        if floorcnt==1:                                                 #층오름 변수가 1이되면 유저위치를 재배치 한 뒤 0으로변경
            col,row=dummy.rand()
            floorcnt=0
        map[col][row]=1

        print("발걸음수",step)
        print("%d층"%floor)
        print("%d회 전투함"%battlecnt)

        dummy.sight(map,col,row)                                        #시야
        dummy.mapimg(map)                                               #맵 이미지 출력,인자를 위에서 받은 map을 넣어줌

        select = keyboard.read_key()                                    #방향키 입력받음
        time.sleep(0.3)
        if select=='left':
            if (row < 1):
                continue
            else:
                map[col][row] = 0
                row-=1
                map[col][row-1] = 1
        elif select == 'down':
            if (col > 13):
                continue
            else:
                map[col][row] = 0
                col+=1
                map[col+1][row] = 1
        elif select == 'right':
            if (row > 13):
                continue
            else:
                map[col][row] = 0
                row+=1
                map[col][row+1] = 1
        elif select == 'up':
            if (col < 1):
                continue
            else:
                map[col][row] = 0
                col-=1
                map[col-1][row] = 1

        step+=1                                                            #발걸음수 증가

        if map[col][row] == 3:                                             #몬스터 만나면 전투
            battlecnt+=1
            battle()
            if win==1:
                for i in range(0, 39, 2):
                    if colrow[i]==col and colrow[i+1]==row:
                        colrow[i]=15
                        colrow[i+1]=15

        elif map[col][row] == 4:                                           #포탈 만나면 다음층이동,발걸음,전투카운트 초기화
            floor+=1
            floorcnt=1
            battlecnt=0
            step=0
map()

import pygame
import sys
from pygame.locals import QUIT
import random
import time

# 오늘 할 일
# 1. 장애물 추가
# 2. 페어리 기능 구현
# 3. 밤 배경으로 바뀌면 느려지는 버그 수정 (버그가 아니라 의도한 기능으로)
# 4. 캐릭터 클래스화
# 5. 배경도 클래스화?
# 6. 아이템 추가
# 7. 보스도 추가? 이건 에바인가

# 게임 초기화
pygame.init()

# 게임 창 설정
Height = 900
Width = 1080
pygame.display.set_caption("달려라 초코의용군")


# 몬스터 클래스
class Monster:
    def slime(self):
        slime = pygame.image.load("source/slime.png")
        x = Width
        y = Height - slime.get_size()[1]
        return slime, x, y

    def fly(self):
        fly = pygame.image.load("source/fly.png")
        x = Width
        y = 200
        return fly, x, y

    def metal(self):
        metal = pygame.image.load("source/metal.png")
        metal_x = Width
        metal_y = 500
        return metal, metal_x, metal_y


# 장애물 클래스
class Obs:
    def spike(self):
        spike = pygame.image.load("source/spike.png")
        spike_x = Width
        spike_y = Height - spike.get_size()[1]
        return spike, spike_x, spike_y

    def elder(self):
        elder = pygame.image.load("source/elder.png")
        elder_x = Width
        elder_y = 0
        return elder, elder_x, elder_y

    def shield_fiary(self):
        sh = pygame.image.load("source/shied_fairy.png")
        sh_x = Width
        sh_y = Height - 110
        return sh, sh_x, sh_y

    def fire(self):
        fire = pygame.image.load("source/fire.png")
        fire_x = Width
        fire_y = 400
        return fire, fire_x, fire_y


# 아이템 클래스
class Item:
    def heart(self):
        heart = pygame.image.load("source/heart.png")
        heart_x = Width
        heart_y = 300
        return heart, heart_x, heart_y


# 페어리 클래스
class Fairy:
    def king(self):
        ki = pygame.image.load("source/king.png")
        ki_x = Width
        ki_y = 350
        return ki, ki_x, ki_y

    def med(self):
        gyu = pygame.image.load("source/potion.png")
        gyu_x = Width
        gyu_y = 350
        return gyu, gyu_x, gyu_y

    def bow(self):
        hyeon = pygame.image.load("source/bow.png")
        hyeon_x = Width
        hyeon_y = 350
        return hyeon, hyeon_x, hyeon_y


# 몬스터 생성 함수
def spawn_monster(sp: int):
    if sp == 1:
        return Monster().slime()
    elif sp == 2:
        return Monster().fly()
    elif sp == 3:
        return Monster().metal()


# 장애물 생성 함수
def spawn_obs(sp: int):
    if sp == 1:
        return Obs().spike()
    elif sp == 2:
        return Obs().elder()
    elif sp == 3:
        return Obs().shield_fiary()
    else:
        return Obs().fire()


# 아이템 생성 함수
def spawn_item(sp: int):
    if sp == 1:
        return Item().heart()


# 페어리 생성 함수
def spawn_fairy(sp: int):
    if sp == 1:
        return Fairy().king()
    elif sp == 2:
        return Fairy().med()
    else:
        return Fairy().bow()


# 게임 실행
def main():
    # 달리는 초코의용군
    choco1 = pygame.image.load("source/run1.png")
    choco2 = pygame.image.load("source/run2.png")
    # 슬라이딩하는 초코의용군
    slide = pygame.image.load("source/sliding.png")
    # 점프중인 초코의용군
    jump = pygame.image.load("source/jump.png")
    # 공격중인 초코의용군
    choco_attack = pygame.image.load("source/attack.png")
    # 데미지를 입은 초코의용군
    damaged = pygame.image.load("source/damaged.png")
    # 초코의용군의 높이
    choco_height = choco1.get_size()[1]
    # 초코의용군의 발 위치
    choco_bottom = Height - choco_height
    # 생명
    life = 3
    # 초코의용군의 x값
    choco_x = 100
    # 초코의용군의 y값
    choco_y = choco_bottom
    # 첨프했을 때의 y값
    jump_height = 0
    # 점프의 최대 y값
    jump_top = 400
    # 점프하는 상태
    jumping = False
    # 바닥에 붙어있지 않은 상태
    not_bottom = False
    # slide의 y값
    slide_y = Height - slide.get_size()[1]
    # 점프한 횟수
    jumped = 0
    # 슬라이딩 상태의 표현
    sliding = False
    # 공격상태
    attacking = False
    # 공격 시간
    attack_time = 0
    # 점수
    score = 0
    # 최종 스코어
    total = 0

    # 낮 배경
    back = pygame.image.load("source/back.png")
    back2 = pygame.image.load("source/back.png")

    # 밤 배경
    back_night = pygame.image.load("source/back_night.png")
    back_night2 = pygame.image.load("source/back_night.png")

    # 배경의 x값
    back_x = 0
    back2_x = back.get_size()[0]

    # 플레이어의 공격 범위
    slash = pygame.image.load("source/slash.png")
    buffed_slash = pygame.image.load("source/buffed_slash2.png")
    slash_x = choco_x + choco_attack.get_size()[0]

    # arrow 화살
    arrow = pygame.image.load("source/arrow.png")
    arrow_x = choco_x + 50 + choco1.get_size()[0]
    arrow_y = 0

    # 필드에 몬스터 존재 판단
    monster_spawned = False

    # 필드에 장애물 존재 판단
    obs_spawned = False

    # 필드에 아이템 존재 판단
    item_spawned = False

    # 필드에 페어리 존재 판단
    fairy_spawned = False
    fairy_num = 0

    # 배경 존재 판단
    back_spawned = False

    game = pygame.display.set_mode((Width, Height))
    frame = pygame.time.Clock()

    # 페어리 지속시간
    fairy_time = 0
    # 킹기테 버프
    king = False
    # 약범규 버프
    gyu = False
    # 보우현재 버프
    bow = False
    # 화살 존재 여부
    arrow_spawned = False

    run = True
    font = pygame.font.SysFont(None, 50)

    while run:

        # 점수에 따라 프레임 속도 증가
        if score < 5000:
            game.fill((255, 255, 255))
            game.blit(back, (back_x, 300))
            game.blit(back2, (back2_x, 300))
            frame.tick(80)
        elif 10000 <= score < 40000:
            game.fill((255, 255, 255))
            game.blit(back, (back_x, 300))
            game.blit(back2, (back2_x, 300))
            frame.tick(100)
        elif 80000 <= score < 320000:
            game.fill((255, 255, 255))
            game.blit(back, (back_x, 300))
            game.blit(back2, (back2_x, 300))
            frame.tick(130)
        elif 640000 <= score:
            game.fill((255, 255, 255))
            game.blit(back, (back_x, 300))
            game.blit(back2, (back2_x, 300))
            frame.tick(150)
        else:
            game.fill((127, 127, 127))
            game.blit(back_night, (back_x, 300))
            game.blit(back_night2, (back2_x, 300))
            frame.tick(60)

        back_x -= 10
        if back_x <= -back.get_size()[0]:
            back_x = Width
        back2_x -= 10
        if back2_x <= -back2.get_size()[0]:
            back2_x = Width

        # 점수, 생명의 폰트 및 위치 설정
        my_score = font.render("My Score : ", True, (0, 0, 0))
        now_score = font.render(str(score), True, (0, 0, 0))
        my_life = font.render("LIFE : ", True, (0, 0, 0))
        now_life = font.render(str(life), True, (0, 0, 0))
        score_x = my_score.get_size()[0]
        score_y = now_score.get_size()[1]
        life_x = my_life.get_size()[0]
        life_y = now_life.get_size()[1] + score_y

        # 플레이어의 입력
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    sliding = True
                if event.key == pygame.K_UP:
                    not_bottom = True
                    jumping = True
                    jumped += 1
                if event.key == pygame.K_SPACE:
                    attacking = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    sliding = False
                if event.key == pygame.K_UP:
                    jumping = False
                    jump_height = 0

        # 점프 높이가 최댓값인지 확인
        if jumping and jump_height >= jump_top:
            jumping = False
            jump_height = 0

        # 스코어가 짝수일 때에는 달리는 모션 1 출력
        if score % 2 == 0 and not sliding and not not_bottom:
            game.blit(choco1, (choco_x, choco_y))
            jumped = 0
            jump_height = 0
        # 스코어가 홀수일 때에는 달리는 모션 2 출력
        elif score % 2 != 0 and not sliding and not not_bottom:
            game.blit(choco2, (choco_x, choco_y))
            jumped = 0
        # 슬라이딩 출력
        elif sliding and not not_bottom:
            game.blit(slide, (choco_x, slide_y))
        # 점프 모션 출력
        elif jumping and not_bottom and jumped <= 2:
            choco_y -= 15
            jump_height += 15
            if not attacking:
                game.blit(jump, (choco_x, choco_y))
            else:
                game.blit(choco_attack, (choco_x, choco_y))
        # 점프 최대 높이에 도달하고 떨어질 때에도 점프 모션 출력
        elif not jumping and not_bottom or jumped > 2:
            if not attacking:
                game.blit(jump, (choco_x, choco_y))
            choco_y += 10
            if choco_y >= choco_bottom:
                not_bottom = False
                choco_y = choco_bottom
        # 공격 중일 때에는 공격 모션 출력 (일정 프레임이 지나면 모션 해제)
        if attacking:
            attack_time += 1
            game.blit(choco_attack, (choco_x, choco_y))
            if not gyu:
                game.blit(slash, (slash_x, choco_y))
            else:
                game.blit(buffed_slash, (slash_x, choco_y))
            if attack_time >= 10:
                attacking = False
                attack_time = 0

        # 점수와 생명 출력
        game.blit(now_score, (score_x, score_y))
        game.blit(my_score, (0, score_y))
        game.blit(now_life, (life_x, life_y))
        game.blit(my_life, (0, life_y))

        # 몬스터 스폰, 이동, 충돌 시 제거 및 생명 소모
        if not monster_spawned:
            spawn = random.randint(1, 3)
            monster, monster_x, monster_y = spawn_monster(spawn)
            monster_spawned = True
        else:
            game.blit(monster, (monster_x, monster_y))
            monster_x -= 10
            if monster_x <= 0 - monster.get_size()[0]:
                monster_spawned = False
            if choco_x - monster.get_size()[0] <= monster_x <= choco_x + choco1.get_size()[0] \
                    and choco_y - monster.get_size()[1] <= monster_y <= choco_y + choco1.get_size()[1]:
                if king:
                    monster_spawned = False
                else:
                    monster_spawned = False
                    life -= 1
                    game.blit(damaged, (choco_x, choco_y))
                    pygame.display.update()
                    time.sleep(0.1)
            elif slash_x - monster.get_size()[0] <= monster_x <= slash_x + slash.get_size()[0] \
                    and choco_y - monster.get_size()[1] <= monster_y <= choco_y + choco1.get_size()[1] \
                    and attacking and not gyu:
                monster_score = int(score / 20)
                print("%d점 획득" % monster_score)
                score += monster_score
                monster_spawned = False
            elif slash_x - monster.get_size()[0] <= monster_x <= slash_x + buffed_slash.get_size()[0] \
                    and choco_y - monster.get_size()[1] <= monster_y <= choco_y + choco1.get_size()[1] \
                    and attacking and gyu:
                monster_score = int(score / 20)
                print("%d점 획득" % monster_score)
                score += monster_score
                monster_spawned = False
            elif arrow_x - monster.get_size()[0] <= monster_x <= arrow_x + arrow.get_size()[0] \
                    and arrow_y - monster.get_size()[1] <= monster_y <= arrow_y:
                if bow:
                    monster_score = int(score / 20)
                    print("%d점 획득" % monster_score)
                    score += monster_score
                    monster_spawned = False

        # 장애물 스폰, 이동, 충돌 시 제거 및 생명 소모
        obs_spawn_check = random.randint(1, 100)
        if not obs_spawned:
            if obs_spawn_check <= 1:
                spawn = random.randint(1, 4)
                obs, obs_x, obs_y = spawn_obs(spawn)
                obs_spawned = True
        else:
            game.blit(obs, (obs_x, obs_y))
            obs_x -= 10
            if obs_x <= 0 - obs.get_size()[0]:
                obs_spawned = False
            if sliding and not not_bottom and not attacking:
                if choco_x - obs.get_size()[0] <= obs_x <= choco_x + slide.get_size()[0] \
                        and slide_y - obs.get_size()[1] <= obs_y <= slide_y + slide.get_size()[1]:
                    obs_spawned = False
                    if not king:
                        life -= 1
                        game.blit(damaged, (choco_x, choco_y))
                        pygame.display.update()
                        time.sleep(0.1)
            else:
                if choco_x - obs.get_size()[0] <= obs_x <= choco_x + choco1.get_size()[0] \
                        and choco_y - obs.get_size()[1] <= obs_y <= choco_y + choco1.get_size()[1]:
                    obs_spawned = False
                    if not king:
                        life -= 1
                        game.blit(damaged, (choco_x, choco_y))
                        pygame.display.update()
                        time.sleep(0.1)

        # 아이템 스폰, 이동, 충돌 시 제거 및 추가 효과
        item_spawn_check = random.randint(1, 500)
        if not item_spawned:
            if item_spawn_check <= 1:
                spawn = random.randint(1, 1)
                item, item_x, item_y = spawn_item(spawn)
                item_spawned = True
        else:
            game.blit(item, (item_x, item_y))
            item_x -= 10
            if item_x <= 0 - item.get_size()[0]:
                item_spawned = False
            if choco_x - item.get_size()[0] <= item_x <= choco_x + choco1.get_size()[0] \
                    and choco_y - item.get_size()[1] <= item_y <= choco_y + choco1.get_size()[1]:
                item_spawned = False
                life += 1
                if life >= 3:
                    life = 3

        # 페어리 스폰, 이동, 획득 시 제거 및 추가 효과
        fairy_spawn_check = random.randint(1, 500)
        if not fairy_spawned and not king and not gyu and not bow:
            if fairy_spawn_check <= 1:
                spawn = random.randint(1, 3)
                fairy, fairy_x, fairy_y = spawn_fairy(spawn)
                fairy_num = spawn
                fairy_spawned = True
        # 페어리 지속시간 계산 후 버프 종료
        elif fairy_spawned and (king or gyu or bow):
            fairy_time += 1
            fairy_x = choco_x - fairy.get_size()[0]
            fairy_y = choco_y
            game.blit(fairy, (fairy_x, fairy_y))
            if fairy_time > 1000:
                king = False
                gyu = False
                bow = False
                fairy_spawned = False
                fairy_time = 0
        else:
            game.blit(fairy, (fairy_x, fairy_y))
            fairy_x -= 10
            if fairy_x <= 0 - fairy.get_size()[0]:
                fairy_spawned = False
            if choco_x - fairy.get_size()[0] <= fairy_x <= choco_x + choco1.get_size()[0] \
                    and choco_y - fairy.get_size()[1] <= fairy_y <= choco_y + choco1.get_size()[1]:
                if fairy_num == 1:
                    king = True
                elif fairy_num == 2:
                    gyu = True
                else:
                    bow = True
                    arrow_y = 350

        # bow 버프 중 arrow 스폰
        if bow:
            if not arrow_spawned:
                arrow_x = choco_x + arrow.get_size()[0]
                arrow_y = choco_y + (choco1.get_size()[1] / 2)
                arrow_spawned = True
            else:
                game.blit(arrow, (arrow_x, arrow_y))
                arrow_x += 15
                if arrow_x >= Width - 10 \
                        or (monster_x - arrow.get_size()[0] <= arrow_x <= monster_x + arrow.get_size()[0]
                            and monster_y - arrow.get_size()[1] <= arrow_y <= monster_y + arrow.get_size()[1]):
                    arrow_spawned = False

        # 라이프 모두 소모 시 게임 종료
        if life <= 0:
            run = False

        score += 5

        # 게임 화면 업데이트
        pygame.display.update()

        # 점수를 저장
        total = score

    # 게임 오버 화면
    while not run:
        game.fill((255, 255, 255))
        retry = font.render("CONTINUE? PRESS  'r'", True, (0, 0, 0))
        game.blit(retry, (300, 400))
        my_score = font.render("Last Score : ", True, (0, 0, 0))
        now_score = font.render(str(total), True, (0, 0, 0))
        game.blit(now_score, (score_x, score_y))
        game.blit(my_score, (score_x - my_score.get_size()[0], score_y))

        # 게임 내용 초기화
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # 생명
                    life = 3
                    # 초코의용군의 x값
                    choco_x = 100
                    # 초코의용군의 y값
                    choco_y = choco_bottom
                    # 첨프했을 때의 y값
                    jump_height = 0
                    # 점프의 최대 y값
                    jump_top = 400
                    # 점프하는 상태
                    jumping = False
                    # 바닥에 붙어있지 않은 상태
                    not_bottom = False
                    # slide의 y값
                    slide_y = Height - slide.get_size()[1]
                    # 점프한 횟수
                    jumped = 0
                    # 슬라이딩 상태의 표현
                    sliding = False
                    # 킹기테 버프
                    king = False
                    # 약범규 버프
                    gyu = False
                    # 보우현재 버프
                    bow = False
                    # 공격상태
                    attacking = False
                    # 공격 시간
                    attack_time = 0
                    # 점수
                    score = 0
                    # 스피드
                    speed = 1
                    # 무적
                    no_enemy = False
                    # 무적 시간
                    no_enemy_time = 0
                    run = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        frame.tick(10)


while True:
    main()
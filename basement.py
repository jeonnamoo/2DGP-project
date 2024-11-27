import random

from pico2d import *

import game_framework
import game_world
import kitchen
from door import Door
from girl import Girl
from mop import Mop
from web import Web
from can import Can
from stain import Stain
from broom import Broom
from key import Key
from duster import Duster

image = None
web_list = []
can_list = []
stain_list = []

door = None
broom = None
mop = None
key = None
duster = None

door_x, door_y = 420, 770  # 문 위치
width, height = 1440, 960  # Yard 크기
mop_x, mop_y = 1100, 300
girl = None

#web 배치 범위 설정
web_x_min, web_x_max = 270, 1180
web_y_min, web_y_max = 210, 760

can_x_min, can_x_max = 270, 1180
can_y_min, can_y_max = 210, 760

stain_x_min, stain_x_max = 270, 1180
stain_y_min, stain_y_max = 210, 760



def init():
    global image, door, girl, mop,  web_list, can_list, stain_list
    image = load_image('basement.png')  # 배경 이미지 로드
    door = Door(width=32, height=32)  # 첫 번째 문 크기 설정

    # Mop 초기화
    mop = game_world.get_object_by_class(Mop)
    if not mop:  # 이미 존재하지 않는 경우에만 생성
        mop = Mop()
        game_world.add_object(mop, 1)
    mop.current_map = "basement"  # 현재 맵 설정
    mop.x, mop.y = 1100, 300  # 초기 위치

    # Girl 초기화
    girl = game_world.get_object_by_class(Girl)
    if not girl:
        girl = Girl()
        game_world.add_object(girl, 2)
    girl.x, girl.y = 420, 770  # 초기 위치





    for _ in range(10):
        x = random.randint(web_x_min, web_x_max)
        y = random.randint(web_y_min, web_y_max)
        web = Web()
        web_list.append((web,x,y))

    for _ in range(10):
        x = random.randint(can_x_min, can_x_max)
        y = random.randint(can_y_min, can_y_max)
        can = Can()
        can_list.append((can,x,y))

    for _ in range(10):
        x = random.randint(stain_x_min, stain_x_max)
        y = random.randint(stain_y_min, stain_y_max)
        stain = Stain()
        stain_list.append((stain,x,y))






def draw():
    global image, door,  mop
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door.draw(door_x, door_y)  # 문 그리기

    # 각 객체의 current_map을 기준으로 그리기
    mop.draw()

    for web, x, y in web_list:
        web.draw(x,y)

    for can, x, y in can_list:
        can.draw(x,y)

    for stain, x, y in stain_list:
        stain.draw(x,y)


    game_world.render()
    update_canvas()


def handle_events():
    global girl, door, mop, broom, key, duster
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            # 첫 번째 문 근처에서 눌렀을 경우
            distance1 = ((girl.x - door_x) ** 2 + (girl.y - door_y) ** 2) ** 0.5
            if distance1 <= 30:  # 문 근처(거리 30 이하)
                game_framework.change_mode(kitchen)

             # Girl과 Mop 사이의 거리 계산
            distance_to_mop = ((girl.x - mop.x) ** 2 + (girl.y - mop.y) ** 2) ** 0.5
            if distance_to_mop <= 30 and not mop.attached:
                mop.attach(girl)  # mop 부착
                if mop and mop.attached:
                    mop.detach()
                    mop.x, mop.y = 110, 300  # yard 초기 위치로 복귀


        else:
            if girl:
                girl.handle_event(event)


def update():
    global girl, mop
    if girl:  # girl 객체가 존재할 경우에만 실행
        girl.x = max(270, min(1180, girl.x))  # x축 이동 범위 제한
        girl.y = max(210, min(760, girl.y))  # y축 이동 범위 제한

    game_world.update()  # 다른 객체들도 업데이트



def pause(): pass

def resume(): pass

def finish():
    global image, door, web_list, can_list, stain_list, mop
    del image
    del door
    web_list.clear()
    can_list.clear()
    stain_list.clear()

    mop.current_map = None



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
from gage import Gage

image = None
web_list = []
can_list = []
stain_list = []
gage = None

door = None
broom = None
mop = None
key = None
duster = None
attached_object = None

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
    global image, door, girl, mop,  web_list, can_list, stain_list, gage
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

    if not gage:
        gage = Gage()
        game_world.add_object(gage, 3)  # UI 레이어에 추가

    if not web_list:
        for _ in range(10):
            x = random.randint(web_x_min, web_x_max)
            y = random.randint(web_y_min, web_y_max)
            web = Web(x, y)  # x, y 전달
            web_list.append((web, x, y))

    if not can_list:
        for _ in range(10):
            x = random.randint(can_x_min, can_x_max)
            y = random.randint(can_y_min, can_y_max)
            can = Can(x, y)
            can_list.append((can, x, y))

    if not stain_list:
        for _ in range(10):
            x = random.randint(stain_x_min, stain_x_max)
            y = random.randint(stain_y_min, stain_y_max)
            stain = Stain(x, y)  # x와 y 전달
            stain_list.append((stain, x, y))






def draw():
    global image, door,  mop, attached_object, gage
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door.draw(door_x, door_y)  # 문 그리기

    # 각 객체의 current_map을 기준으로 그리기
    mop.draw()  # 기존 mop 그리기
    if attached_object:  # 새로운 mop이 생성되었다면 그리기
        attached_object.draw()

    for web, x, y in web_list:
        web.draw()

    for can, x, y in can_list:
        can.draw()

    for stain, x, y in stain_list:
        stain.draw()

    if gage:
        gage.draw()  # gage 그리기

    game_world.render()
    update_canvas()


def handle_events():
    global girl, door, mop, can_list, stain_list, web_list, broom, duster
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            # Can과의 상호작용
            for can, x, y in can_list:
                distance_to_can = ((girl.x - can.x) ** 2 + (girl.y - can.y) ** 2) ** 0.5
                if isinstance(girl.item, Broom) and not can.removed and distance_to_can <= 30:
                    can.activate_trash()
                    return

            # Stain과의 상호작용
            for stain, x, y in stain_list:
                distance_to_stain = ((girl.x - stain.x) ** 2 + (girl.y - stain.y) ** 2) ** 0.5
                if isinstance(girl.item, Mop) and not stain.removed and distance_to_stain <= 30:
                    stain.activate_water()
                    return

            # Web과의 상호작용
            for web, x, y in web_list:
                distance_to_web = ((girl.x - web.x) ** 2 + (girl.y - web.y) ** 2) ** 0.5
                if isinstance(girl.item, Duster) and not web.removed and distance_to_web <= 30:
                    web.activate_dust()
                    return

            # Door 근처 거리 계산
            distance_to_door = ((girl.x - door_x) ** 2 + (girl.y - door_y) ** 2) ** 0.5
            if distance_to_door <= 30:
                door.play_sound()  # Door 사운드 재생
                game_framework.change_mode(kitchen)

            # Broom 근처 거리 계산
            distance_to_mop = ((girl.x - mop.x) ** 2 + (girl.y - mop.y) ** 2) ** 0.5
            if distance_to_mop <= 30:
                girl.set_item(mop)  # 새로운 Broom 부착

        else:
            if girl:
                girl.handle_event(event)



def update():
    global girl, gage
    if girl:  # girl 객체가 존재할 경우에만 실행
        girl.x = max(270, min(1180, girl.x))  # x축 이동 범위 제한
        girl.y = max(210, min(760, girl.y))  # y축 이동 범위 제한

    for can, x, y in can_list:
        can.update()  # Can 애니메이션 업데이트

    for stain, x, y in stain_list:
        stain.update()  # Stain 애니메이션 업데이트
    for web, x, y in web_list:
        web.update()

    if gage:
        game_framework.update_gage(gage)  # gage 상태 업데이트
        gage.update()



    game_world.update()  # 다른 객체들도 업데이트



def pause(): pass

def resume(): pass

def finish():
    global image, door,  mop
    del image
    del door


    mop.current_map = None
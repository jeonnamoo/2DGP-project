import random

from pico2d import *

import bedroom
import door
import game_framework
import game_world
import kitchen
import library
import yard
from door import Door
from girl import Girl
from web import Web
from can import Can
from stain import Stain
from broom import Broom
from duster import Duster
from mop import Mop
from key import Key
from gage import Gage

image = None
gage = None

web_list = []
can_list = []
stain_list = []
doors  = []

key_required = True

# 문 위치
door_positions = {
    'door1': (820, 160),
    'door2': (410, 160),
    'door3': (790, 800),
    'door4': (1290, 445),
}

width, height = 1440, 960  # Livingroom 크기
girl = None

# 마지막에 사용된 문과 이전 모드
last_used_door = None

#web 배치 범위 설정
web_x_min, web_x_max = 200, 1290
web_y_min, web_y_max = 150, 810

can_x_min, can_x_max = 200, 1290
can_y_min, can_y_max = 150, 810

stain_x_min, stain_x_max = 200, 1290
stain_y_min, stain_y_max = 150, 810



def init():
    global image, doors, girl, last_used_door, web_list, can_list, stain_list, broom, gage
    image = load_image('livingroom.png')  # 배경 이미지 로드

    if not doors:
        doors.extend([Door(), Door(), Door(), Door()])  # 문 생성

    girl = game_world.get_object_by_class(Girl)
    if not girl:
        girl = Girl()
        game_world.add_object(girl, 2)

    broom = game_world.get_object_by_class(Broom)
    if not broom:
        broom = Broom(width=32, height=32)
        game_world.add_object(broom, 1)

    broom.current_map = "livingroom"  # 현재 맵을 livingroom으로 설정

    # 마지막 사용된 문에 따라 초기 위치 설정
    if last_used_door and last_used_door in door_positions:
        girl.x, girl.y = door_positions[last_used_door]
    else:  # 기본 위치
        girl.x, girl.y = 820, 160

    if broom.attached:
        broom.x, broom.y = girl.x, girl.y  # broom 위치 동기화

    if not gage:
        gage = Gage()
        game_world.add_object(gage, 3)  # UI 레이어에 추가

    # 이미 생성된 web_list, can_list, stain_list를 재사용
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
    global image, doors,gage
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)

    for i, door in enumerate(doors):
        door.draw(*door_positions[f'door{i + 1}'])

    if gage:
        gage.draw()  # gage 그리기

    for web, x, y in web_list:
        web.draw()

    for can, x, y in can_list:
        can.draw()

    for stain, x, y in stain_list:
        stain.draw()



    # girl 및 부착된 물체 렌더링
    if girl:
        girl.draw()
        if girl.item:  # 부착된 아이템이 있을 경우 렌더링
            girl.item.draw()

    game_world.render()
    update_canvas()


def handle_events():
    global girl, can_list, stain_list, web_list, broom, duster, mop, last_used_door, key_required
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

            # Door와의 거리 계산
            for idx, (door, position) in enumerate(zip(doors, door_positions.values())):
                distance = ((girl.x - position[0]) ** 2 + (girl.y - position[1]) ** 2) ** 0.5
                if distance <= 30:
                    last_used_door = list(door_positions.keys())[idx]

                    # 잠긴 문 처리
                    if last_used_door == 'door4' and key_required:
                        if isinstance(girl.item, Key):  # 열쇠가 있는 경우
                            key_required = False  # 열쇠 필요 조건 해제
                            door.play_sound()  # 문 열리는 사운드
                            game_framework.change_mode(library)
                        else:
                            door.play_locked_sound()  # 잠긴 문 사운드
                            print("Key가 필요합니다!")
                    else:  # 잠기지 않은 문 처리
                        door.play_sound()
                        if last_used_door == 'door1':
                            game_framework.change_mode(yard)
                        elif last_used_door == 'door2':
                            game_framework.change_mode(kitchen)
                        elif last_used_door == 'door3':
                            game_framework.change_mode(bedroom)
                        elif last_used_door == 'door4':
                            game_framework.change_mode(library)
        else:
            if girl:
                girl.handle_event(event)


def update():
    global girl, broom, gage
    if girl:  # girl 객체가 존재할 경우
        girl.x = max(200, min(1290, girl.x))  # x축 이동 범위 제한
        girl.y = max(150, min(810, girl.y))  # y축 이동 범위 제한

    for can, x, y in can_list:
        can.update()  # Can 애니메이션 업데이트

    for stain, x, y in stain_list:
        stain.update()  # Stain 애니메이션 업데이트
    for web, x, y in web_list:
        web.update()


    if gage:
        game_framework.update_gage(gage)  # gage 상태 업데이트
        gage.update()



    game_world.update()  # 다른 객체 업데이트


def finish():
    global image, doors
    del image
    doors.clear()
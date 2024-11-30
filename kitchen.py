import random

from pico2d import *

import basement
import game_framework
import game_world
import livingroom
from door import Door
from girl import Girl
from web import Web
from can import Can
from stain import Stain
from broom import Broom
from duster import Duster
from mop import Mop
from gage import Gage

image = None
gage = None
web_list = []
can_list = []
stain_list = []
door1 = None
door2 = None
door1_x, door1_y = 803, 275  # 첫 번째 문 위치
door2_x, door2_y = 780, 750  # 두 번째 문 위치
width, height = 1440, 960  # Kitchen 크기
girl = None
last_door_used = None  # 마지막 사용된 문

web_x_min, web_x_max = 200, 1240
web_y_min, web_y_max = 150, 730

can_x_min, can_x_max = 200, 1240
can_y_min, can_y_max = 150, 730

stain_x_min, stain_x_max = 200, 1240
stain_y_min, stain_y_max = 150, 730

def init():
    global image, door1, door2, girl, last_door_used, web_list, can_list, stain_list, gage
    image = load_image('kitchen.png')  # 배경 이미지 로드
    door1 = Door(width=32, height=32)  # 첫 번째 문 크기 설정
    door2 = Door(width=32, height=32)  # 두 번째 문 크기 설정

    girl = game_world.get_object_by_class(Girl)  # 기존 girl 객체 가져오기
    if not girl:  # girl 객체가 없으면 새로 생성
        girl = Girl()
        game_world.add_object(girl, 2)



    # 마지막 사용된 문에 따라 초기 위치 설정
    if last_door_used == "door1":
        girl.x, girl.y = door1_x, door1_y
    elif last_door_used == "door2":
        girl.x, girl.y = door2_x, door2_y
    else:  # 기본 초기 위치
        girl.x, girl.y = 803, 275

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
    global image, door1, door2, gage
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door1.draw(door1_x, door1_y)  # 첫 번째 문 그리기
    door2.draw(door2_x, door2_y)  # 두 번째 문 그리기


    if gage:
        gage.draw()  # gage 그리기
    for web, x, y in web_list:
        web.draw()

    for can, x, y in can_list:
        can.draw()

    for stain, x, y in stain_list:
        stain.draw()

    if girl:
        girl.draw()
        if girl.item:  # 부착된 아이템이 있을 경우 렌더링
            girl.item.draw()


    game_world.render()
    update_canvas()

def handle_events():
    global girl, door1, door2, last_door_used, can_list, stain_list, web_list, broom, duster, mop
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
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

            # 첫 번째 문 근처에서 눌렀을 경우
            distance1 = ((girl.x - door1_x) ** 2 + (girl.y - door1_y) ** 2) ** 0.5
            if distance1 <= 30:  # 문 근처(거리 30 이하)
                last_door_used = "door1"
                game_framework.change_mode(livingroom)

            # 두 번째 문 근처에서 눌렀을 경우
            distance2 = ((girl.x - door2_x) ** 2 + (girl.y - door2_y) ** 2) ** 0.5
            if distance2 <= 30:  # 문 근처(거리 30 이하)
                last_door_used = "door2"
                game_framework.change_mode(basement)
        else:
            if girl:
                girl.handle_event(event)

def update():
    global girl, gage
    if girl:  # girl 객체가 존재할 경우에만 실행
        girl.x = max(200, min(1240, girl.x))  # x축 이동 범위 제한
        girl.y = max(150, min(730, girl.y))  # y축 이동 범위 제한
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
    global image, door1, door2
    del image
    del door1
    del door2


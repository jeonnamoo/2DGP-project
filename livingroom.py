import random

from pico2d import *

import bedroom
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

image = None

web_list = []
can_list = []
stain_list = []
doors  = []

# 문 위치
door_positions = {
    'door1': (820, 300),
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
    global image, doors, girl, last_used_door, web_list, can_list, stain_list, broom, broom_attached
    image = load_image('livingroom.png')  # 배경 이미지 로드
    doors = [Door(), Door(), Door(), Door()]  # 문 생성

    girl = game_world.get_object_by_class(Girl)
    if not girl:
        girl = Girl()
        game_world.add_object(girl, 2)

    broom = game_world.get_object_by_class(Broom)
    if not broom:
        broom = Broom(width=32, height=32)
        game_world.add_object(broom, 1)

    # 마지막 사용된 문에 따라 초기 위치 설정
    if last_used_door and last_used_door in door_positions:
        girl.x, girl.y = door_positions[last_used_door]
    else:  # 기본 위치
        girl.x, girl.y = 820, 300

    if broom.attached:
        broom.x, broom.y = girl.x, girl.y  # broom 위치 동기화

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
    global image, doors
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)
    for i, door in enumerate(doors):
        door.draw(*door_positions[f'door{i + 1}'])

    for web, x, y in web_list:
        web.draw(x,y)

    for can, x, y in can_list:
        can.draw(x,y)

    for stain, x, y in stain_list:
        stain.draw(x,y)


    game_world.render()
    update_canvas()

def handle_events():
    global girl, last_used_door
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            for door_name, position in door_positions.items():
                distance = ((girl.x - position[0]) ** 2 + (girl.y - position[1]) ** 2) ** 0.5
                if distance <= 30:
                    last_used_door = door_name
                    if door_name == 'door1':
                        game_framework.change_mode(yard)
                    elif door_name == 'door2':
                        game_framework.change_mode(kitchen)
                    elif door_name == 'door3':
                        game_framework.change_mode(bedroom)
                    elif door_name == 'door4':
                        game_framework.change_mode(library)
        else:
            if girl:
                girl.handle_event(event)

def update():
    global girl, broom, broom_attached
    if girl:
        girl.x = max(200, min(1290, girl.x))  # x축 이동 범위 제한
        girl.y = max(150, min(810, girl.y))  # y축 이동 범위 제한
    if game_framework.broom_attached:
        broom.x, broom.y = girl.x, girl.y
    game_world.update()

    game_world.update()

def finish():
    global image, doors, web_list, can_list, stain_list
    del image
    doors.clear()
    web_list.clear()
    can_list.clear()
    stain_list.clear()

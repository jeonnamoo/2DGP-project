import random

from pico2d import *

import game_framework
import game_world
import livingroom
from broom import Broom
from door import Door
from duster import Duster
from girl import Girl
from key import Key
from mop import Mop
from web import Web
from can import Can
from stain import Stain



image = None

web_list = []
can_list = []
stain_list = []

door = None
broom = None
mop = None
key = None
duster = None
door_x, door_y = 244, 248  # 문 위치
key_x, key_y = 1070, 570
width, height = 1440, 960  # Yard 크기
girl = None

#web 배치 범위 설정
web_x_min, web_x_max = 150, 1290
web_y_min, web_y_max = 250, 610

can_x_min, can_x_max = 150, 1290
can_y_min, can_y_max = 250, 610

stain_x_min, stain_x_max = 150, 1290
stain_y_min, stain_y_max = 250, 610


def init():
    global image, door, girl, key,duster, broom,  web_list, can_list, stain_list
    image = load_image('bedroom.png')  # 배경 이미지 로드
    door = Door(width=32, height=32)  # 첫 번째 문 크기 설정
    key = Key(width=32, height =32)


    girl = game_world.get_object_by_class(Girl)  # 기존 girl 객체 가져오기
    if not girl:  # girl 객체가 없으면 새로 생성
        girl = Girl()
        game_world.add_object(girl, 2)

    girl.x, girl.y = 244, 248  # 초기 위치

    # Key 객체 초기화
    key = game_world.get_object_by_class(Key)
    if not key:
        key = Key()  # Key 생성
        game_world.add_object(key, 1)
    key.current_map = "bedroom"  # 현재 맵 설정
    key.x, key.y = 1070, 570  # Key 초기 위치

    if not key.attached:
        key.x, key.y = 1070, 570  # broom 초기 위치

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
    global image, door, broom,  duster, key
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door.draw(door_x, door_y)  # 문 그리기

    # 각 객체의 current_map을 기준으로 그리기
    key.draw()

    for web, x, y in web_list:
        web.draw(x,y)

    for can, x, y in can_list:
        can.draw(x,y)

    for stain, x, y in stain_list:
        stain.draw(x,y)


    game_world.render()
    update_canvas()


def handle_events():
    global girl, door, broom, mop, duster, key
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
                game_framework.change_mode(livingroom)
            distance_to_key = ((girl.x - key.x) ** 2 + (girl.y - key.y) ** 2) ** 0.5
            if distance_to_key <= 30 and not key.attached:
                key.attach(girl)  # broom을 girl에 부착

                if key and key.attached:
                    key.detach()
                    key.x, key.y = 1070, 570  # yard 초기 위치로 복귀

        else:
            if girl:
                girl.handle_event(event)


def update():
    global girl
    if girl:  # girl 객체가 존재할 경우에만 실행
        girl.x = max(150, min(1290, girl.x))  # x축 이동 범위 제한
        girl.y = max(250, min(610, girl.y))  # y축 이동 범위 제한
    game_world.update()  # 다른 객체들도 업데이트


def pause(): pass


def resume(): pass


def finish():
    global image, door, web_list, can_list, stain_list, key
    del image
    del door
    web_list.clear()
    can_list.clear()
    stain_list.clear()

    key.current_map = None



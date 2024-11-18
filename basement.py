import random

from pico2d import *

import game_framework
import game_world
import kitchen
from door import Door
from girl import Girl
from mop import Mop
from web import Web

image = None
web_list = []
door = None
mop = None

door_x, door_y = 420, 770  # 문 위치
width, height = 1440, 960  # Yard 크기
mop_x, mop_y = 1100, 300
girl = None

#web 배치 범위 설정
web_x_min, web_x_max = 270, 1180
web_y_min, web_y_max = 210, 760


def init():
    global image, door, girl, mop, web_list
    image = load_image('basement.png')  # 배경 이미지 로드
    door = Door(width=32, height=32)  # 첫 번째 문 크기 설정
    mop = Mop(width=32, height=32)


    girl = game_world.get_object_by_class(Girl)  # 기존 girl 객체 가져오기
    if not girl:  # girl 객체가 없으면 새로 생성
        girl = Girl()
        game_world.add_object(girl, 2)

    girl.x, girl.y = 420, 770  # 초기 위치

    for _ in range(10):
        x = random.randint(web_x_min, web_x_max)
        y = random.randint(web_y_min, web_y_max)
        web = Web()
        web_list.append((web,x,y))




def draw():
    global image, door, mop
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door.draw(door_x, door_y)  # 첫 번째 문 그리기
    mop.draw(mop_x, mop_y)

    for web, x, y in web_list:
        web.draw(x,y)


    game_world.render()
    update_canvas()


def handle_events():
    global girl, door
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

        else:
            if girl:
                girl.handle_event(event)


def update():
    global girl
    if girl:  # girl 객체가 존재할 경우에만 실행
        girl.x = max(270, min(1180, girl.x))  # x축 이동 범위 제한
        girl.y = max(210, min(760, girl.y))  # y축 이동 범위 제한
    game_world.update()  # 다른 객체들도 업데이트


def pause(): pass

def resume(): pass

def finish():
    global image, door, mop, web_list
    del image
    del door
    del mop
    web_list.clear()


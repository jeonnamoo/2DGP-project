from pico2d import *

import game_framework
import game_world
from door import Door
from girl import Girl
from broom import Broom
import livingroom
from mop import Mop
from duster import Duster
from key import Key
from gage import Gage



image = None
door = None
gage = None

door_x, door_y = 720, 550  # 문 위치
width, height = 1440, 960  # Yard 크기
broom_x, broom_y = 520, 490
girl = None
broom = None
mop = None
key = None
duster = None
attached_object = None  # 새롭게 생성된 broom을 관리할 변수

# yard.py
web_list = []
stain_list = []
can_list = []


def init():
    global image, door, girl, broom, mop, duster, key, gage
    image = load_image('yard.png')  # 배경 이미지 로드
    door = Door(width=32, height=32)  # 문 크기 설정


    girl = game_world.get_object_by_class(Girl)  # 기존 girl 객체 가져오기
    if not girl:  # girl 객체가 없으면 새로 생성
        girl = Girl()
        game_world.add_object(girl, 2)

    broom = game_world.get_object_by_class(Broom)
    if not broom:
        broom = Broom(width=32, height=32)
        game_world.add_object(broom, 1)
    # gage 초기화 및 추가
    if not gage:
        gage = Gage()
        game_world.add_object(gage, 3)  # UI 레이어에 추가


    broom.current_map = "yard"  # 현재 맵을 yard로 설정

    girl.x, girl.y = 720, 550  # 초기 위치

    if not broom.attached:
        broom.x, broom.y = 520, 490  # broom 초기 위치


def draw():
    global image, door, broom,  gage
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door.draw(door_x, door_y)  # 문 그리기

    broom.draw()

    if gage:
        gage.draw()  # gage 그리기

    game_world.render()  # 나머지 객체들 그리기
    update_canvas()

def handle_events():
    global girl, door, broom, attached_object
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            # Door 근처 거리 계산
            distance_to_door = ((girl.x - door_x) ** 2 + (girl.y - door_y) ** 2) ** 0.5
            if distance_to_door <= 30:
                game_framework.change_mode(livingroom)

            # Broom 근처 거리 계산
            distance_to_broom = ((girl.x - broom.x) ** 2 + (girl.y - broom.y) ** 2) ** 0.5
            if distance_to_broom <= 30:
                girl.set_item(broom)  # 새로운 Broom 부착

        else:
            if girl:
                girl.handle_event(event)



def update():
    global girl, gage
    if girl:  # girl 객체가 존재할 경우에만 실행
        girl.x = max(500, min(820, girl.x))  # x축 이동 범위 제한
        girl.y = max(475, min(530, girl.y))  # y축 이동 범위 제한

    if gage:
        game_framework.update_gage(gage)  # gage 상태 업데이트
        gage.update()



    game_world.update()  # 다른 객체들도 업데이트

def pause(): pass
def resume(): pass
def finish():
    global image, door
    del image
    del door
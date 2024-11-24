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


image = None
door = None
broom = None
door_x, door_y = 720, 550  # 문 위치
width, height = 1440, 960  # Yard 크기
broom_x, broom_y = 520, 490
girl = None



def init():
    global image, door, girl, broom, mop, duster, key
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


    broom.current_map = "yard"  # 현재 맵을 yard로 설정

    girl.x, girl.y = 720, 550  # 초기 위치

    if not broom.attached:
        broom.x, broom.y = 520, 490  # broom 초기 위치


def draw():
    global image, door,broom
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door.draw(door_x, door_y)  # 문 그리기

    broom.draw()
    game_world.render()

    update_canvas()

def handle_events():
    global girl, door, broom, mop, key, duster
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            # Girl과 Door 사이의 거리 계산
            distance = ((girl.x - door_x) ** 2 + (girl.y - door_y) ** 2) ** 0.5
            if distance <= 30:  # 문 근처(거리 50 이하)일 때만 Livingroom으로 전환
                game_framework.change_mode(livingroom)
            distance_to_broom = ((girl.x - broom.x) ** 2 + (girl.y - broom.y) ** 2) ** 0.5
            if distance_to_broom <= 30 and not broom.attached:
                broom.attach(girl)  # broom을 girl에 부착
                if mop and mop.attached:
                    mop.detach()
                    mop.x, mop.y = 110, 300  # yard 초기 위치로 복귀
                if duster and duster.attached:
                    duster.detach()
                    duster.x, duster.y = 720, 630  # yard 초기 위치로 복귀
                if key and key.attached:
                    key.detach()
                    key.x, key.y = 1070, 570  # yard 초기 위치로 복귀
                if broom and broom.attached:
                    broom.detach()
                    broom.x, broom.y = 520, 490  # yard 초기 위치로 복귀


        else:
            if girl:
                girl.handle_event(event)

def update():
    global girl
    if girl:  # girl 객체가 존재할 경우에만 실행
        girl.x = max(500, min(820, girl.x))  # x축 이동 범위 제한
        girl.y = max(475, min(530, girl.y))  # y축 이동 범위 제한

    game_world.update()  # 다른 객체들도 업데이트

def pause(): pass
def resume(): pass
def finish():
    global image, door
    del image
    del door
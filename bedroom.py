from pico2d import *

import game_framework
import game_world
import livingroom
from door import Door
from girl import Girl
from key import Key

image = None
door = None
key = None
door_x, door_y = 244, 248  # 문 위치
key_x, key_y = 1070, 570
width, height = 1440, 960  # Yard 크기
girl = None


def init():
    global image, door, girl, key
    image = load_image('bedroom.png')  # 배경 이미지 로드
    door = Door(width=32, height=32)  # 첫 번째 문 크기 설정
    key = Key(width=32, height =32)


    girl = game_world.get_object_by_class(Girl)  # 기존 girl 객체 가져오기
    if not girl:  # girl 객체가 없으면 새로 생성
        girl = Girl()
        game_world.add_object(girl, 2)

    girl.x, girl.y = 244, 248  # 초기 위치


def draw():
    global image, door, key
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door.draw(door_x, door_y)  # 첫 번째 문 그리기
    key.draw(key_x, key_y)
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
                game_framework.change_mode(livingroom)


        else:
            if girl:
                girl.handle_event(event)


def update():
    global girl
    if girl:  # girl 객체가 존재할 경우에만 실행
        girl.x = max(200, min(1240, girl.x))  # x축 이동 범위 제한
        girl.y = max(150, min(810, girl.y))  # y축 이동 범위 제한
    game_world.update()  # 다른 객체들도 업데이트


def pause(): pass


def resume(): pass


def finish():
    global image, door, key
    del image
    del door
    del key


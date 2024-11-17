from pico2d import *

import bedroom
import game_framework
import game_world
import kitchen
import library
import yard
from door import Door
from girl import Girl

image = None
door1 = None
door2 = None
door3 = None
door4 = None

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
from_mode = None


def init():
    global image, door1, door2, door3, door4, girl
    image = load_image('livingroom.png')  # 배경 이미지 로드
    door1, door2, door3, door4 = Door(), Door(), Door(), Door()

    girl = game_world.get_object_by_class(Girl)  # 기존 girl 객체 가져오기
    if not girl:  # girl 객체가 없으면 새로 생성
        girl = Girl()
        game_world.add_object(girl, 2)

    # 마지막 사용된 문을 기준으로 초기 위치 설정
    if from_mode == 'yard' and last_used_door in door_positions:
        girl.x, girl.y = door_positions[last_used_door]
    elif from_mode == 'kitchen' and last_used_door in door_positions:
        girl.x, girl.y = door_positions[last_used_door]
    elif from_mode == 'bedroom' and last_used_door in door_positions:
        girl.x, girl.y = door_positions[last_used_door]
    elif from_mode == 'library' and last_used_door in door_positions:
        girl.x, girl.y = door_positions[last_used_door]


def draw():
    global image, door1, door2, door3, door4
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door1.draw(*door_positions['door1'])  # 문1 그리기
    door2.draw(*door_positions['door2'])  # 문2 그리기
    door3.draw(*door_positions['door3'])  # 문3 그리기
    door4.draw(*door_positions['door4'])  # 문4 그리기
    game_world.render()
    update_canvas()


def handle_events():
    global girl, last_used_door, from_mode
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            for door, position in door_positions.items():
                distance = ((girl.x - position[0]) ** 2 + (girl.y - position[1]) ** 2) ** 0.5
                if distance <= 30:
                    last_used_door = door
                    from_mode = 'livingroom'
                    if door == 'door1':
                        game_framework.change_mode(yard)
                    elif door == 'door2':
                        game_framework.change_mode(kitchen)
                    elif door == 'door3':
                        game_framework.change_mode(bedroom)
                    elif door == 'door4':
                        game_framework.change_mode(library)
        else:
            if girl:
                girl.handle_event(event)


def update():
    global girl
    if girl:  # girl 객체가 존재할 경우에만 실행
        girl.x = max(200, min(1290, girl.x))  # x축 이동 범위 제한
        girl.y = max(150, min(810, girl.y))  # y축 이동 범위 제한
    game_world.update()  # 다른 객체들도 업데이트


def pause(): pass
def resume(): pass
def finish():
    global image, door1, door2, door3, door4
    del image
    del door1
    del door2
    del door3
    del door4

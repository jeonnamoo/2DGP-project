from pico2d import *

import game_framework
import game_world
import yard
from door import Door
from girl import Girl



image = None
door = None
door_x, door_y = 800, 300  # 문 위치
width, height = 1440, 960  # Yard 크기
girl = None

def init():
    global image, door, girl
    image = load_image('livingroom.png')  # 배경 이미지 로드
    door = Door(width=32, height=32)  # 문 크기 설정

    girl = Girl()
    game_world.add_object(girl, 2)

def draw():
    global image, door
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door.draw(door_x, door_y)  # 문 그리기
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
            # Girl과 Door 사이의 거리 계산
            distance = ((girl.x - door_x) ** 2 + (girl.y - door_y) ** 2) ** 0.5
            if distance <= 30:  # 문 근처(거리 50 이하)일 때만 Livingroom으로 전환
                game_framework.change_mode(yard)
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
    global image, door
    del image
    del door


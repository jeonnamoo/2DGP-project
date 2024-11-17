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
door1_x, door1_y = 820, 300  # 첫 번째 문 위치
door2_x, door2_y = 410, 160  # 두 번째 문 위치
door3_x, door3_y = 800, 800  # 첫 번째 문 위치
door4_x, door4_y = 910, 910  # 두 번째 문 위치
width, height = 1440, 960  # Livingroom 크기
girl = None

def init():
    global image, door1, door2,door3, door4, girl
    image = load_image('livingroom.png')  # 배경 이미지 로드
    door1 = Door(width=32, height=32)  # 첫 번째 문 크기 설정
    door2 = Door(width=32, height=32)  # 두 번째 문 크기 설정
    door3 = Door(width=32, height=32)  # 첫 번째 문 크기 설정
    door4 = Door(width=32, height=32)  # 두 번째 문 크기 설정

    girl = game_world.get_object_by_class(Girl)  # 기존 girl 객체 가져오기
    if not girl:  # girl 객체가 없으면 새로 생성
        girl = Girl()
        game_world.add_object(girl, 2)

    girl.x, girl.y = 820, 300  # 초기 위치

def draw():
    global image, door1, door2, door3, door4
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door1.draw(door1_x, door1_y)  # 첫 번째 문 그리기
    door2.draw(door2_x, door2_y)  # 두 번째 문 그리기
    door3.draw(door3_x, door3_y)  # 첫 번째 문 그리기
    door4.draw(door4_x, door4_y)  # 두 번째 문 그리기
    game_world.render()
    update_canvas()

def handle_events():
    global girl, door1, door2
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            # 첫 번째 문 근처에서 눌렀을 경우
            distance1 = ((girl.x - door1_x) ** 2 + (girl.y - door1_y) ** 2) ** 0.5
            if distance1 <= 30:  # 문 근처(거리 30 이하)
                game_framework.change_mode(yard)

            # 두 번째 문 근처에서 눌렀을 경우
            distance2 = ((girl.x - door2_x) ** 2 + (girl.y - door2_y) ** 2) ** 0.5
            if distance2 <= 30:  # 문 근처(거리 30 이하)
                game_framework.change_mode(kitchen)

            distance3 = ((girl.x - door3_x) ** 2 + (girl.y - door3_y) ** 2) ** 0.5
            if distance3 <= 30:  # 문 근처(거리 30 이하)
                game_framework.change_mode(bedroom)

            distance4 = ((girl.x - door4_x) ** 2 + (girl.y - door4_y) ** 2) ** 0.5
            if distance4 <= 30:  # 문 근처(거리 30 이하)
                game_framework.change_mode(library)
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
    global image, door1, door2, door3, door4
    del image
    del door1
    del door2
    del door3
    del door4

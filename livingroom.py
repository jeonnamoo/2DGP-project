from pico2d import *

import game_framework
import game_world
import yard
from door import Door
from girl import Girl


image = None
doors = []
width, height = 1440, 960  # Yard 크기
girl = None



def init():
    global image
    image = load_image('livingroom.png')  # 배경 이미지 로드




def draw():
    global image
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    game_world.render()
    update_canvas()

def handle_events():
    girl = game_world.get_object_by_class(Girl)  # game_world에서 girl 객체 가져오기
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if 300 <= girl.x <= 360 and 100 <= girl.y <= 120:  # 특정 범위 확인
                game_framework.change_mode(yard)

        else:
            if girl:
                girl.handle_event(event)

def update():
    global girl
    if girl:
        girl.x = max(200, min(1240, girl.x))  # x축 이동 범위 제한
        girl.y = max(150, min(810, girl.y))  # y축 이동 범위 제한
    game_world.update()  # 다른 객체들도 업데이트
def pause(): pass
def resume(): pass
def finish():
    global image
    del image
    doors.clear()


from pico2d import *

import game_framework
import girl
from door import Door
from girl import Girl


image = None
door = None
door_x, door_y = 720, 550  # 문 위치
width, height = 1440, 960  # Yard 크기

def init():
    global image, door
    image = load_image('yard.png')  # 배경 이미지 로드
    door = Door(width=32, height=32)  # 문 크기 설정

def draw():
    global image, door
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    door.draw(door_x, door_y)  # 문 그리기
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if 700 <= girl.x <= 740 and 540 <= girl.y <= 560:  # 특정 범위 확인
                import livingroom
                game_framework.change_mode(livingroom)

def update(): pass
def pause(): pass
def resume(): pass


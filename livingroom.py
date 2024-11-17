from pico2d import *

import game_framework

image = None
width, height = 1440, 960  # Livingroom 크기

def init():
    global image
    image = load_image('livingroom.png')  # 배경 이미지 로드

def draw():
    global image
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def update(): pass
def pause(): pass
def resume(): pass

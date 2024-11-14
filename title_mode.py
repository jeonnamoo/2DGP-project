from pico2d import load_image, get_events, clear_canvas, update_canvas
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import play_mode

def init():
    global image
    image = load_image('main_screen.png')

def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(play_mode)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode)

def draw():
    clear_canvas()
    # 현재 캔버스 크기 가져오기
    canvas_width, canvas_height = 1440, 960  # 캔버스 크기를 명시적으로 설정해주거나 자동으로 가져와야 함
    # 이미지의 너비와 높이를 캔버스 크기에 맞게 조정하여 그리기
    image.draw_to_origin(0, 0, canvas_width, canvas_height)
    update_canvas()

def update(): pass

def pause(): pass
def resume(): pass
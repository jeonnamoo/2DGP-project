from pico2d import load_image, get_events, clear_canvas, update_canvas
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import game_world
import play_mode
import yard
from gage import Gage

gage_object = None  # gage 객체 초기화

def init():
    global image
    image = load_image('main_screen.png')

def finish():
    global image
    del image

def handle_events():
    global gage_object
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_SPACE:
                # Space를 누른 후 gage 활성화
                if not gage_object:
                    gage_object = Gage()  # gage 생성
                    game_world.add_object(gage_object, 3)  # UI 레이어에 추가
                game_framework.change_mode(yard)  # yard로 전환

def draw():
    global gage_object
    clear_canvas()
    # 현재 캔버스 크기 가져오기
    canvas_width, canvas_height = 1440, 960  # 캔버스 크기를 명시적으로 설정해주거나 자동으로 가져와야 함
    # 이미지의 너비와 높이를 캔버스 크기에 맞게 조정하여 그리기
    image.draw_to_origin(0, 0, canvas_width, canvas_height)
    if gage_object:
        gage_object.draw()  # gage 렌더링
    update_canvas()

def update(): pass

def pause(): pass
def resume(): pass

import game_framework
from pico2d import load_image, delay, clear_canvas, update_canvas, get_events, get_time

import title_mode


def init():
    global image

    global logo_start_time
    image = load_image('load_screen.png')

    logo_start_time = get_time()



def finish():
    global image
    del image

def update():
    global logo_start_time
    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_framework.change_mode(title_mode)

def draw():
    clear_canvas()
    # 현재 캔버스 크기 가져오기
    canvas_width, canvas_height = 1440, 960  # 캔버스 크기를 명시적으로 설정해주거나 자동으로 가져와야 함
    # 이미지의 너비와 높이를 캔버스 크기에 맞게 조정하여 그리기
    image.draw_to_origin(0, 0, canvas_width, canvas_height)
    update_canvas()

def handle_events():
    events = get_events()

def pause(): pass
def resume(): pass
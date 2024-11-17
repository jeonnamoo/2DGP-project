from pico2d import *
import game_world
import game_framework
from yard import Yard
from girl import Girl
from livingroom import Livingroom

running = True
current_mode = "yard"  # 현재 모드 상태
girl = None

def handle_events():
    global running, current_mode

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if current_mode == "yard" and check_girl_position():
                switch_to_livingroom()
        else:
            girl.handle_event(event)

def reset_world():
    global girl, current_mode

    game_world.clear()

    if current_mode == "yard":
        yard = Yard()
        game_world.add_object(yard, 0)  # Yard 배경 추가
    elif current_mode == "livingroom":
        livingroom = Livingroom()
        game_world.add_object(livingroom, 0)  # Livingroom 배경 추가

    girl = Girl()
    game_world.add_object(girl, 1)  # Girl 객체 추가

def check_girl_position():
    # girl 위치를 확인하여 특정 조건을 만족하는지 판단
    return girl.y >= 520 and 720 <= girl.x <= 752

def switch_to_livingroom():
    global current_mode
    print("Switching to Livingroom...")
    current_mode = "livingroom"
    reset_world()  # Livingroom 초기화

open_canvas(1440, 960)
reset_world()

while running:
    handle_events()
    game_world.update()
    clear_canvas()
    game_world.render()
    update_canvas()
    delay(0.01)

close_canvas()

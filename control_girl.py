from pico2d import *
import game_world
import game_framework
from yard import Yard
from girl import Girl
from livingroom import Livingroom

running = True
current_mode = "yard"  # 현재 모드 상태 (yard 또는 livingroom)
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
            if current_mode == "yard" and check_collision_with_door():
                switch_to_livingroom()  # Livingroom으로 전환
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

def check_collision_with_door():
    yard = game_world.get_object_by_class(Yard)
    if yard:
        return game_world.collide(girl, yard.get_door())
    return False

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
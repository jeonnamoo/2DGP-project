from pico2d import *

import game_world
from yard import Yard
from girl import Girl
from door import Door

running = True
girl = None
door = None


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            girl.handle_event(event)


def reset_world():
    global girl, door

    game_world.clear()

    # 배경 추가
    yard = Yard()
    game_world.add_object(yard, 0)  # 배경 레이어 (0)

    # Door 추가
    door = Door(x=740, y=610)  # 문 위치를 조정하여 정확히 배치
    game_world.add_object(door, 1)  # Door는 1번 레이어에 배치

    # Girl 추가
    girl = Girl()
    game_world.add_object(girl, 2)  # Girl은 2번 레이어에 배치


open_canvas(1440, 960)
reset_world()

# game loop
while running:
    handle_events()
    game_world.update()
    clear_canvas()
    game_world.render()
    update_canvas()
    delay(0.01)

# finalization code
close_canvas()

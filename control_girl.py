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
    game_world.add_object(yard, 0)  # 레이어 0: 배경

    # 문 추가
    door = Door(x=740, y=610)
    game_world.add_object(door, 1)  # 레이어 1: 문

    # 캐릭터 추가
    girl = Girl()
    game_world.add_object(girl, 2)  # 레이어 2: 캐릭터


def check_collision(obj1, obj2):
    # 충돌 판정 함수 (AABB 방식)
    left1, bottom1, right1, top1 = obj1.get_bb()
    left2, bottom2, right2, top2 = obj2.get_bb()

    if left1 > right2 or right1 < left2 or top1 < bottom2 or bottom1 > top2:
        return False
    return True


open_canvas(1440, 960)
reset_world()

# 게임 루프
while running:
    handle_events()
    game_world.update()

    # 충돌 판정
    if check_collision(girl, door):
        print("Collision with Door!")

    clear_canvas()
    game_world.render()
    update_canvas()
    delay(0.01)

# 종료 코드
close_canvas()

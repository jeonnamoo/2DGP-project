from pico2d import *

import game_world
from yard import Yard
from girl import Girl

running = True
girl = None
yard = None


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
    global girl, yard

    game_world.clear()

    # Yard와 Door 추가
    yard = Yard()
    game_world.add_object(yard, 0)  # 레이어 0: Yard

    # 캐릭터 추가
    girl = Girl()
    game_world.add_object(girl, 1)  # 레이어 1: 캐릭터


def check_collision_with_door():
    # Yard 내부의 Door와 충돌 확인
    if yard is not None and girl is not None:
        if collide(girl, yard.get_door_bb()):
            print("Collision with Door!")


def collide(obj, rect):
    # 충돌 판정 (AABB 방식)
    left1, bottom1, right1, top1 = obj.get_bb()
    left2, bottom2, right2, top2 = rect

    return not (left1 > right2 or right1 < left2 or top1 < bottom2 or bottom1 > top2)


open_canvas(1440, 960)
reset_world()

# 게임 루프
while running:
    handle_events()
    game_world.update()
    check_collision_with_door()  # Door 충돌 체크
    clear_canvas()
    game_world.render()
    update_canvas()
    delay(0.01)

close_canvas()

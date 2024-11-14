from pico2d import *

import game_world
from yard import Yard
from girl import Girl


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
    global running
    global girl

    running = True

    yard = Yard()
    game_world.add_object(yard, 0)

    girl = Girl()
    game_world.add_object(girl, 1)


open_canvas()
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

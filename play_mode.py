from pico2d import *

import game_framework
import game_world
import information_mode
import title_mode
from yard import Yard
from girl import Girl


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_i):
            game_framework.push_mode(information_mode)
        else:
            girl.handle_event(event)


def init():
    global girl

    running = True

    yard = Yard()
    game_world.add_object(yard, 0)

    girl = Girl()
    game_world.add_object(girl, 1)

def finish():
    game_world.clear()
    pass

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause(): pass
def resume(): pass


from pico2d import *

import game_framework
import game_world
import information_mode
import title_mode
import yard
import livingroom
from girl import Girl
from door import Door


def handle_events():
    global girl
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_mode(title_mode)
            elif event.key == SDLK_i:
                import information_mode
                game_framework.push_information_mode(information_mode.InformationMode())
            else:
                if girl:
                    girl.handle_event(event)



def init():
    global girl

    running = True


    girl = Girl()
    game_world.add_object(girl, 2)

    door = Door()
    game_world.add_object(door, 1)

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

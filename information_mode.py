from pico2d import load_image, get_events, clear_canvas, update_canvas
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDLK_0, SDLK_1, SDLK_2

import game_framework
import game_world
import play_mode
from pannel import Pannel

class InformationMode:
    def __init__(self):
        self.pannel = None

    def init(self):
        self.pannel = Pannel()

    def finish(self):
        self.pannel = None

    def draw(self):
        clear_canvas()
        self.pannel.draw()
        update_canvas()

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.pop_information_mode()


def init():
    global pannel
    if pannel is None:
        pannel = Pannel()
        game_world.add_object(pannel, 3)  # 3번 레이어에 추가 (가장 위)

def finish():
    game_world.remove_object(pannel)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def update(): pass
def pause(): pass
def resume(): pass
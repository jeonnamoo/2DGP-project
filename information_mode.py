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
        from pannel import Pannel
        self.pannel = Pannel()

    def finish(self):
        del self.pannel

    def draw(self):
        if self.pannel:
            self.pannel.draw()

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                # information_mode 종료
                game_framework.pop_information_mode()

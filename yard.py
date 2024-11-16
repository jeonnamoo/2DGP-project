from pico2d import *
import game_world

class Yard:
    def __init__(self):
        self.image = load_image('yard.png')
        self.x, self.y = 720, 480
        self.width, self.height = 1440, 960
        self.door_bb = (720 - 32, 500 - 64, 720 + 32, 500 + 64)  # Door Bounding Box

    def draw(self):
        self.image.draw_to_origin(0, 0, self.width, self.height)
        # Door의 Bounding Box 그리기 (디버깅용)
        draw_rectangle(*self.door_bb)

    def update(self):
        pass

    def get_door_bb(self):
        return self.door_bb

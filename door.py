from pico2d import *
import game_world

class Door:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Door.image == None:
            Door.image = load_image('door.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

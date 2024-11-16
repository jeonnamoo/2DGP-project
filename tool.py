from pico2d import *
import game_world

class Broom:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Broom.image == None:
            Broom.image = load_image('broom.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)

class Mop:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Mop.image == None:
            Mop.image = load_image('mop.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)

class Duster:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Duster.image == None:
            Duster.image = load_image('duster.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)
from pico2d import load_image


class Basement:
    def __init__(self):
        self.image = load_image('basement.png')

    def draw(self):
        self.image.draw(720, 480)

    def update(self):
        pass

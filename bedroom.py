from pico2d import load_image


class Bedroom:
    def __init__(self):
        self.image = load_image('bedroom.png')

    def draw(self):
        self.image.draw(720, 480)

    def update(self):
        pass

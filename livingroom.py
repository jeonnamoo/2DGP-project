from pico2d import load_image


class Livingroom:
    def __init__(self):
        self.image = load_image('livingroom.png')

    def draw(self):
        self.image.draw(720, 480)

    def update(self):
        pass

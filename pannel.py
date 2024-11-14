from pico2d import load_image

class Pannel:
    def __init__(self):
        self.image = load_image('describe.png')

    def draw(self):
        self.image.draw(720, 480)

    def update(self):
        pass
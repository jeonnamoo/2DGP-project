from pico2d import load_image


class Library:
    def __init__(self):
        self.image = load_image('library.png')

    def draw(self):
        self.image.draw(720, 480)

    def update(self):
        pass

from pico2d import *
import game_world

class Door:
    image = None

    def __init__(self, x=400, y=300):
        if Door.image is None:
            Door.image = load_image('image.png')  # 첨부한 door 이미지를 사용
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

from pico2d import *

class Yard:
    def __init__(self):
        self.image = load_image('yard.png')
        self.x, self.y = 720, 480  # Yard 중심 좌표 (캔버스 중앙)
        self.width, self.height = 1440, 960  # Yard 크기

    def draw(self):
        self.image.draw_to_origin(0, 0, self.width, self.height)

    def update(self):
        pass

    def get_bb(self):
        # Yard의 Bounding Box 반환
        return self.x - self.width // 2, self.y - self.height // 2, \
               self.x + self.width // 2, self.y + self.height // 2

from pico2d import load_image


class Yard:
    def __init__(self):
        self.image = load_image('yard.png')

    def draw(self):
        # 캔버스 전체 크기에 맞춰 배경을 정확히 그립니다.
        self.image.draw_to_origin(0, 0, 1440, 960)

    def update(self):
        pass

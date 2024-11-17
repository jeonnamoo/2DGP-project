from pico2d import load_image


class Livingroom:
    def __init__(self):
        self.image = load_image('livingroom.png')  # 배경 이미지
        self.x, self.y = 720, 480  #  중심 좌표
        self.width, self.height = 1440, 960  #  크기

    def draw(self):
        # 배경 그리기
        self.image.draw_to_origin(0, 0, self.width, self.height)

    def update(self):
        pass

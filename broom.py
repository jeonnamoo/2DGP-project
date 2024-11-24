from pico2d import *

class Broom:
    image = None

    def __init__(self, width=40, height=50, scale=4):  # 기본 크기와 배율 설정
        if Broom.image is None:
            Broom.image = load_image('broom.png')  # Broom 이미지 로드
        self.width, self.height = width * scale, height * scale  # 크기 설정
        self.x, self.y = 0, 0  # 초기 위치 설정

    def draw(self):
        # 객체의 내부 속성 x, y를 사용하여 이미지 그리기
        self.image.draw_to_origin(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

    def update(self):
        pass

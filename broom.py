from pico2d import *




class Broom:
    image = None

    def __init__(self, width=40, height=50, scale=4):  # 기본 크기와 배율 설정
        if Broom.image is None:
            Broom.image = load_image('broom.png')  # 문 이미지 로드
        self.width, self.height = width * scale, height * scale  # 문 크기를 4배로 설정

    def draw(self, x, y):
        # 문 이미지를 크기 조정하여 주어진 위치(x, y)에 그리기
        self.image.draw_to_origin(x - self.width // 2, y - self.height // 2, self.width, self.height)
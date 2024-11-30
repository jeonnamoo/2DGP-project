from pico2d import *

class Gage:
    def __init__(self, x=400, y=920):  # 기본 위치
        self.image = load_image('gage.png')  # gage 이미지 로드
        self.x = x
        self.y = y

    def draw(self):
        """gage 렌더링"""
        self.image.draw(self.x, self.y)

    def update(self):
        """gage 업데이트 (필요할 경우 구현)"""
        pass

from pico2d import *
import game_world

class Door:
    image = None

    def __init__(self, x=740, y=610, width=64, height=128):  # 문 크기 추가
        if Door.image is None:
            Door.image = load_image('door.png')  # 문 이미지 로드
        self.x, self.y = x, y
        self.width, self.height = width, height  # 문 크기 설정

    def get_bb(self):
        # 문 객체의 충돌 영역 반환 (Bounding Box)
        return (self.x - self.width // 2, self.y - self.height // 2,
                self.x + self.width // 2, self.y + self.height // 2)

    def draw(self):
        if Door.image is not None:
            Door.image.draw(self.x, self.y)
            # 충돌 영역 디버깅용 사각형 (필요하면 주석 처리)
            draw_rectangle(*self.get_bb())

    def update(self):
        pass

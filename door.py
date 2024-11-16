from pico2d import *
import game_world

class Door:
    image = None

    def __init__(self, x=740, y=610):  # 문 좌표를 정밀히 조정
        if Door.image is None:
            Door.image = load_image('door.png')  # 문 이미지 로드
        self.x, self.y = x, y

    def draw(self):
        print(f"Drawing Door at ({self.x}, {self.y})")  # 디버깅 메시지
        self.image.draw(self.x, self.y)

    def update(self):
        pass

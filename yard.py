from pico2d import *
from door import Door

class Yard:
    def __init__(self):
        self.image = load_image('yard.png')  # 배경 이미지
        self.door = Door(width=32, height=32)  # 문 크기 설정
        self.x, self.y = 720, 480  # Yard 중심 좌표
        self.width, self.height = 1440, 960  # Yard 크기
        self.door_x, self.door_y = 720, 550  # 문 위치

    def draw(self):
        # 배경 그리기
        self.image.draw_to_origin(0, 0, self.width, self.height)
        # 문 그리기
        self.door.draw(self.door_x, self.door_y)

    def update(self):
        pass


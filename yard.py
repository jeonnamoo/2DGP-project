from pico2d import *

class Yard:
    def __init__(self):
        self.image = load_image('yard.png')  # 배경 이미지
        self.door_image = load_image('door.png')  # 문 이미지
        self.x, self.y = 720, 480  # Yard 중심 좌표
        self.width, self.height = 1440, 960  # Yard 크기
        self.door_x, self.door_y = 720, 520  # 문 위치
        self.door_width, self.door_height = 32, 32  # 문 크기

    def draw(self):
        # 배경 그리기
        self.image.draw_to_origin(0, 0, self.width, self.height)
        # 문 그리기
        self.door_image.draw(self.door_x, self.door_y)

    def update(self):
        pass

    def get_door_bb(self):
        # 문의 Bounding Box 반환
        return (self.door_x - self.door_width // 2, self.door_y - self.door_height // 2,
                self.door_x + self.door_width // 2, self.door_y + self.door_height // 2)

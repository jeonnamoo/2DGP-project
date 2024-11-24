from pico2d import *

class Broom:
    image = None

    def __init__(self, width=40, height=50, scale=4):
        if Broom.image is None:
            Broom.image = load_image('broom.png')  # Broom 이미지 로드
        self.width, self.height = width * scale, height * scale
        self.x, self.y = 520, 490  # 초기 위치 설정 (yard의 위치)
        self.attached = False  # broom이 girl에 부착되었는지 상태 관리
        self.girl = None  # 부착된 대상
        self.current_map = "yard"  # 기본 맵을 yard로 설정

    def attach(self, girl):
        """broom을 girl에 부착"""
        self.attached = True
        self.girl = girl

    def detach(self):
        """broom을 girl에서 분리"""
        self.attached = False
        self.girl = None

    def update(self):
        """부착된 상태일 경우 girl의 위치를 따라감"""
        if self.attached and self.girl:
            self.x, self.y = self.girl.x, self.girl.y

    def draw(self):
        """broom을 그리는 조건"""
        if self.attached:  # 부착된 상태일 경우 현재 위치에 그림
            self.image.draw_to_origin(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)
        elif self.current_map == "yard":  # yard일 경우 초기 위치에 그림
            self.image.draw_to_origin(520 - self.width // 2, 490 - self.height // 2, self.width, self.height)

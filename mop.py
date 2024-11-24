from pico2d import *

class Mop:
    image = None

    def __init__(self, width=40, height=50, scale=3):
        if Mop.image is None:
            Mop.image = load_image('mop.png')  # Mop 이미지 로드
        self.width, self.height = width * scale, height * scale
        self.x, self.y = 1100, 300  # basement 초기 위치
        self.attached = False  # mop이 girl에 부착되었는지 상태 관리
        self.girl = None  # 부착된 대상
        self.current_map = "basement"  # 기본 맵을 basement로 설정

    def attach(self, girl):
        """mop을 girl에 부착"""
        self.attached = True
        self.girl = girl

    def detach(self):
        """mop을 girl에서 분리"""
        self.attached = False
        self.girl = None

    def update(self):
        """부착된 상태일 경우 girl의 위치를 따라감"""
        if self.attached and self.girl:
            self.x, self.y = self.girl.x, self.girl.y

    def draw(self):
        if self.attached:  # 부착된 상태일 경우 현재 위치에 그림
            self.image.draw_to_origin(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)
        elif self.current_map == "basement":  # basement일 경우 초기 위치에 그림
            self.image.draw_to_origin(1100 - self.width // 2, 300 - self.height // 2, self.width, self.height)
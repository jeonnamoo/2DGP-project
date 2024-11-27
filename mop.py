from pico2d import *

import game_framework


class Mop:
    image = None

    def __init__(self, width=40, height=50, scale=2):
        if Mop.image is None:
            Mop.image = load_image('mop.png')  # Broom 이미지 로드
        self.width, self.height = width * scale, height * scale
        self.x, self.y = 520, 490  # 초기 위치 설정 (yard의 위치)
        self.attached = False  # broom이 girl에 부착되었는지 상태 관리
        self.girl = None  # 부착된 대상
        self.current_map = "basement"  # 기본 맵을 yard로 설정

    def attach(self, girl):
        """Girl에 청소도구 부착"""
        if not self.attached:  # 이미 부착된 상태가 아니면
            self.attached = True
            self.girl = girl

    def detach(self):
        """Girl에서 청소도구 분리"""
        if self.attached:  # 부착된 상태인 경우
            self.attached = False
            self.girl = None

    def update(self):
        """부착된 상태일 경우 girl의 위치를 따라감"""
        if self.current_map == "basement" and self.attached and self.girl:
            self.x, self.y = self.girl.x, self.girl.y

    def draw(self):
        """broom을 현재 위치에 그리기"""
        if self.attached or self.current_map == "basement":  # yard이거나 부착된 경우만 그림
            self.image.draw_to_origin(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

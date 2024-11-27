from pico2d import *

import game_framework


class Key:
    image = None

    def __init__(self, width=40, height=50, scale=3):
        if Key.image is None:
            Key.image = load_image('key.png')  # Broom 이미지 로드
        self.width, self.height = width * scale, height * scale
        self.x, self.y = 1070, 570  # 초기 위치 설정 (yard의 위치)
        self.attached = False  # broom이 girl에 부착되었는지 상태 관리
        self.girl = None  # 부착된 대상
        self.current_map = "bedroom"  # 기본 맵을 yard로 설정

    def attach(self, girl):
        """key을 girl에 부착"""
        self.attached = True
        self.girl = girl

    def detach(self):
        """key을 girl에서 분리"""
        self.attached = False
        self.girl = None

    def update(self):
        """부착된 상태일 경우 girl의 위치를 따라감"""
        if self.attached and self.girl:
            self.x, self.y = self.girl.x, self.girl.y

    def draw(self):
        """broom을 현재 위치에 그리기"""
        if self.attached or self.current_map == "bedroom":  # yard이거나 부착된 경우만 그림
            self.image.draw_to_origin(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)
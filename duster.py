from pico2d import *

import game_framework


class Duster:
    image = None

    def __init__(self, width=40, height=50, scale=4):
        if Duster.image is None:
            Duster.image = load_image('duster.png')  # Broom 이미지 로드
        self.width, self.height = width * scale, height * scale
        self.x, self.y = 720, 630  # 초기 위치 설정 (yard의 위치)
        self.attached = False  # broom이 girl에 부착되었는지 상태 관리
        self.girl = None  # 부착된 대상
        self.current_map = "library"  # 기본 맵을 yard로 설정

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
        # 현재 맵에서만 그리기
        if self.current_map == game_framework.current_map and not self.attached:
            self.image.draw(self.x, self.y)

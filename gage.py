from pico2d import *

class Gage:
    def __init__(self, x=400, y=920):
        self.gage_image = load_image('gage.png')  # 기본 게이지 이미지
        self.bar_image = load_image('gage_bar1.png')  # 단일 바 이미지
        self.x = x
        self.y = y
        self.percentage = 0  # 현재 퍼센티지 (0~100)

    def update_level(self, removed_percentage):
        """제거된 퍼센티지에 따라 게이지를 업데이트"""
        self.percentage = min(max(removed_percentage, 0), 100)  # 0~100 사이로 제한

    def draw(self):
        """게이지와 바를 렌더링"""
        # 기본 gage 이미지 그리기
        self.gage_image.draw(self.x, self.y)

        # 퍼센티지에 따라 바 이미지 렌더링 (왼쪽부터 채우기)
        if self.percentage > 0:
            total_width = self.bar_image.w  # 전체 바 이미지 너비
            height = self.bar_image.h  # 바 이미지 높이
            fill_width = int(total_width * (self.percentage / 100))  # 채워질 너비 계산
            self.bar_image.clip_draw_to_origin(
                0, 0, fill_width, height, self.x - total_width // 2, self.y - height // 2
            )

    def update(self):
        pass

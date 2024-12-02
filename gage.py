from pico2d import *
import game_framework

class Gage:
    def __init__(self, x=400, y=920):
        self.gage_image = load_image('gage.png')  # 게이지 틀 이미지
        self.bar_image = load_image('gage_bar4.png')  # 단일 바 이미지
        self.game_clear_image = load_image('game_clear.png')  # 게임 클리어 이미지 추가
        self.x = x
        self.y = y
        self.percentage = 0  # 현재 퍼센티지 (0~100)
        self.gage_width = self.gage_image.w -10   # gage 이미지의 너비
        self.gage_height = self.gage_image.h  # gage 이미지의 높이
        self.bar_height = self.bar_image.h  # bar 이미지의 높이
        self.clear_visible = False  # 클리어 이미지 표시 여부

    def update_level(self, removed_objects):
        """삭제된 객체 개수를 기준으로 업데이트"""
        self.percentage = (removed_objects / 150) * 100  # 삭제된 객체 수를 백분율로 변환
        if removed_objects >= 150:  # 150개가 삭제되었을 때
            self.clear_visible = True

    def draw(self):
        """게이지와 바, 게임 클리어 이미지를 렌더링"""
        # gage 틀 그리기
        self.gage_image.draw(self.x, self.y)

        # 퍼센티지에 따라 gage_bar 채우기
        if self.percentage > 0:
            fill_width = int(self.gage_width * (self.percentage / 100))  # 채워질 너비 계산
            self.bar_image.clip_draw_to_origin(
                0, 0, fill_width, self.bar_height,  # 클립 영역
                self.x - (self.gage_width // 2) ,  # 왼쪽 끝부터 시작 (10px 오른쪽으로 이동)
                self.y - (self.bar_height // 2)  # y 좌표 중앙 맞춤
            )

        # 게임 클리어 이미지 그리기
        if self.clear_visible:
            self.game_clear_image.draw(720, 480)  # 화면 중앙에 표시

    def update(self):
        pass
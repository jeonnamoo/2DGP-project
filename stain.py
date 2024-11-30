from pico2d import *

class Stain:
    image = None
    water_image = None

    def __init__(self, x, y, width=40, height=50, scale=2):
        if Stain.image is None:
            Stain.image = load_image('stain.png')  # Stain 이미지 로드
        if Stain.water_image is None:
            Stain.water_image = load_image('water.png')  # Water 애니메이션 이미지 로드

        self.x, self.y = x, y
        self.width, self.height = width * scale, height * scale
        self.removed = False  # Stain이 삭제되었는지 여부
        self.water_active = False  # Water 애니메이션 활성 상태
        self.water_frame = 0  # 현재 애니메이션 프레임
        self.water_timer = 0  # 애니메이션 타이머
        self.water_frame_count = 4  # 총 애니메이션 프레임 수
        self.water_frame_delay = 1.0  # 프레임 간 지연 시간 (초)

    def activate_water(self):
        """Water 애니메이션을 활성화"""
        if not self.water_active and not self.removed:
            self.water_active = True
            self.water_frame = 0
            self.water_timer = 0

    def update(self):
        """Water 애니메이션 업데이트"""
        if self.water_active:
            self.water_timer += 1 / 60  # 프레임 시간 누적
            if self.water_timer >= self.water_frame_delay:  # 다음 프레임으로 전환
                self.water_timer = 0
                self.water_frame += 1
                if self.water_frame >= self.water_frame_count:  # 마지막 프레임 도달 시
                    self.water_active = False
                    self.removed = True  # Stain 삭제 상태로 전환

    def draw(self):
        """Stain 및 Water 애니메이션 렌더링"""
        if self.water_active:
            frame_width = self.water_image.w // self.water_frame_count
            frame_height = self.water_image.h
            self.water_image.clip_draw(
                self.water_frame * frame_width, 0, frame_width, frame_height,
                self.x, self.y, self.width, self.height  # Stain 크기에 맞춰 렌더링
            )
        elif not self.removed:  # 삭제되지 않은 경우
            self.image.draw_to_origin(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

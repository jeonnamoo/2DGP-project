from pico2d import *

class Web:
    image = None
    dust_image = None

    def __init__(self, x, y, width=40, height=50, scale=3):
        if Web.image is None:
            Web.image = load_image('web.png')  # Web 이미지 로드
        if Web.dust_image is None:
            Web.dust_image = load_image('dust.png')  # Dust 애니메이션 이미지 로드

        self.x, self.y = x, y
        self.width, self.height = width * scale, height * scale
        self.removed = False  # Web 삭제 여부
        self.dust_active = False  # Dust 애니메이션 활성화 여부
        self.dust_frame = 0  # 현재 Dust 애니메이션 프레임
        self.dust_timer = 0  # Dust 애니메이션 타이머
        self.dust_frame_count = 4  # Dust 애니메이션 총 프레임 수
        self.dust_frame_delay = 1.0  # 프레임 간 지연 시간 (초)

    def activate_dust(self):
        """Dust 애니메이션을 활성화"""
        if not self.dust_active and not self.removed:
            self.dust_active = True
            self.dust_frame = 0
            self.dust_timer = 0

    def update(self):
        """Dust 애니메이션 업데이트"""
        if self.dust_active:
            self.dust_timer += 1 / 60  # 프레임 시간 누적
            if self.dust_timer >= self.dust_frame_delay:  # 다음 프레임으로 전환
                self.dust_timer = 0
                self.dust_frame += 1
                if self.dust_frame >= self.dust_frame_count:  # 마지막 프레임 도달 시
                    self.dust_active = False
                    self.removed = True  # Web 삭제 상태로 전환

    def draw(self):
        """Web 및 Dust 애니메이션 렌더링"""
        if self.dust_active:
            frame_width = self.dust_image.w // self.dust_frame_count
            frame_height = self.dust_image.h
            self.dust_image.clip_draw(
                self.dust_frame * frame_width, 0, frame_width, frame_height,
                self.x, self.y, self.width, self.height  # Web 크기에 맞춰 렌더링
            )
        elif not self.removed:  # 삭제되지 않은 경우
            self.image.draw_to_origin(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

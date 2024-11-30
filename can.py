from pico2d import *

class Can:

    image = None
    trash_image  = None

    def __init__(self, x, y, width=40, height=50, scale=2):
        if Can.image is None:
            Can.image = load_image('can.png')  # Can 이미지 로드
        if Can.trash_image is None:
            Can.trash_image = load_image('trash.png')  # Trash 애니메이션 이미지 로드

        self.x, self.y = x, y
        self.width, self.height = width * scale, height * scale
        self.removed = False  # Can이 삭제되었는지 여부
        self.trash_active = False  # Trash 애니메이션 활성 상태
        self.trash_frame = 0  # 현재 애니메이션 프레임
        self.trash_timer = 0  # 애니메이션 타이머
        self.trash_frame_count = 4  # 총 애니메이션 프레임 수
        self.trash_frame_delay = 1.0  # 프레임 간 지연 시간 (초)

    def activate_trash(self):
        """Trash 애니메이션을 활성화"""
        if not self.trash_active and not self.removed:
            self.trash_active = True
            self.trash_frame = 0
            self.trash_timer = 0

    def update(self):
        """Trash 애니메이션 업데이트"""
        if self.trash_active:
            self.trash_timer += 1 / 60  # 프레임 시간 누적
            if self.trash_timer >= self.trash_frame_delay:  # 다음 프레임으로 전환
                self.trash_timer = 0
                self.trash_frame += 1
                if self.trash_frame >= self.trash_frame_count:  # 마지막 프레임 도달 시
                    self.trash_active = False
                    self.removed = True  # Can 삭제 상태로 전환

    def draw(self):
        """Can 및 Trash 애니메이션 렌더링"""
        if self.trash_active:
            frame_width = self.trash_image.w // self.trash_frame_count
            frame_height = self.trash_image.h
            self.trash_image.clip_draw(
                self.trash_frame * frame_width, 0, frame_width, frame_height,
                self.x, self.y, self.width, self.height  # Can 크기에 맞춰 렌더링
            )
        elif not self.removed:  # 삭제되지 않은 경우
            self.image.draw_to_origin(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

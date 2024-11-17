from pico2d import *
import game_framework
import livingroom
from door import Door

class Yard:
    def __init__(self):
        self.image = load_image('yard.png')  # 배경 이미지
        self.door = Door(width=32, height=32)  # 문 크기 설정
        self.x, self.y = 720, 480  # Yard 중심 좌표
        self.width, self.height = 1440, 960  # Yard 크기
        self.door_x, self.door_y = 736, 540  # 문 위치

    def handle_events(self, girl):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_mode(livingroom)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                # 조건 확인: 특정 범위 안에 girl이 있을 때만 전환
                if 720 <= girl.x <= 752 and girl.y >= 520:
                    game_framework.change_mode(livingroom)

    def draw(self):
        # 배경 그리기
        self.image.draw_to_origin(0, 0, self.width, self.height)
        # 문 그리기
        self.door.draw(self.door_x, self.door_y)

    def update(self):
        pass

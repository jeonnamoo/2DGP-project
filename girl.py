from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN
from state_machine import *
from ball import Ball, BigBall
import game_world


class Idle:
    @staticmethod
    def enter(girl, e):
        # Idle 상태에 진입했을 때 초기화
        girl.dir_x, girl.dir_y = 0, 0  # 멈춤
        girl.action = 0  # Idle 상태는 첫 번째 줄
        girl.frame = 0  # 애니메이션 없음

    @staticmethod
    def exit(girl, e):
        if space_down(e):
            girl.fire_ball()

    @staticmethod
    def do(girl):
        # Idle 상태에서는 애니메이션 없음
        pass

    @staticmethod
    def draw(girl):
        # Idle 상태에서는 고정된 한 프레임만 출력
        girl.image.clip_draw(0, girl.action * 64, 32, 64, girl.x, girl.y)


class Run:
    @staticmethod
    def enter(girl, e):
        # Run 상태에 진입했을 때 방향 및 애니메이션 초기화
        if right_down(e):
            girl.dir_x, girl.dir_y = 1, 0
            girl.action = 1  # 오른쪽
        elif left_down(e):
            girl.dir_x, girl.dir_y = -1, 0
            girl.action = 3  # 왼쪽
        elif top_down(e):
            girl.dir_x, girl.dir_y = 0, 1
            girl.action = 2  # 위쪽
        elif bottom_down(e):
            girl.dir_x, girl.dir_y = 0, -1
            girl.action = 0  # 아래쪽

    @staticmethod
    def exit(girl, e):
        if space_down(e):
            girl.fire_ball()

    @staticmethod
    def do(girl):
        # Run 상태에서만 애니메이션 작동 및 이동 처리
        girl.frame = (girl.frame + 1) % 4  # 4개의 프레임 순환
        girl.x += girl.dir_x * 2  # 속도를 줄임
        girl.y += girl.dir_y * 2  # 상하 이동 추가

    @staticmethod
    def draw(girl):
        # Run 상태에서는 애니메이션 프레임 순환
        girl.image.clip_draw(girl.frame * 32, girl.action * 64, 32, 64, girl.x, girl.y)


class Girl:
    def __init__(self):
        self.x, self.y = 400, 300  # 초기 위치
        self.dir_x, self.dir_y = 0, 0  # 이동 방향
        self.face_dir = 1  # 캐릭터가 바라보는 방향
        self.action = 0  # 현재 상태 (0: Idle, 1~3: Run 상태)
        self.frame = 0  # 애니메이션 프레임
        self.image = load_image('animation_sheet1.png')  # 스프라이트 시트 로드
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: Run, left_down: Run, top_down: Run, bottom_down: Run},
                Run: {right_up: Idle, left_up: Idle, top_up: Idle, bottom_up: Idle},
            }
        )
        self.set_item('NONE')

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        # 이벤트 추가
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()

    def set_item(self, item):
        self.item = item

    def fire_ball(self):
        if self.item == 'SmallBall':
            ball = Ball(self.x, self.y, self.face_dir * 10)
            game_world.add_object(ball)

        elif self.item == 'BigBall':
            ball = BigBall(self.x, self.y, self.face_dir * 10)
            game_world.add_object(ball)

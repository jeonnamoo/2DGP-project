import math


from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN, \
    clamp

import game_framework
from state_machine import *
from broom import Broom
import game_world

# girl Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 40.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# girl Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Idle:
    @staticmethod
    def enter(girl, e):
        # Idle 상태에 진입했을 때 초기화
        if e[0] == 'START':  # 게임 시작 시 기본 위치 설정
            girl.action = 3  # 1행 (아래 방향)
        elif right_down(e):  # 오른쪽 방향 입력
            girl.action = 1  # 2행 (오른쪽 방향)
        elif upkey_down(e):  # 위쪽 방향 입력
            girl.action = 2  # 3행 (위쪽 방향)
        elif left_down(e):  # 왼쪽 방향 입력
            girl.action = 3  # 4행 (왼쪽 방향)
        girl.speed = 0
        girl.frame = 0  # 애니메이션 없음
    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass

    @staticmethod
    def draw(girl):
        # Idle 상태에서 고정된 스프라이트 프레임 출력
        direction = girl.action
        frame_width, frame_height = 16, 32
        girl.image.clip_draw(0, direction * frame_height, frame_width, frame_height, girl.x, girl.y, 48, 96)


class RunRight:
    @staticmethod
    def enter(girl, e):
        girl.action = 2
        girl.speed = RUN_SPEED_PPS
        girl.dir = 0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunRightUp:
    @staticmethod
    def enter(girl, e):
        girl.action = 2
        girl.speed = RUN_SPEED_PPS
        girl.dir = math.pi / 4.0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunRightDown:
    @staticmethod
    def enter(girl, e):
        girl.action = 2
        girl.speed = RUN_SPEED_PPS
        girl.dir = -math.pi / 4.0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunLeft:
    @staticmethod
    def enter(girl, e):
        girl.action = 0
        girl.speed = RUN_SPEED_PPS
        girl.dir = math.pi

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunLeftUp:
    @staticmethod
    def enter(girl, e):
        girl.action = 0
        girl.speed = RUN_SPEED_PPS
        girl.dir = math.pi * 3.0 / 4.0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunLeftDown:
    @staticmethod
    def enter(girl, e):
        girl.action = 0
        girl.speed = RUN_SPEED_PPS
        girl.dir = - math.pi * 3.0 / 4.0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunUp:
    @staticmethod
    def enter(girl, e):
        girl.action = 1
        girl.speed = RUN_SPEED_PPS
        girl.dir = math.pi / 2.0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunDown:
    @staticmethod
    def enter(girl, e):
        girl.action = 3
        girl.speed = RUN_SPEED_PPS
        girl.dir = - math.pi / 2.0
        pass

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass



class Girl:
    def __init__(self, x = 0, y = 0):
        self.x, self.y = 720, 480  # 초기 위치
        self.frame = 0  # 애니메이션 프레임
        self.action = 0  # 현재 상태 (0: 아래, 1: 오른쪽, 2: 위, 3: 왼쪽)
        self.image = load_image('animation_sheet1.png')  # 스프라이트 시트 로드
        self.circle_mask = load_image('circle_mask.png')  # 원형 마스크 로드
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: RunRight, left_down: RunLeft, left_up: RunRight, right_up: RunLeft,
                       upkey_down: RunUp, downkey_down: RunDown, upkey_up: RunDown, downkey_up: RunUp},
                RunRight: {right_up: Idle, left_down: Idle, upkey_down: RunRightUp, upkey_up: RunRightDown,
                           downkey_down: RunRightDown, downkey_up: RunRightUp},
                RunRightUp: {upkey_up: RunRight, right_up: RunUp, left_down: RunUp, downkey_down: RunRight},
                RunUp: {upkey_up: Idle, left_down: RunLeftUp, downkey_down: Idle, right_down: RunRightUp,
                        left_up: RunRightUp, right_up: RunLeftUp},
                RunLeftUp: {right_down: RunUp, downkey_down: RunLeft, left_up: RunUp, upkey_up: RunLeft},
                RunLeft: {left_up: Idle, upkey_down: RunLeftUp, right_down: Idle, downkey_down: RunLeftDown,
                          upkey_up: RunLeftDown, downkey_up: RunLeftUp},
                RunLeftDown: {left_up: RunDown, downkey_up: RunLeft, upkey_down: RunLeft, right_down: RunDown},
                RunDown: {downkey_up: Idle, left_down: RunLeftDown, upkey_down: Idle, right_down: RunRightDown,
                          left_up: RunRightDown, right_up: RunLeftDown},
                RunRightDown: {right_up: RunDown, downkey_up: RunRight, left_down: RunDown, upkey_down: RunRight}
            }
        )
        self.x, self.y = x, y
        self.item = None  # 현재 부착된 아이템
        self.dir = 0  # Initialize direction

    def update(self):
        self.state_machine.update()
        # 애니메이션 프레임 업데이트
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        self.x += math.cos(self.dir) * self.speed * game_framework.frame_time
        self.y += math.sin(self.dir) * self.speed * game_framework.frame_time

        # 이동 경계 제한
        self.x = clamp(50, self.x, 1440 - 50)
        self.y = clamp(50, self.y, 960 - 50)

    def handle_event(self, event):
        # 이벤트 큐에 입력 이벤트 추가
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        direction = self.action  # 현재 방향
        frame_width = 16
        frame_height = 32
        self.image.clip_draw(
            int(self.frame) * frame_width, direction * frame_height,
            frame_width, frame_height,
            self.x, self.y,  # 직접적인 좌표 사용
            48, 96
        )
        self.circle_mask.draw(self.x, self.y)

    def set_item(self, item):
        """
        현재 부착된 아이템을 관리. 기존 아이템이 있으면 제거하고 새 아이템을 부착.
        """
        if self.item:  # 기존 부착된 아이템이 있으면 제거
            print(f"Removing attached item: {self.item}")
            self.item.detach()  # 기존 아이템의 부착 해제
            game_world.remove_object(self.item)  # game_world에서 제거
        if item:  # 새로운 아이템을 부착
            print(f"Attaching new item: {item}")
            item.attach(self)
            game_world.add_object(item, 1)
        self.item = item  # 부착된 아이템 업데이트
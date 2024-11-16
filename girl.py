from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN

from door import Door
from state_machine import *
import game_world
from yard import Yard


class Idle:
    @staticmethod
    def enter(girl, e):
        # Idle 상태에 진입했을 때 초기화
        girl.dir_x, girl.dir_y = 0, 0  # 멈춤
        girl.frame = 0  # 애니메이션 없음
        if e[0] == 'START':  # 게임 시작 시 기본 위치 설정
            girl.action = 0  # 1행 (아래 방향)
        elif right_down(e):  # 오른쪽 방향 입력
            girl.action = 1  # 2행 (오른쪽 방향)
        elif top_down(e):  # 위쪽 방향 입력
            girl.action = 2  # 3행 (위쪽 방향)
        elif left_down(e):  # 왼쪽 방향 입력
            girl.action = 3  # 4행 (왼쪽 방향)

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
        girl.image.clip_draw(0, girl.action * 32, 16, 32, girl.x, girl.y, 48, 96)  # 살짝 줄인 크기로 그리기


class Run:
    @staticmethod
    def enter(girl, e):
        # Run 상태에 진입했을 때 방향 및 애니메이션 초기화
        if bottom_down(e):  # 아래 방향
            girl.dir_x, girl.dir_y = 0, 1
            girl.action = 1  # 아래쪽
        elif right_down(e):  # 오른쪽 방향
            girl.dir_x, girl.dir_y = 1, 0
            girl.action = 2  # 오른쪽
        elif top_down(e):  # 위 방향
            girl.dir_x, girl.dir_y = 0, -1
            girl.action = 3  # 위쪽
        elif left_down(e):  # 왼쪽 방향
            girl.dir_x, girl.dir_y = -1, 0
            girl.action = 0  # 왼쪽

    @staticmethod
    def exit(girl, e):
        if space_down(e):
            girl.fire_ball()

    @staticmethod
    def do(girl):
        # Run 상태에서만 애니메이션 작동 및 이동 처리
        girl.frame = (girl.frame + 1) % 4  # 4개의 프레임 순환
        girl.x += girl.dir_x * 1.5  # X축 이동
        girl.y += girl.dir_y * 1.5  # Y축 이동 (위: +, 아래: -)

        yard = game_world.get_object_by_class(Yard)
        if yard:
            girl.x = max(500, min(820, girl.x))
            girl.y = max(475, min(530, girl.y))

    @staticmethod
    def draw(girl):
        # Run 상태에서는 애니메이션 프레임 순환, 살짝 줄인 크기로 그리기
        girl.image.clip_draw(girl.frame * 16, girl.action * 32, 16, 32, girl.x, girl.y, 48, 96)



class Girl:
    def __init__(self):
        self.x, self.y = 720, 480
        self.dir_x, self.dir_y = 0, 0
        self.action = 0
        self.frame = 0
        self.image = load_image('animation_sheet1.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions({
            Idle: {bottom_down: Run, right_down: Run, top_down: Run, left_down: Run},
            Run: {bottom_up: Idle, right_up: Idle, top_up: Idle, left_up: Idle},
        })

    def update(self):
        self.state_machine.update()
        # 충돌 체크
        for obj in game_world.world[1]:  # Door가 1번 레이어에 있으므로
            if isinstance(obj, Door) and self.check_collision(obj):
                print("Collision with Door!")
                self.x -= self.dir_x * 2  # 충돌 시 이동 되돌림
                self.y -= self.dir_y * 2

    def check_collision(self, other):
        # 충돌 판정 (AABB 방식)
        left1, bottom1, right1, top1 = self.get_bb()
        left2, bottom2, right2, top2 = other.get_bb()
        if left1 > right2 or right1 < left2 or top1 < bottom2 or bottom1 > top2:
            return False
        return True

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()

    def get_bb(self):
        # 캐릭터 Bounding Box
        return self.x - 16, self.y - 32, self.x + 16, self.y + 32


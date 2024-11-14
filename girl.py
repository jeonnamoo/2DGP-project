# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from state_machine import *
from ball import Ball, BigBall
import game_world

class Idle:
    @staticmethod
    def enter(girl, e):
        if start_event(e):
            girl.action = 0  # 기본 상태 (1행 1열)
            girl.face_dir = 1
        elif right_down(e) or left_up(e):
            girl.action = 1  # 오른쪽 (2행 1열)
            girl.face_dir = 1
        elif left_down(e) or right_up(e):
            girl.action = 3  # 왼쪽 (4행 1열)
            girl.face_dir = -1
        elif top_down(e):
            girl.action = 2  # 위쪽 (3행 1열)
            girl.face_dir = 1
        elif bottom_down(e):
            girl.action = 0  # 아래쪽 (1행 1열)
            girl.face_dir = 1

        girl.frame = 0
        girl.wait_time = get_time()

    @staticmethod
    def exit(girl, e):
        if space_down(e):
            girl.fire_ball()

    @staticmethod
    def do(girl):
        girl.frame = (girl.frame + 1) % 8
        if get_time() - girl.wait_time > 2:
            girl.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(girl):
        girl.image.clip_draw(0, girl.action * 32, 32, 32, girl.x, girl.y)



class Sleep:
    @staticmethod
    def enter(girl, e):
        if start_event(e):
            girl.face_dir = 1
            girl.action = 3
        girl.frame = 0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        girl.frame = (girl.frame + 1) % 8

    @staticmethod
    def draw(girl):
        if girl.face_dir == 1:
            girl.image.clip_composite_draw(girl.frame * 100, 300, 100, 100,
                                          3.141592 / 2, '', girl.x - 25, girl.y - 25, 100, 100)
        else:
            girl.image.clip_composite_draw(girl.frame * 100, 200, 100, 100,
                                          -3.141592 / 2, '', girl.x + 25, girl.y - 25, 100, 100)


class Run:
    @staticmethod
    def enter(girl, e):
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            girl.dir, girl.face_dir, girl.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
            girl.dir, girl.face_dir, girl.action = -1, -1, 0

    @staticmethod
    def exit(girl, e):
        if space_down(e):
            girl.fire_ball()


    @staticmethod
    def do(girl):
        girl.frame = (girl.frame + 1) % 8
        girl.x += girl.dir * 5
        pass

    @staticmethod
    def draw(girl):
        girl.image.clip_draw(girl.frame * 100, girl.action * 100, 100, 100, girl.x, girl.y)





class Girl:

    def __init__(self):
        self.x, self.y = 400, 90
        self.face_dir = 1
        self.image = load_image('animation_sheet1.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, space_down: Idle},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Run},
                Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run, space_down: Idle}
            }
        )
        self.set_item('NONE')

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        # 여기서 받을 수 있는 것만 걸러야 함. right left  등등..
        self.state_machine.add_event(('INPUT', event))
        pass

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
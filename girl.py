from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from state_machine import *
from ball import Ball, BigBall
import game_world


class Idle:
    @staticmethod
    def enter(girl, e):
        girl.dir, girl.face_dir, girl.action = 0, 1, 0
        girl.frame = 0

    @staticmethod
    def exit(girl, e):
        if space_down(e):
            girl.fire_ball()

    @staticmethod
    def do(girl):
        girl.frame = (girl.frame + 1) % 4

    @staticmethod
    def draw(girl):
        girl.image.clip_draw(girl.frame * 16, girl.action * 32, 16, 32, girl.x, girl.y)


class Run:
    @staticmethod
    def enter(girl, e):
        if right_down(e):
            girl.dir, girl.face_dir, girl.action = 1, 1, 1
        elif left_down(e):
            girl.dir, girl.face_dir, girl.action = -1, -1, 3

    @staticmethod
    def exit(girl, e):
        if space_down(e):
            girl.fire_ball()

    @staticmethod
    def do(girl):
        girl.frame = (girl.frame + 1) % 4
        girl.x += girl.dir * 5

    @staticmethod
    def draw(girl):
        girl.image.clip_draw(girl.frame * 16, girl.action * 32, 16, 32, girl.x, girl.y)


class Girl:
    def __init__(self):
        self.x, self.y = 400, 90
        self.face_dir = 1
        self.image = load_image('animation_sheet1.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: Run, left_down: Run, left_up: Idle, right_up: Idle, space_down: Idle},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Run},
            }
        )
        self.set_item('NONE')

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
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

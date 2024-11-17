from pico2d import *
import game_framework
import game_world
from door import Door
from girl import Girl
import yard


image = None
doors = []
width, height = 1440, 960  # Yard 크기
girl = None



def init():
    global image, girl
    image = load_image('livingroom.png')  # 배경 이미지 로드
    door = Door(width=32, height=32)  # Initialize door size

    if not girl:  # Use the existing girl instance
        girl = Girl()
        game_world.add_object(girl, 2)

        # Reset girl's position and constraints for the living room
    girl.x, girl.y = 300, 200
    girl.min_x, girl.max_x = 200, 1240
    girl.min_y, girl.max_y = 150, 810



def draw():
    global image
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)  # 배경 그리기
    game_world.render()
    update_canvas()

def handle_events():
    girl = game_world.get_object_by_class(Girl)  # game_world에서 girl 객체 가져오기
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if 300 <= girl.x <= 360 and 100 <= girl.y <= 120:  # 특정 범위 확인
                game_framework.change_mode(yard)

        else:
            if girl:
                girl.handle_event(event)

def update():
    global girl
    if girl:
        # Constrain girl's movement within the living room's boundaries
        girl.x = max(girl.min_x, min(girl.max_x, girl.x))
        girl.y = max(girl.min_y, min(girl.max_y, girl.y))
    game_world.update()

def pause(): pass
def resume(): pass
def finish():
    global image
    del image
    doors.clear()


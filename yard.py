from pico2d import *
import game_framework
import game_world
from door import Door
from girl import Girl
import livingroom

image = None
door = None
door_x, door_y = 720, 550  # 문 위치
width, height = 1440, 960  # Yard 크기
girl = None
last_used_door = None

def init():
    global image, door, girl, last_used_door
    image = load_image('yard.png')
    door = Door()

    girl = game_world.get_object_by_class(Girl)
    if not girl:
        girl = Girl()
        game_world.add_object(girl, 2)

    # 마지막 사용된 문에 따라 초기 위치 설정
    if last_used_door == 'door1':
        girl.x, girl.y = 720, 550
    else:  # 기본 위치
        girl.x, girl.y = 500, 500

def draw():
    global image, door
    clear_canvas()
    image.draw_to_origin(0, 0, width, height)
    door.draw(door_x, door_y)
    game_world.render()
    update_canvas()

def handle_events():
    global girl, last_used_door
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            distance = ((girl.x - door_x) ** 2 + (girl.y - door_y) ** 2) ** 0.5
            if distance <= 30:
                last_used_door = 'door1'
                game_framework.change_mode(livingroom)
        else:
            if girl:
                girl.handle_event(event)

def update():
    if girl:
        girl.x = max(500, min(820, girl.x))
        girl.y = max(475, min(530, girl.y))
    game_world.update()

def finish():
    global image, door
    del image
    del door

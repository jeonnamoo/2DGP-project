from pico2d import *
import game_world
import game_framework
import yard
from girl import Girl
import livingroom

running = True
current_mode = "yard"  # 현재 모드 상태 (yard 또는 livingroom)
girl = None

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_SPACE:
                # 특정 조건에서 전환
                if 720 <= girl.x <= 752 and girl.y >= 520:
                    import livingroom
                    game_framework.change_mode(livingroom)
        else:
            girl.handle_event(event)

def reset_world():
    global girl, current_mode

    game_world.clear()


    girl = Girl()
    game_world.add_object(girl, 1)  # Girl 객체 추가




open_canvas(1440, 960)
reset_world()

while running:
    handle_events()
    game_world.update()
    clear_canvas()
    game_world.render()
    update_canvas()
    delay(0.01)

close_canvas()
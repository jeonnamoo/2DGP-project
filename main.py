import game_framework
from pico2d import open_canvas, delay, close_canvas
# logo_mode 를 임포트 하되 이름을 바꾼다. start_mode.
import logo_mode as start_mode

open_canvas(1440, 960)
game_framework.run(start_mode)
close_canvas()

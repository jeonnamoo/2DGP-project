from pico2d import *

open_canvas()
sound = load_wav('mop1.wav')
sound.set_volume(128)
sound.play()
delay(1)  # 소리가 들릴 만큼 대기
close_canvas()

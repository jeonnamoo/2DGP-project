from pico2d import *
import game_world

class Door:
    image = None
    sound = None  # 사운드 추가

    def __init__(self, width=32, height=32, scale=4):  # 기본 크기와 배율 설정
        if Door.image is None:
            Door.image = load_image('door.png')  # 문 이미지 로드
        if Door.sound is None:
            Door.sound = load_wav('door2.mp3')  # 문 사운드 로드
            Door.sound.set_volume(64)  # 볼륨 설정 (0~128)

        self.width, self.height = width * scale, height * scale  # 문 크기를 4배로 설정

    def draw(self, x, y):
        """문 이미지를 크기 조정하여 주어진 위치(x, y)에 그리기"""
        self.image.draw_to_origin(x - self.width // 2, y - self.height // 2, self.width, self.height)

    def play_sound(self):
        """문 사운드 재생"""
        if Door.sound:
            Door.sound.play()

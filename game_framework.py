import basement
import bedroom
import gage
import kitchen
import library
import livingroom
import yard

import time

running = None
stack = None
frame_time = 0.0  # frame_time 초기화

current_map = None  # 현재 맵을 추적할 전역 변수

def change_mode(mode):
    global stack, current_map
    if stack:
        stack[-1].finish()
        stack.pop()
    stack.append(mode)
    mode.init()
    current_map = mode  # 맵을 변경할 때 현재 맵 업데이트



def push_mode(mode):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    global stack
    if (len(stack) > 0):
        # execute the current mode's finish function
        stack[-1].finish()
        # remove the current mode
        stack.pop()

    # execute resume function of the previous mode
    if (len(stack) > 0):
        stack[-1].resume()


def quit():
    global running
    running = False


def run(start_mode):
    global running, stack, frame_time
    running = True
    stack = [start_mode]
    start_mode.init()


    current_time = time.time()
    while running:
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()

        # frame_time 계산
        new_time = time.time()
        frame_time = new_time - current_time
        current_time = new_time

    while stack:
        stack[-1].finish()
        stack.pop()
    # gage 상태 지속적으로 업데이트
    if gage:
        total_objects, removed_objects = count_removed_objects()
        removed_percentage = removed_objects * 0.66
        gage.update_level(min(removed_percentage, 100))

def count_removed_objects():
    """제거된 객체 수 계산"""
    total_objects = 150  # 총 객체 수 고정
    removed_objects = 0

    for map_name in [yard, basement, bedroom, kitchen, livingroom, library]:
        # 각 맵의 객체 리스트를 안전하게 접근
        for obj_list_name in ['web_list', 'stain_list', 'can_list']:
            obj_list = getattr(map_name, obj_list_name, [])
            for obj, _, _ in obj_list:
                if obj.removed:  # 제거된 객체만 카운트
                    removed_objects += 1

    return total_objects, removed_objects

def update_gage(gage):
    """gage 업데이트 로직"""
    total_objects, removed_objects = count_removed_objects()

    # Gage에 업데이트
    gage.update_level(removed_objects)  # removed_objects로 변경

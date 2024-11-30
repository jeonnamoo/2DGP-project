import basement
import kitchen
import library
import livingroom
import yard

running = None
stack = None



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
    global running, stack
    running = True
    stack = [start_mode]
    start_mode.init()

    while running:
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()

    while stack:
        stack[-1].finish()
        stack.pop()

def count_removed_objects():
    """모든 맵의 객체를 추적하여 제거 상태 계산"""
    total_objects = 0
    removed_objects = 0

    for map_name in [yard, basement, kitchen, livingroom, library]:
        # 각 맵의 객체 리스트를 안전하게 접근
        for obj_list_name in ['web_list', 'stain_list', 'can_list']:
            obj_list = getattr(map_name, obj_list_name, [])
            for obj, _, _ in obj_list:
                total_objects += 1
                if obj.removed:
                    removed_objects += 1

    return total_objects, removed_objects



def update_gage(gage):
    """gage 업데이트 로직"""
    total_objects, removed_objects = count_removed_objects()
    if total_objects == 0:
        return  # 객체가 없으면 아무 것도 하지 않음

    removed_percentage = (removed_objects / total_objects) * 100
    gage.update_level(removed_percentage)

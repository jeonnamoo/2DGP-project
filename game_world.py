world = [[], [], [], []]  # 레이어: 0 = 배경, 1 = 문, 2 = 캐릭터, 3 = UI 등


def add_object(o, depth=0):
    if 0 <= depth < len(world):
        world[depth].append(o)
        print(f"Object {o.__class__.__name__} added to layer {depth}")  # 디버깅 메시지
    else:
        raise ValueError(f"Invalid depth {depth}: Object not added to any layer.")


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise ValueError('Cannot delete non-existing object')


def clear():
    for layer in world:
        layer.clear()


def get_object_by_class(cls):
    """특정 클래스의 첫 번째 객체를 반환합니다."""
    for layer in world:
        for obj in layer:
            if isinstance(obj, cls):
                return obj
    return None  # 해당 클래스의 객체가 없으면 None 반환

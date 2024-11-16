world = [[], [], [], []]  # 레이어: 0 = 배경, 1 = Door, 2 = 캐릭터, 3 = UI 등


def add_object(o, depth=0):
    if 0 <= depth < len(world):
        world[depth].append(o)
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

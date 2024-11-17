world = [[], [], [], []]  # 레이어: 0 = 배경, 1 = 문, 2 = 캐릭터, 3 = UI 등


def add_object(o, depth = 0):
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol

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
    for layer in world:
        for o in layer:
            if isinstance(o, cls):
                return o
    return None
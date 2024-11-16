world = [[], [], [], []]


def add_object(o, depth=0):
    if 0 <= depth < len(world):
        world[depth].append(o)


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

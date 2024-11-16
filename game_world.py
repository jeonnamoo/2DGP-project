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


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)


    return None


def get_object_by_class(cls):
    """특정 클래스의 첫 번째 객체를 반환합니다."""
    for layer in world:
        for obj in layer:
            if isinstance(obj, cls):
                return obj
    return None  # 해당 클래스의 객체가 없으면 None 반환

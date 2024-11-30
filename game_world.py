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

def replace_attached_object(new_object_class, attached_object, girl):
    """
    기존 부착된 오브젝트를 제거하고 새 오브젝트를 부착합니다.
    """
    if attached_object:  # 기존 부착된 오브젝트가 있으면 제거
        remove_object(attached_object)
        attached_object.detach()

    # 새로운 오브젝트 생성 및 부착
    new_object = new_object_class()
    new_object.attach(girl)
    add_object(new_object, 1)
    return new_object  # 새로 부착된 오브젝트 반환

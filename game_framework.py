import information_mode


stack = None


def change_mode(mode):
    global stack
    if stack:
        stack[-1].finish()  # 현재 모드 종료
        stack.pop()
    stack.append(mode)
    mode.init()



def push_mode(mode):
    global stack
    if stack:
        stack[-1].pause()
    stack.append(mode)
    mode.init()  # 모드 초기화 함수 호출

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

def push_information_mode(mode):
    global stack
    if mode not in stack:
        stack.append(mode)
        mode.init()

def pop_information_mode():
    global stack
    if stack and isinstance(stack[-1], information_mode.InformationMode):
        stack[-1].finish()
        stack.pop()


def run(start_mode):
    global running, stack
    running = True
    stack = [start_mode]
    start_mode.init()

    while running:
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()

        # 정보 패널 모드가 활성화된 경우 최상위에서 렌더링
        for mode in stack:
            if isinstance(mode, information_mode.InformationMode):
                mode.draw()

    while stack:
        stack[-1].finish()
        stack.pop()
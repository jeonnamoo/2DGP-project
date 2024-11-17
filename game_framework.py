running = None
stack = None


def change_mode(mode):
    global stack
    if len(stack) > 0:
        # 현재 스택의 최상위 모드의 종료 함수를 실행합니다.
        stack[-1].finish()
        # 현재 스택의 최상위 모드를 제거합니다.
        stack.pop()
    # 새로운 모드를 스택에 추가합니다.
    stack.append(mode)
    # 추가된 모드의 초기화 함수를 실행합니다.
    mode.init()


def push_mode(mode):
    global stack
    if len(stack) > 0:
        # 현재 스택의 최상위 모드의 일시 중지(pause) 함수를 실행합니다.
        stack[-1].pause()
    # 새로운 모드를 스택에 추가합니다.
    stack.append(mode)
    # 추가된 모드의 초기화 함수를 실행합니다.
    mode.init()


def pop_mode():
    global stack
    if len(stack) > 0:
        # 현재 스택의 최상위 모드의 종료 함수를 실행합니다.
        stack[-1].finish()
        # 현재 스택의 최상위 모드를 제거합니다.
        stack.pop()

    if len(stack) > 0:
        # 스택에 남아 있는 이전 모드의 재개(resume) 함수를 실행합니다.
        stack[-1].resume()


def quit():
    global running
    # 게임 실행 상태를 False로 설정하여 루프를 종료합니다.
    running = False


def run(start_mode):
    global running, stack
    # 게임 실행 상태를 True로 설정합니다.
    running = True
    # 스택을 초기화하고, 시작 모드를 스택에 추가합니다.
    stack = [start_mode]
    # 시작 모드의 초기화 함수를 실행합니다.
    start_mode.init()

    # 실행 루프
    while running:
        # 스택 최상위 모드의 이벤트 처리 함수를 실행합니다.
        stack[-1].handle_events()
        # 스택 최상위 모드의 업데이트 함수를 실행합니다.
        stack[-1].update()
        # 스택 최상위 모드의 그리기(draw) 함수를 실행합니다.
        stack[-1].draw()

    # 실행이 종료되면 스택에 남아 있는 모든 모드를 삭제합니다.
    while len(stack) > 0:
        # 각 모드의 종료 함수를 실행합니다.
        stack[-1].finish()
        # 스택에서 제거합니다.
        stack.pop()

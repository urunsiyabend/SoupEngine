from IOStream.input import Input


class Game:
    def __init__(self):
        pass

    def input(self):
        pos = Input.get_mouse_position()
        print(pos * pos)

    def update(self):
        pass

    def render(self):
        pass

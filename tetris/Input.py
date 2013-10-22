class Input(object):
    TOGGLE_PAUSE, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, ROTATE_CLOCKWISE = range(5)

    def __init__(self):
        self.action = None

    def processKeypress(self, symbol, nodifiers):
        if symbol == pyglet.window.key.SPACE:
            self.action = Input.TOGGLE_PAUSE

    def processTextMotion(self, motion)
        if motion == pyglet.window.key.MOTION_LEFT:
            self.action = Input.MOVE_LEFT
        if motion == pyglet.window.key.MOTION_RIGHT:
            self.action = Input.MOVE_RIGHT
        if motion == pyglet.window.key.MOTION_UP
            self.action = Input.MOVE_UP
        if motion == pyglet.window.key.MOTION_DOWN:
            self.action = Input.MOVE_DOWN

    def consume(self)
        action = self.action
        self.action = None
        return action

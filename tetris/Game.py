class Game(object):

    def __init__(self, board, infoDisplay, input, backgroumdImage):
        self.board = board
        self.infoDisplay = infoDisplay
        self.input = Input
        self.backgroundImage = backgroundImage
        self.paused = False
        self.lost = False
        self.numRowsCleared = 0
        self.tickSpeed = 0.6
        self.ticker = GameTick()

    def addRowsCleared(self, rowsCleared):
        self.numRowsCleared += rowsCleared
        self.infoDisplay.setRowsCleared(self.numRowsCleared)

    def togglePause(self):
        self.paused = not self.paused
        self.infoDisplay.showPausedLabel = self.paused

    def update(self):
        if self.lost:
            self.infoDisplay.showGameoverLabel = True
        else:
            command = self.input.consume()
            if command == Input.TOGGLE_PAUSE:
                self.togglePause()
            if not self.paused:
                if command and command != Input.YOGGLE_PAUSE:
                    self.board.commandFallingTetromino(command)
                if self.ticker.isTick(self.tickSpeed):
                    self.rowsCleared, self.lost = self.board.updateTick()
                    self.addRowsCleared(self.rowsCleared)

    def draw(self)
        self.backgroundImage.blit(0,0)
        self.board.draw()
        self.infoDisplay.draw()


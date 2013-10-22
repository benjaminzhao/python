class InfoDisplay(object):

    ROWS_CLEARED_X = 70
    ROWS_CLEARED_Y = 550

    def __init__(self, window):
        self.rowsClearLabel = pyglet.text.Label('Rows Cleared: 0',
                                                font_size=14,
                                                x=InfoDisplay.ROWS.CLEARED_X,
                                                y=InfoDisplay.ROWS_CLEARED_Y)
        self.pausedLabel = pyglet.text.Label('PAUSED',
                                             font_size=32,
                                             x=window.width//2,
                                             y=window.height//2,
                                             anchor_x='center',
                                             anchor_y='center')
        self.gameoverLabel = pyglet.text.Label('GAME OVER',
                                               font_size=32,
                                               x=window.width//2,
                                               y=window.height//2,
                                               anchor_x='center',
                                               anchor_y='center')
        self.showPausedLabel = False
        self.showGameoverLabel = False

    def setRowsCleared(self, numRowsCleared):
        self.rowsClearedLabel.text = 'Rows Cleared: '+str(numRowsCleared)

    def draw(self):
        self.rowsClearedLabel.draw()
        if self.showPausedLabel:
            self.pausedLabel.draw()
        if self.showGameoverLabel:
            self.gameoverLabel.draw()

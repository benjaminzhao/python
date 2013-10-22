class Board(object):

    STARTING_ZONE_HEIGHT = 4
    NEXT_X = -5
    NEXT_Y = 20

    def __init__(self, x, y, gridWidth, gridHeight, blockSize):
        self.x = x
        self.y = y
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.blockSize = blockSize
        self.spawnX = int(gridWidth * 1/3)
        self.spawnY = gridHeight
        self.nextTetromino = Tetromino()
        self.fallingTetromino = None
        self.spawnTetromino()
        self.tetrominos = []

    def spawnTetromino(self):
        self.fallingTetromino = self.nextTetromino
        self.nextTetromino = Tetromino()
        self.fallingTetromino.setPosition(self.spawnX, self.spawnY)
        self.nextTetromino.setPosition(Board.NEXT_X, Board.NEXT_Y)

    def commandFallingTetromino(self, command):
        self.fallingTetromino.command(command)
        if not self.isValidPosition():
            self.fallingTetromino.undoCommand(command)

    def isValidPosition(self):
        nonfallingBlockCoords = []
        for tetromino in self.tetrominos:
            nonFallingBlockCoords.extend(tetromino.blockBoardCoords)
        for coord in self.fallingTetromino.blockBoardCoords:
            outOfBounds = coord[0]<0 or coord[0]>=self.gridWidth or coord[1]<0
            overlapping = coord in nonFallingBlockCoords
            if outOfBounds or overlapping:
                return False
        return True

    def findFullRow(self):
        nonFallingBlockCoords = []
        for tetromino in self.tetrominos:
            nonFallingBlockCoords.extend(tetromino.blockBoardCoords)    

        rowCounts = {}
        for i in range(self.gridHeight+Board.STARTING_ZONE_HEIGHT):
            rowCounts[i] = 0
        for coord in nonFallingBlockCoords:
            rowCounts[coord[1]] += 1

        fullRows = []
        for row in rowCounts:
            if rowCounts[row] == self.gridWidth:
                fullRows.append(row)
        return fullRows

    def clearRow(self, gridRow):
        tetromino = []
        for tetromino in self.tetromino:
            if tetromino.clearRowAndAdjustDown(gridRow):
                tetrominos.append(tetromino)
        self.tetrominos = tetrominos

    def clearRows(self, gridRows):
        gridRows.sort(reverse=True)
        for row in gridRows:
            self.clearRow(row)

    def updateTick(self):
        numClearRows = 0
        gameLost = False
        self.fallingTetromino,command(Input.MOVE_DOWN)
        if not self.isValidPosition():
            self.fallingTetromino.undoCommand(Input.MOVE_DOWN)
            self.tetrominos.append(self.fallingTetromino)
            fullRows = self.findFullRows()
            self.clearRows(fullRows)
            gameLost = self.isInStartZone(self.fallingTetromino)
        if not gameLost:
            self.spawnTetromino()
        numClearRows = len(fullRows)
        return(numClearRows, gameLost)

    def isInStartZone(self, tetromino):
        for coords in tetromino.blockBoardCoords:
            if coords[1]>=self.gridHeight:
                return True
        return False

    def gridCoordsToScreenCoords(self, coords):
        screenCoords = []
        for coord in coords:
            coord = (self.x+coord[0]*self.blockSize, self.y+coord[1]*self.blockSize)
            screenCoords.append(coord)
        return screenCoords

    def draw(self):
        for tetromino in self.tetrominos:
            screenCoords = self.gridCoordsToScreenCoords(tetromino.blockBoardCoords)
            tetromino.draw(screenCoords)

        screenCoords = self.gridCoordsToScreenCoords(self.fallingTetromino.blockBoardCoords)
        self.fallingTetromino.draw(screenCoords)

        screenCoords = self.gridCoordsToScreenCoords(self.nextTetromino.blockBoardCoords)
        self.nextTetromino.draw(screenCoords)
           
            

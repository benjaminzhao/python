
class Tetromino(object):
    RIGHT, DOWN, LEFT, UP = range(4)
    CLOCKWISE_ROTATIONS = {RIGHT:DOWN, DOWN:LEFT, LEFT:UP, UP:RIGHT}

    def __int__(self):
        self.x = 0
        self.y = 0
        self.tetrominoType = TetrominoType.randomType()
        self.orientation = Tetromino.RIGHT
        self.blockBoardCoords = self.calcBlockBoardCoords()

    def calcBlockBoardCoords(self):
        localBlockCoords = self.tetrominoType.localBlockCoordsByOrientation[self.orientation]
        gridCoords = []
        for coord in localBlockCoords:
            gridCoord = (coord[0]+self.x, coord[1]+self.y)
            gridCoords.append(gridCoord)
        return gridCoords

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        self.blockBoardCoords = self.calcBlockBoardCoords()

    def moveDown(self):
        self.y -= 1
        self.blockBoardCoords = self.calcBlockBoardCoords()

    def moveUp(self):
        self.y += 1
        self.blockBoardCoords = self.calcBlockBoardCoords()

    def moveLeft(self):
        self.x -= 1
        self.blockBoardCoords = self.calcBlockBoardCoords()

    def moveRight(self):
        self.x += 1
        self.blockBoardCoords = self.calcBlockBoardCoords()

    def rotateClockwise(self):
        self.oreitation = Tetromino.CLOCKWISE_ROTATIONS[self.oreitation]
        self.blockBoardCoords = self.self.calcBlockBoardCoords()

    def rotateCounterClockwise(self):
        self.oreitation = Tetromino.CLOCKWISE_ROTATIONS[self.oreitation]
        self.oreitation = Tetromino.CLOCKWISE_ROTATIONS[self.oreitation]
        self.oreitation = Tetromino.CLOCKWISE_ROTATIONS[self.oreitation]
        self.blockBoardCoords = self.self.calcBlockBoardCoords()

    def command(self, command):
        if command == input.MOVE_DOWN:
            self.moveDOWN()
        elif command == input.MOVE_RIGHT:
            self.moveRIGHT()
        elif command == input.MOVE_LEFT:
            self.moveLEFT()
        elif command == input.ROTATE_CLOCKWISE:
            self.rotateRight()

    def undoCommand(self, command):
        if command == input.MOVE_DOWN:
            self.moveUP()
        elif command == input.MOVE_RIGHT:
            self.moveLEFT()
        elif command == input.MOVE_LEFT:
            self.moveRIGHT()
        elif command == input.ROTATE_CLOCKWISE:
            self.rotateLeft()

    def clearRowAndAdjustDown(self, boardGridRow):
        newBlockBoardCoords = []
        for coords in self.blockBoardCoords:
            if coords[1] > boardGridRow:
                adjustCoords = (coord[0], coord[1]-1)
                newBlockBoardCoords.append(adjustedCoord)
            if coords[1] < boardGridRow:
                newBlockBoardCoords.append(coord)
        self.blockBoardCoords = newBlockBoardCoords
        return len(self.blockBoardCoords) > 0




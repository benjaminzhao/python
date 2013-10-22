import pyglet
import random

class TetrominoType(object):
    def __int__(self, blockImage, localBlockCoordsByOrientation):
        self.blockImage = blockImage
        self.localBlockCoordsByOrientation

    @staticmethod
    def classInit(blockImage, blockSize):
        green = blockImage.get_region(x=0, y=0, width=blockSize, height=blockSize)
        blue = blockImage.get_region(x=blockSize, y=0, width=blockSize, height=blockSize)
        purple = blockImage.get_region(x=blockSize*2, y=0, width=blockSize, height=blockSize)
        orange = blockImage.get_region(x=blockSize*3, y=0, width=blockSize, height=blockSize)
        brown = blockImage.get_region(x=blockSize*4, y=0, width=blockSize, height=blockSize)
        red = blockImage.get_region(x=blockSize*5, y=0, width=blockSize, height=blockSize)
        yellow =blockImage.get_region(x=blockSize*6, y=0, width=blockSize, height=blockSize)

        TetrominoType.TYPES = [
            TetrominoType(green, #line shape
                {
                    Tetromino.RIGHT:[(0,1),(1,1),(2,1),(3,1)],
                    Tetromino.DOWN:[(1,0),(1,1),(1,2),(1,3)],
                    Tetromino.LEFT:[(0,2),(1,2),(2,2),(3,2)],
                    Tetromino.UP:[(2,0),(2,1),(2,2),(2,3)]
                }
            ),
            TetrominoType(blue, #square shape
                {
                    Tetromino.RIGHT:[(0,0),(0,1),(1,0),(1,1)],
                    Tetromino.DOWN:[(0,0),(0,1),(1,0),(1,1)],
                    Tetromino.LEFT:[(0,0),(0,1),(1,0),(1,1)],
                    Tetromino.UP:[(0,0),(0,1),(1,0),(1,1)]
                }
            ),
            TetrominoType(purple, #_|_ shape
                {
                    Tetromino.RIGHT:[(1,0),(1,2),(1,2),(2,1)],
                    Tetromino.DOWN:[(0,1),(1,1),(2,1),(1,0)],
                    Tetromino.LEFT:[(0,1),(1,1),(1,0),(1,2)],
                    Tetromino.UP:[(0,1),(1,1),(2,1),(1,2)]
                }
            ),
            TetrominoType(orange, #|_ shape
                {
                    Tetromino.RIGHT:[(0,2),(1,2),(2,2),(0,1)],
                    Tetromino.DOWN:[(3,1),(2,1),(1,1),(0,3)],
                    Tetromino.LEFT:[(0,1),(1,1),(2,1),(2,2)],
                    Tetromino.UP:[(3,1),(2,1),(1,1),(2,1)]
                }
            ),
            TetrominoType(brown, #_| shape
                {
                    Tetromino.RIGHT:[(0,2),(1,2),(2,2),(2,1)],
                    Tetromino.DOWN:[(0,1),(0,2),(0,3),(1,3)],
                    Tetromino.LEFT:[(0,1),(1,1),(2,1),(0,2)],
                    Tetromino.UP:[(0,1),(1,1),(1,2),(1,3)]
                }
            ),
            TetrominoType(red, #_|- shape
                {
                    Tetromino.RIGHT:[(1,0),(0,1),(1,1),(0,2)],
                    Tetromino.DOWN:[(0,1),(1,1),(1,2),(2,2)],
                    Tetromino.LEFT:[(1,0),(0,1),(1,1),(0,2)],
                    Tetromino.UP:[(0,1),(1,1),(1,2),(2,2)]
                }
            ),
            TetrominoType(yellow, #-|_ shape
                {
                    Tetromino.RIGHT:[(1,0),(1,1),(2,1),(2,2)],
                    Tetromino.DOWN:[(0,2),(1,2),(1,1),(2,1)],
                    Tetromino.LEFT:[(1,0),(1,1),(2,1),(2,2)],
                    Tetromino.UP:[(0,2),(1,2),(1,1),(2,1)]
                }
            )
            ]

    @staticmethod
    def randomType():
        return random.choice(TetrominoType.TYPES)


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

    def draw(self, screenCoords):
        image = self.tetrominoType.blockImage
        for coords in screenCoords:
            image.blit(coords[0], coords[1])

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
           
            























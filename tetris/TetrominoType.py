

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

import pyglet
import gametypes

##gameState = GameState()


WIDTH = 800
HEIGHT = 600
BOARD_X = 445
BOARD_Y = 13
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 24
window = pyglet.window.Window(WIDTH, HEIGHT)
window.set_vsync(False)

## load resource ##
##loadResources()
backgroundImage = pyglet.resource.image('')
blockImage = pyglet.resource.image('')
gametypes.TetrominoType.classInit(blockImage, BLOCK_SIZE)

## init game state ##
##InitializeState()
board = gametypes.board(BOARD_X, BOARD_Y, GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE)
infoDisplay = gametypes.InfoDisplay(window)
input = gametypes.Input()
game = gametypes.Game(board, infoDisplay, input, backgroundImage)


@window.event
def on_key_press(symbol, modifiers)
    input.processKeypress(symbol, modifiers)

@window.event
def on_text_motion(motion)
    input.processTextMotion(motion)

@window.event
def on_draw()
    game.draw()

def update(dt)
    game.update()

    
##    updateState()
##    renderSound()


pyglet.clock.schedule.interval(update, 1/60.0)

pyglet.app.run()

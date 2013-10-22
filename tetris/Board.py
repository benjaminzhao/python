import pyglet

WIDTH = 800
HEIGHT = 600
BOARD_X = 445
BOARD_Y = 13
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 24
window = pyglet.window.Window(WIDTH, HEIGHT)
window.set_vsync(False)



MIN_LABEL_Y = 50
MAX_LBAEL_Y = HEIGHT - 50

MIN_LABEL_X = 50
MAX_LBAEL_X = WIDTH - 50

hellolabel = pyglet.text.Label('hello world!', font_size=14, x=MIN_LABEL_X, y=MIN_LABEL_Y)
goodbylabel = pyglet.text.Label('Goodby world!', font_size=14, x=MIN_LABEL_X, y=MIN_LABEL_Y)
label = hellolabel
backgroundImage = pyglet.resource.image('bg.png')

@window.event
def on_key_press(symbol, modifiers):
    global label
    global MIN_LABEL_Y
    global MAX_LABEL_Y
    global MIN_LABEL_X
    global MAX_LBAEL_X
    
    if symbol == pyglet.window.key.SPACE:
        if label == hellolabel:
            label = goodbylabel
        else:
            label = hellolabel
    elif symbol == pyglet.window.key.UP:
        label.y += 1
        if label.y > MAX_LABEL_Y:
            label.y = MIN_LABEL_Y
            
    elif symbol == pyglet.window.key.DOWN:
        label.y -= 1
        if label.y < MIN_LABEL_Y:
            label.y = MAX_LABEL_Y
            
    elif symbol == pyglet.window.key.LEFT:
        label.x -= 1
        if label.x < MIN_LABEL_X:
            label.x = MAX_LABEL_X
            
    elif symbol == pyglet.window.key.RIGHT:
        label.x += 1
        if label.x > MAX_LABEL_X:
            label.x = MIN_LABEL_X
@window.event
def on_draw():
    ##renderScreen()
    window.clear()
    backgroundImage.blit(0,0)
    label.draw()
def update(dt):
    label.y += 1
    if label.y > MAX_LABEL_Y:
        label.y = MIN_LABEL_Y
##    updateState()
##    renderSound()


##pyglet.clock.schedule.interval(update, 1/60.0)

pyglet.app.run()

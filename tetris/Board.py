import pyglet

##loadResources()
##gameState = GameState()
##InitializeState()

MIN_LABEL_Y = 200
MAX_LBAEL_Y = 400


window = pyglet.window.Window(320, 240)
hellolabel = pyglet.text.Label('hello world!', font_size=14, x=0, y=MIN_LABEL_Y)
goodbylabel = pyglet.text.Label('Goodby world!', font_size=14, x=0, y=MIN_LABEL_Y)
label = hellolabel

def on_key_press(symbol, modifiers):
    global label
    if symbol == pyglet.window.key.SPACE:
        if label == hellolabel:
            label = goodbylabel
        else:
            label = hellolabel


def on_draw():
    ##renderScreen()
    window.clear()
    label.draw()

def update(dt):
    label.y += 1
    if label.y > MAX_LABEL_Y:
        label.y = MIN_LABEL_Y
##    updateState()
##    renderSound()


pyglet.clock.schedule.interval(update, 1/60.0)

pyglet.app.run()

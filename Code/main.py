import pyglet
from pyglet.window import Window
from pyglet import app

import euclid3

display = pyglet.canvas.Display()
print(display)
screen = display.get_default_screen()
screen_width = screen.width
screen_height = screen.height

win = Window(screen.width, screen_height)

@win.event
def on_key_press(symbol, modifiers):
    pass

@win.event
def on_draw():
    pass


if __name__ == '__main__':
    app.run()


import pyglet

from Drawer import Drawer
from Page import PageStack
from Timer import Timer

window = pyglet.window.Window(800, 600, "Whiteboard", resizable=True)

pages = PageStack()
@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.DOWN:
        pages.current_index += 1
        if pages.current_index >= pages.get_size():
            pages.Push()
    elif symbol == pyglet.window.key.UP:
        if pages.get_current_page().is_empty() and pages.current_index == pages.get_size() - 1:
            pages.Pop()
        pages.current_index -= 1
    
    print("We have {0} pages".format(pages.get_size()))

is_drawing = False
is_pen_drawing = False

tablets = pyglet.input.get_tablets()

if len(tablets) > 0:
    tablet = tablets[0]
    tablet = tablet.open(window)

    @tablet.event
    def on_motion(cursor, x, y, pressure, a, b):
        global is_pen_drawing

        if pressure > 0:
            is_pen_drawing = True
            point = (x, y)

            pages.get_current_page().get_drawer().add_point(point)
        else:
            is_pen_drawing = False


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        global is_drawing

        is_drawing = True

@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        global is_drawing

        is_drawing = False

        pages.get_current_page().get_drawer().add_point(None)

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if is_drawing and not is_pen_drawing:
        point = (x, y)
        pages.get_current_page().get_drawer().add_point(point)

pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

draw_benchmarking = open("Files/draw_benchmarking.txt", "w")

pyglet.gl.glLineWidth(3.0)
@window.event
def on_draw():
    t = Timer()
    window.clear()

    pages.get_current_page().get_drawer().draw()

    draw_benchmarking.write(str(t.get_microseconds()) + '\n')
    print(t.str_microseconds())

pyglet.app.run()
draw_benchmarking.close()
import pyglet

from Point import Point
import Color
from Timer import Timer


window = pyglet.window.Window(800, 600, "Whiteboard", resizable=True)

batch = pyglet.graphics.Batch()

points = []

def add_point(point):
    if point is not None:
        points.append(Point(point))

        index = len(points) - 1

        if index > 1:
            if points[index - 1] is not None:
                data = batch.add(
                        2, pyglet.gl.GL_LINES, None, 
                        ('v2f', (points[index - 1].x, points[index - 1].y, points[index].x, points[index].y)),  #Position
                        ('c4B', Color.WHITE.get_rgba() * 2),                                                    #Color
                    )
                for vertex in data.colors:
                    print(vertex)
    else:
        points.append(None)


pyglet.gl.glLineWidth(3)

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
            #print("Pen Position: ({0}, {1})".format(x, y))
            is_pen_drawing = True
            pos = (x, y)
            if pos not in points:
                add_point(pos)
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

        add_point(None)

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if is_drawing and not is_pen_drawing:
        pos = (x, y)
        add_point(pos)

pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

draw_benchmarking = open("Files/draw_benchmarking.txt", "w")

@window.event
def on_draw():
    window.clear()
    
    t = Timer()

    batch.draw()
    
    draw_benchmarking.write(str(t.get_microseconds()) + '\n')
    print(t.str_microseconds())

pyglet.app.run()
draw_benchmarking.close()
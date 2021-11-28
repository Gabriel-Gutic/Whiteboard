import pyglet

from Color import Color, WHITE
from Point import Point


class Drawer:
    def __init__(self):
        self.batch = pyglet.graphics.Batch()

        self.vertices = []
        self.current_color = WHITE

    def draw(self):
        self.batch.draw()

    def add_color(self, color : Color.Color):
        self.data.append(color)
        self.current_color = color

    def add_point(self, coords):
            self.batch.add(2, pyglet.gl.GL_POINTS,
            ('v2f', (self.data[index - 1].x, self.data[index - 1].y, self.data[index].x, self.data[index].y)),
            ('c4B', Color.WHITE.get_rgba() * 2), 
        )        





import pyglet

from Color import Color, WHITE
from Point import Point


class Drawer:
    def __init__(self):
        self.batch = pyglet.graphics.Batch()

        self.data = None
        self.last_point = None
        self.current_color = WHITE

    def draw(self):
        self.batch.draw()

    def set_current_color(self, color : Color):
        self.current_color = color

    def add_point(self, coords):
        if self.last_point is not None and coords is not None:
            self.data = self.batch.add(2, pyglet.gl.GL_LINES, None,
                ('v2f', (self.last_point[0], self.last_point[1], coords[0], coords[1])),
                ('c4B', self.current_color.get_rgba() * 2), 
            )
        self.last_point = coords
    
    def get_data(self):
        return self.data






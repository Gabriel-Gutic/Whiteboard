import pyglet

from Point import Point
import Color


class Window(pyglet.window.Window):
    def __init__(self, title="Window"):
        super(Window, self).__init__(caption=title, resizable=True)

        self._keys = []
        self._mouse_buttons = []
        self._mouse_position = Point(0, 0)
        self._background_color = Color.WHITE

    @property
    def keys(self):
        return self._keys

    @property
    def mouse_buttons(self):
        return self._mouse_buttons

    @property
    def mouse_position(self):
        return self._mouse_position
    
    @property
    def background_color(self):
        return self._background_color
    
    @background_color.setter
    def background_color(self, value):
        self._background_color = value

    @mouse_position.setter
    def mouse_position(self, mp):
        self._mouse_position = mp
import pyglet

from Point import Point


class Window(pyglet.window.Window):
    def __init__(self, title="Window"):
        super(Window, self).__init__(caption=title, resizable=True)

        self._keys = []
        self._mouse_buttons = []
        self._mouse_position = Point(0, 0)

    @property
    def keys(self):
        return self._keys

    @property
    def mouse_buttons(self):
        return self._mouse_buttons

    @property
    def mouse_position(self):
        return self._mouse_position

    @mouse_position.setter
    def mouse_position(self, mp):
        self._mouse_position = mp
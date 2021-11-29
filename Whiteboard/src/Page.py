from Drawer import Drawer
from Camera import Camera

from Point import Point


class Page:
    def __init__(self, window):
        self._drawer = Drawer()
        self._camera = Camera(window=window, pos=Point(0, 0), fov=1000)

    def update(self, dt):
        from App import Input
        from pyglet.window import mouse

        if Input.MouseButton(mouse.LEFT):
            pos = Input.MousePosition()
            point = self.camera.translate(pos.x, pos.y)
            self.drawer.add_point(point)
        else:
            self.drawer.add_point(None)

    def draw(self):
        self.drawer.draw()
    
    def is_empty(self):
        if self.drawer.get_data() is not None:
            return len(self.drawer.get_data().vertices) == 0
        return True
    
    @property
    def drawer(self):
        return self._drawer

    @property
    def camera(self):
        return self._camera


class PageStack:
    def __init__(self, window):
        self._stack = [Page(window)]
        self._current_index = 0
        self._window = window

    def Push(self):
        self.stack.append(Page(self._window))

    def Pop(self, index = None):
        if index is None:
            index = len(self.stack) - 1
        self.stack.pop(index)

    def current_page(self):
        return self.stack[self.current_index]
    
    def size(self):
        return len(self.stack)

    @property
    def current_index(self):
        return self._current_index

    @current_index.setter
    def current_index(self, ci):
        self._current_index = ci

    @property
    def stack(self):
        return self._stack
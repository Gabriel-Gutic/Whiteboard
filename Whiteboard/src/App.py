import pyglet

from Window import Window
from Camera import Camera
from Page import PageStack
from Point import Point
from Printer import print_error


class App:
    Instance = None

    def __init__(self):
        if App.Instance is not None:
            print_error("App already initialized!")
            self = None
            return
        App.Instance = self

        self._window = Window()
        self._pages = PageStack(window=self.window)

        from EventsSetup.Events import setup_events
        setup_events(self)

    def update(self, dt):
        self.pages.current_page().update(dt)

    def run(self):
        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
        pyglet.gl.glLineWidth(3.0)

        pyglet.clock.schedule_interval(self.update, 1/120.0)
        pyglet.app.run()

    @property
    def window(self):
        return self._window

    @property
    def pages(self):
        return self._pages

class Input:
    @staticmethod
    def Keyboard(symbol):
        return symbol in App.Instance.window.keys

    @staticmethod
    def MouseButton(button):
        return button in App.Instance.window.mouse_buttons

    @staticmethod
    def MousePosition():
        return App.Instance.window.mouse_position


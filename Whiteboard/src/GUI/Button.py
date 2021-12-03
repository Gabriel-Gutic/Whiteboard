import pyglet


class Button():
    def __init__(self, text="", width=100, height=100, x = 100, y = 100):
        self._rectangle = pyglet.shapes.Rectangle(width=width, height=height, x=x, y=y, color=(0, 0, 0))
        self._label = pyglet.text.Label(text,
                font_name='Times New Roman',
                font_size=40,
                x=x, 
                y=y,
                #anchor_x='center'
            )
    
    def draw(self):
        self._rectangle.draw()
        self._label.draw()

    @property
    def label(self):
        return self._label
    
    @label.setter
    def label(self, value):
        self._label = value

    @property
    def rectangle(self):
        return self._rectangle
    
    @rectangle.setter
    def rectangle(self, value):
        self._rectangle = value

    
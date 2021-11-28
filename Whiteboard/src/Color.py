

class Color:
    def __init__(self, r = 255, g = 255, b = 255, a = 255):
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a
    
    def set_rgb(self, r, g, b):
        self.red, self.green, self.blue = r, g, b
    
    def get_rgb(self):
        return (self.red, self.green, self.blue)
    
    def get_rgba(self):
        return (self.red, self.green, self.blue, self.alpha)

WHITE = Color(255, 255, 255, 255)
BLACK = Color(0, 0, 0, 255)

RED = Color(255, 0, 0, 255)
GREEN = Color(0, 255, 0, 255)
BLUE = Color(0, 0, 255, 255)

AQUA = Color(0, 255, 255, 255)
PURPLE = Color(128, 0, 128, 255)
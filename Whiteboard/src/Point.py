

class Point:
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y
    
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self) -> float:
        return self.x
    
    def get_y(self) -> float:
        return self.y

    def set_position(self, pos):
        if type(pos) in (tuple, list):
            x = pos[0]
            y = pos[1]
    
    def get_position(self) -> tuple:
        return (self.x, self.y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
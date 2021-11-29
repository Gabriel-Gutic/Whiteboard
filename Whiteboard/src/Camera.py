from pyglet.gl import *
from pyglet.window import key

from Point import Point


class Camera:
    def __init__(self, window, pos, fov, speed=10):
        self.position = pos
        self.fov = fov

        self.near = 1
        self.far = -1

        self.speed = speed
        self.window = window
    
    def begin(self):
        # Initialize Projection matrix
        glMatrixMode( GL_PROJECTION )
        glLoadIdentity()
        # Initialize Modelview matrix
        glMatrixMode( GL_MODELVIEW )
        glLoadIdentity()
        # Save the default modelview matrix
        glPushMatrix()
        # Clear window with ClearColor
        glClear( GL_COLOR_BUFFER_BIT )

        left, right, bottom, top = self.__dimensions__()

        # Set orthographic projection matrix
        glOrtho(left, right, bottom, top, self.near, self.far)

    def end(self):
        # Remove default modelview matrix
        glPopMatrix()
    
    #Convert mouse coordinates to world coordinates
    def translate(self, x, y):
        left, right, bottom, top = self.__dimensions__()

        #Translate on x axis
        dif = right - left
        ratio = self.window.width / dif

        trans_x = x / ratio + left

        #Translate on y axis
        dif = top - bottom
        ratio = self.window.height / dif

        trans_y = y / ratio + bottom

        return (trans_x, trans_y)        

    def __dimensions__(self):
        #Calculate orthographic camera dimensions
        aspect_ratio = self.window.width / self.window.height
        left = self.position.x - self.fov * aspect_ratio
        right = self.position.x + self.fov * aspect_ratio
        bottom = self.position.y - self.fov
        top = self.position.y + self.fov

        return (left, right, bottom, top)

    def on_key_repeat(self, symbol, modifiers):
        if symbol == key.A:
            self.position.y += self.speed
        if symbol == key.S:
            self.position.y -= self.speed
        if symbol == key.A:
            self.position.x -= self.speed
        if symbol == key.D:
            self.position.x += self.speed

    
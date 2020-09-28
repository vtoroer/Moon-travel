from math import *

class Vector:

    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def multiply(self, factor):
        self.x *= factor
        self.y *= factor
        return

    def module(self):
        mod = pow(pow(self.x, 2) + pow(self.x, 2), 0.5)
        return mod

from math import *

class Vector:

    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y
        if x < 0:
            self.phi = math.atan(y/x) + math.pi/2
        elif (x == 0) and (y >= 0):
            self.phi = math.pi/2
        elif (x == 0) and (y < 0):
            self.phi = -math.pi/2
        else:
            self.phi = math.atan(y/x)
        self.module = pow(x**2+y**2,0.5)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_phi(self):
        return self.phi
    
    def get_module(self):
        return self.module
    
    def update_by_xy(self, x, y):
        self.x = x
        self.y = y
        self.phi = math.atan(y/x)
        self.module = pow(x**2+y**2,0.5)
        
    def update_by_phi_and_module(self, phi, module):
        self.x = module * math.cos(phi)
        self.y = module * math.sin(phi)
        self.phi = phi
        self.length = module
        

    def multiply(self, factor):
        self.x *= factor
        self.y *= factor
        return

    def module(self):        
        return self.length

import math


G = 0.000000000667408
class Particle:



    def __init__(self,**kwargs):
        self.mass = kwargs.get('mass',1) # mass - kg
        self.position= kwargs.get('position',(0,0))
        self.velocity = kwargs.get('velocity',(0,0))
        self.acceleration = kwargs.get('acceleration',(0, 0)) # acceleration m/s^2
        self.angle = kwargs.get('angle',0)
        self.color = kwargs.get('color', (0,0,0))
        self.friction = kwargs.get('friction',0)

    def set_position(self, interval,gravity):
        x_pos = self.position[0] + self.velocity[0] * interval
        x_vel = self.velocity[0]
        y_pos = self.position[1] + self.velocity[1] * interval + 0.5 * gravity * math.pow(interval,2)
        y_vel = self.velocity[1] - 9.8 * interval
        self.position = (x_pos, y_pos)
        self.velocity = (x_vel, y_vel)

    def check_bounds(self, width, height,interval):
        elast = 0.75
        if self.position[0] < 0:
            x_vel = self.velocity[0] * -1 * elast
            self.position = (0, self.position[1])
        elif self.position[0] > width:
            x_vel = self.velocity[0] * -1 * elast
            self.position = (width, self.position[1])
        else:
            x_vel = self.velocity[0]
        if height - self.position[1] < 0:
            y_vel = self.velocity[1] * -1 * elast
            self.position = (self.position[0], height)
        elif height - self.position[1] > height:
            y_vel = self.velocity[1] * -1 * elast
            self.position = (self.position[0], 0)
        else:
            y_vel = self.velocity[1]

        self.velocity = (x_vel, y_vel)

    def get_angle(self):
        if self.velocity[0] == 0 or self.velocity[1] == 0:
            self.angle = 0
        else:
            self.angle = math.atan(self.velocity[1] / self.velocity[0])


class Planet(Particle):
    def __init__(self,**kwargs):
        self.object = kwargs.get('object', 0) # set to known object
        self.radius = kwargs.get('object', 1) # radius - meters
        # radius - meters # acceleration of gravity - meters/second^2
        self.grav_accel = kwargs.get('grav_accel', G * self.mass / math.pow(radius,2))

    #def get_gravity(self):
    #    if self.object == 1:
    #        gravity = 9.8 #  Earth acceleration - meters / second^2
    #    elif self.object == 2:
    #        gravity = 1.622 #   Moon acceleration - meters / second^2
    #    elif self.object == 3:
    #        gravity = 3.711 #   Mars acceleration - meters / second^2
    #    else:
    #        gravity =

class Earth(Planet):
    def __init__(self,**kwargs):
        self.mass = kwargs.get('mass',5972000000000000000000000) # mass - kg
        self.radius = kwargs.get('radius', 6371000) # radius - meters
        self.grav_accel = kwargs.get('grav_accel', 9.8) # radius - meters # acceleration of gravity - meters/second^2




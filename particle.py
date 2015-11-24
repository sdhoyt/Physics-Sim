import math
class Particle:



    def __init__(self,mass,position,velocity,acceleration):
        self.mass = mass # mass - kg
        self.position= position
        self.velocity = velocity
        self.acceleration = (0, 0) # acceleration m/s^2
        #self.angle = math.atan(self.velocity[1] / self.velocity[0])

    def set_position(self, interval):
        x_pos = self.position[0] + self.velocity[0] * interval
        x_vel = self.velocity[0]
        y_pos = self.position[1] + self.velocity[1] * interval - 0.5 * 9.8 * math.pow(interval,2)
        y_vel = self.velocity[1] - 9.8 * interval
        self.position = (x_pos, y_pos)
        self.velocity = (x_vel, y_vel)

    def check_bounds(self, width, height,interval):
        if self.position[0] < 0:
            x_vel = self.velocity[0] * -1
            self.position = (width, self.position[1])
        elif self.position[0] > width:
            x_vel = self.velocity[0] * -1
            self.position = (0, self.position[1])
        else:
            x_vel = self.velocity[0]
        if height - self.position[1] < 0:
            y_vel = self.velocity[1] * -1
            self.position = (self.position[0], height)
        elif height - self.position[1] > height:
            y_vel = self.velocity[1] * -1
            self.position = (self.position[0], 0)
        else:
            y_vel = self.velocity[1]

        self.velocity = (x_vel, y_vel)

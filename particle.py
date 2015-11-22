class Particle:
    mass = 1 # mass - kg
    initial_position = (0,0)
    position = (0, 0) # position - m
    initial_velocity = (1,1)
    velocity = (1, 1) # velocity - m/s
    acceleration = (0, 0) # acceleration m/s^2


    def set_position(self, interval):
        x_component = self.initial_position[0] + self.initial_velocity[0] * interval
        y_component = self.initial_position[1] + self.initial_velocity[1] * interval - 0.5 * 9.8 * interval ** 2
        self.position = (x_component, y_component)



import math
import random
from vector import Vector

def check_collision(particle, particle2):
    distance = abs(particle.position - particle2.position)

    if distance <= (particle.mass + particle2.mass) * 2:
        x_vel1 = (particle.velocity[0] * (particle.mass - particle2.mass) + 2 * particle2.mass * particle2.velocity[0]) / (particle.mass + particle2.mass)
        y_vel1 = (particle.velocity[1] * (particle.mass - particle2.mass) + 2 * particle2.mass * particle2.velocity[1]) / (particle.mass + particle2.mass)
        x_vel2 = (particle2.velocity[0] * (particle2.mass - particle.mass) + 2 * particle.mass * particle.velocity[0]) / (particle2.mass + particle.mass)
        y_vel2 = (particle2.velocity[0] * (particle2.mass - particle.mass) + 2 * particle.mass * particle.velocity[0]) / (particle2.mass + particle.mass)
        particle.velocity = Vector(x_vel1, y_vel1)
        particle2.velocity = Vector(x_vel2, y_vel2)

class PhysicsWorld:

    def __init__(self, width, height, **kwargs):
        self.width = width
        self.height = height
        self.particle_list = list()
        self.color = (0, 0, 0)
        #self.mass_of_air = 0.2
        self.elasticity = 0.25
        #self.acceleration = None
        # gravitational acceleration - m/s^2
        self.gravity = Vector(0, kwargs.get('gravity', -0.98))

    def update(self):
        for i, particle in enumerate(self.particle_list):
            particle.move(self)
            self.bounce(particle)
            for ii in range(i + 1, len(self.particle_list)):
                check_collision(particle, self.particle_list[ii])

    def bounce(self, particle):
        if particle.position[0] < 0:
            x_vel = particle.velocity[0] * -1 * particle.elasticity
            particle.position = (0, particle.position[1])

        elif particle.position[0] > self.width:
            x_vel = particle.velocity[0] * -1 * particle.elasticity
            particle.position = (self.width, particle.position[1])

        else:
            x_vel = particle.velocity[0]

        if self.height - particle.position[1] < 0:
            y_vel = particle.velocity[1] * -1 * particle.elasticity
            particle.position = (particle.position[0], self.height)

        elif self.height - particle.position[1] > self.height:
            y_vel = particle.velocity[1] * -1 * particle.elasticity
            particle.position = (particle.position[0], 0)

        else:
            y_vel = particle.velocity[1]

        particle.velocity = (x_vel, y_vel)

    def make_particle(self, n=1, **kwargs):

        for i in range(n):
            mass = kwargs.get('mass', random.randint(1, 10))
            position = kwargs.get(
                'position',
                (random.randint(0, self.width),
                 random.randint(0, self.height))
            )

            particle = Particle(position[0], position[1], mass)
            #particle.velocity = kwargs.get('velocity', (random.randint(0, 50), random.randint(0, 50)))
            particle.velocity = kwargs.get('velocity', (0, 0))

            particle.color = kwargs.get(
                'color',
                (random.randint(0, 254),
                 random.randint(0, 254),
                 random.randint(0, 254))
            )
            particle.elasticity = kwargs.get('elasticity', 0.50)

            self.particle_list.append(particle)

class Particle:

    def __init__(self, x, y, mass=1):
        self.position = Vector(x, y)
        self.size = mass
        self.color = (0, 0, 255)
        self.thickness = 0
        self.velocity = Vector(0, 0)
        self.angle = 0
        self.mass = mass
        self.drag = 1
        self.elasticity = 0.75

    def move(self, scene):
        self.position = self.position + self.velocity + 0.5 * scene.gravity
        self.velocity = self.velocity + scene.gravity

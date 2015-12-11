import math

class PhysicsWorld:

    def __init__(self,**kwargs):
        self.gravity = kwargs.get('gravity',-9.8) # gravitational acceleration - m/s^2
        self.interval = kwargs.get('interval', 0.2) # intervals of time - s

    def check_collision(particle, particle2):
        dx = abs(particle2.position[0] - particle.position[0])
        dy = abs(particle2.position[1] - particle.position[1])
        distance = math.hypot(dx, dy)

        if distance <= (particle.mass + particle2.mass) * 2 :
            x_vel1 = (particle.velocity[0]*(particle.mass - particle2.mass) + 2*particle2.mass*particle2.velocity[0])/(particle.mass + particle2.mass)
            y_vel1 = (particle.velocity[1]*(particle.mass - particle2.mass) + 2*particle2.mass*particle2.velocity[1])/(particle.mass + particle2.mass)
            x_vel2 = (particle2.velocity[0]*(particle2.mass - particle.mass) + 2*particle.mass*particle.velocity[0])/(particle2.mass + particle.mass)
            y_vel2 = (particle2.velocity[0]*(particle2.mass - particle.mass) + 2*particle.mass*particle.velocity[0])/(particle2.mass + particle.mass)
            particle.velocity = (x_vel1, y_vel1)
            particle2.velocity = (x_vel2, y_vel2)

    #def collide(particle, particle2):
    #    dx = abs(particle2.position[0] - particle.position[0])
    #    dy = abs(particle2.position[1] - particle.position[1])
    #    distance = math.hypot(dx, dy)
    #    x_vel1 = (particle.velocity[0]*(particle.mass - particle2.mass) + 2*particle2.mass*particle2.velocity[0])/(particle.mass + particle2.mass)
    #    y_vel1 = (particle.velocity[1]*(particle.mass - particle2.mass) + 2*particle2.mass*particle2.velocity[1])/(particle.mass + particle2.mass)
    #    x_vel2 = (particle2.velocity[0]*(particle2.mass - particle.mass) + 2*particle.mass*particle.velocity[0])/(particle2.mass + particle.mass)
    #    y_vel2 = (particle2.velocity[0]*(particle2.mass - particle.mass) + 2*particle.mass*particle.velocity[0])/(particle2.mass + particle.mass)
    #    particle.velocity = (x_vel1, y_vel1)
    #    particle2.velocity = (x_vel2, y_vel2)


class Particle:

    def __init__(self,**kwargs):
        self.mass = kwargs.get('mass',1) # mass - kg
        self.position= kwargs.get('position',(0,0))
        self.velocity = kwargs.get('velocity',(0,0))
        self.acceleration = kwargs.get('acceleration',(0, 0)) # acceleration m/s^2
        self.angle = kwargs.get('angle',0)
        self.color = kwargs.get('color', (0,0,0))
        self.friction = kwargs.get('friction',0)
        self.elasticity = kwargs.get('elasticity',0.25)

    #def move(particle_list, gravity, interval, width, height):
        #for i, particle in enumerate(particle_list):
        #    particle.set_position(interval, gravity)
        #    particle.check_bounds(width, height, interval)
        #    for ii in range(i + 1, len(particle_list)):
        #        PhysicsWorld.check_collision(particle, particle_list[ii])
    def move(scene):
        for i, particle in enumerate(scene.particle_list):
            particle.set_position(scene.world.interval, scene.world.gravity)
            particle.check_bounds(scene.width, scene.height, scene.world.interval)
            for ii in range(i + 1, len(scene.particle_list)):
                PhysicsWorld.check_collision(particle, scene.particle_list[ii])

    def set_position(self, interval,gravity):
        x_pos = self.position[0] + self.velocity[0] * interval
        x_vel = self.velocity[0]
        y_pos = self.position[1] + self.velocity[1] * interval + 0.5 * gravity * math.pow(interval,2)
        y_vel = self.velocity[1] - 9.8 * interval
        self.position = (x_pos, y_pos)
        self.velocity = (x_vel, y_vel)

    def check_bounds(self, width, height,interval):

        if self.position[0] < 0:
            x_vel = self.velocity[0] * -1 * self.elasticity
            self.position = (0, self.position[1])
        elif self.position[0] > width:
            x_vel = self.velocity[0] * -1 * self.elasticity
            self.position = (width, self.position[1])
        else:
            x_vel = self.velocity[0]
        if height - self.position[1] < 0:
            y_vel = self.velocity[1] * -1 * self.elasticity
            self.position = (self.position[0], height)
        elif height - self.position[1] > height:
            y_vel = self.velocity[1] * -1 * self.elasticity
            self.position = (self.position[0], 0)
        else:
            y_vel = self.velocity[1]

        self.velocity = (x_vel, y_vel)

    def get_angle(self):
        if self.velocity[0] == 0 or self.velocity[1] == 0:
            self.angle = 0
        else:
            self.angle = math.atan(self.velocity[1] / self.velocity[0])
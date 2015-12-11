import PhysicsKit
import pygame
import random

class Scene:

    def set_up(self):
        self.background_colour = (255, 255, 255)
        self.width = 800
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.PhysicsWorld = PhysicsKit.PhysicsWorld
        self.Particle = PhysicsKit.Particle
        self.world = self.PhysicsWorld()
        #self.particle_list = self.get_particle_list()
        self.particle_list = self.read_input('freeFalling-2.txt')

    def refresh_img(self):
        self.screen.fill(self.background_colour)
        for particle in self.particle_list:
            pygame.draw.circle(
                self.screen,
                particle.color,
                (int(particle.position[0]), self.height - int(particle.position[1])),
                particle.mass * 2, 2
            )
            pygame.display.update()

    def get_particle_list(self):
        particle_list = list()

        for i in range(0, 3):
            particle_list.append(self.Particle())
            particle_list[i].color = (random.randint(0, 254),
                                    random.randint(0, 254),
                                    random.randint(0, 254))
            particle_list[i].mass = random.randint(2, 10)
            particle_list[i].position = (random.randint(5, 750),
                                        random.randint(5, 750))
            particle_list[i].velocity = (random.randint(-200, 200),
                                        random.randint(-200, 200))
            particle_list[i].elasticity = 0.25

        return particle_list

    def read_input(self, input_file):
        particle_list = list()
        inputFile = open(input_file)
        input = inputFile.readlines()
        new_input = list()
        for index in range(0, len(input)):
            if input[index][0] != '#':
                new_input.append(input[index])
        number_of_particles = int(new_input[0])
        del new_input[0]
        for index in range(0, number_of_particles):
            random_int1 = random.randint(0,254)
            random_int2 = random.randint(0,254)
            random_int3 = random.randint(0,254)

            particle_list.append(self.Particle(
                color = (random_int1,random_int2,random_int3),
                mass = int(new_input[0]),
                position = (int(new_input[1]), int(new_input[2])),
                velocity = (int(new_input[3]), int(new_input[4])),
            ))
            del new_input[0:7]

        return particle_list

    def __init__(self):
        self.set_up()
        testWorld = self.PhysicsWorld()
        testWorld.gravity = -0.98
        pygame.display.set_caption('Physics Sim')
        self.screen.fill(self.background_colour)
        pygame.display.flip()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  running = False

            self.Particle.move(self, testWorld)
            self.refresh_img()

        pygame.quit()

Scene()
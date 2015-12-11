import PhysicsKit
import pygame
import time
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
        self.particle_list = self.get_particle_list()

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
        time.sleep(0.02)

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

    def __init__(self):
        self.set_up()
        pygame.display.set_caption('Physics Sim')
        self.screen.fill(self.background_colour)
        pygame.display.flip()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  running = False

            self.Particle.move(self)
            self.refresh_img()

        pygame.quit()

Scene()
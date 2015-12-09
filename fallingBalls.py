import PhysicsKit
from pygame.locals import *
from read_input import read_input
import pygame, time, sys, math, random


def refresh_img(particle_list, background_colour):
    screen.fill(background_colour)
    for particle in particle_list:
        pygame.draw.circle(screen, particle.color, (int(particle.position[0]), height - int(particle.position[1])),
                           particle.mass * 2, 2)
        pygame.display.update()
    time.sleep(0.02)


background_colour = (255, 255, 255)
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Physics Sim')
screen.fill(background_colour)
pygame.display.flip()

PhysicsWorld = PhysicsKit.PhysicsWorld
Particle = PhysicsKit.Particle

scene = PhysicsWorld()

particle_list = list()
for i in range(0, 5):
    particle_list.append(Particle())
    particle_list[i].color = (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))
    particle_list[i].mass = random.randint(15, 20)
    particle_list[i].position = (random.randint(5, 750), random.randint(5, 750))
    particle_list[i].velocity = (random.randint(-200, 200), random.randint(-200, 200))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Particle.move(particle_list, scene.gravity, scene.interval, width, height)
    refresh_img(particle_list, background_colour)

pygame.quit()

import pygame
import PhysicsKit
import random


pygame.display.set_caption('Physics Sim')
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
background_colour = (255, 255, 255)
screen.fill(background_colour)


scene = PhysicsKit.PhysicsWorld(width, height)
scene.make_particle(5)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scene.update()
    screen.fill(scene.color)

    for particle in scene.particle_list:
        pygame.draw.circle(screen, particle.color, (int(particle.position[0]), height - int(particle.position[1])), particle.mass * 2, 2)


    pygame.display.flip()
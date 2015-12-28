import pygame
import PhysicsKit
import random

pygame.display.set_caption('Physics Sim')
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
background_color = (0, 0, 0)
thickness = 2
screen.fill(background_color)

nebula = PhysicsKit.PhysicsWorld(width, height)
nebula.make_particle(5)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    nebula.update()
    screen.fill(nebula.color)

    for particle in nebula.particle_list:
        pygame.draw.circle(
            screen,
            particle.color,
            (int(particle.position[0]), height - int(particle.position[1])),
            particle.mass * 2,
            thickness
        )

    pygame.display.flip()

from particle import Particle
from pygame.locals import *
from read_input import read_input
import pygame, time, sys, math
from PhysicsWorld import check_collision
##### Functions #####
def refresh_img(particle_list,background_colour):
  screen.fill(background_colour)
  for particle in particle_list:
    pygame.draw.circle(screen, particle.color, (int(particle.position[0]), height - int(particle.position[1])), particle.mass * 2, 2)
    pygame.display.update()
  time.sleep(0.02)


#### Set up Pygame #####
background_colour = (255, 255, 255)
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Physics Sim')
screen.fill(background_colour)
pygame.display.flip()
########################

particle_list, planetary_obj = read_input("freeFalling-2.txt")


interval = 0.2
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


  for i, particle in enumerate(particle_list):
    particle.set_position(interval, planetary_obj)
    particle.check_bounds(width, height, interval)
    for ii in range(i + 1, len(particle_list)):
      check_collision(particle, particle_list[ii])
  refresh_img(particle_list)

pygame.quit()


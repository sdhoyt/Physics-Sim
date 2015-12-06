from particle import Particle
from pygame.locals import *
from read_input import read_input
import pygame, time, sys, math

##### Functions #####
def refresh_img(particle_list):
  screen.fill(background_colour)
  for particle in particle_list:
    pygame.draw.circle(screen, particle.color, (int(particle.position[0]), height - int(particle.position[1])), particle.mass * 5, 5)
    pygame.display.update()
  time.sleep(0.02)

def check_collision(particle, particle2):
  dx = abs(particle2.position[0] - particle.position[0])
  dy = abs(particle2.position[1] - particle.position[1])
  distance = math.hypot(dx, dy)

  if distance <= (particle.mass + particle2.mass) * 5 :
    x_vel1 = (particle.velocity[0]*(particle.mass - particle2.mass) + 2*particle2.mass*particle2.velocity[0])/(particle.mass + particle2.mass)
    y_vel1 = (particle.velocity[1]*(particle.mass - particle2.mass) + 2*particle2.mass*particle2.velocity[1])/(particle.mass + particle2.mass)
    x_vel2 = (particle2.velocity[0]*(particle2.mass - particle.mass) + 2*particle.mass*particle.velocity[0])/(particle2.mass + particle.mass)
    y_vel2 = (particle2.velocity[0]*(particle2.mass - particle.mass) + 2*particle.mass*particle.velocity[0])/(particle2.mass + particle.mass)
    particle.velocity = (x_vel1, y_vel1)
    particle2.velocity = (x_vel2, y_vel2)

#### Set up Pygame #####
background_colour = (255, 255, 255)
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
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


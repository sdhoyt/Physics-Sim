from particle import Particle
from pygame.locals import *
from read_input import read_input
import pygame, time, sys

##### Functions #####
def refresh_img(particle_list):
  screen.fill(background_colour)
  for particle in particle_list:
    pygame.draw.circle(screen, (0, 0, 0), (int(particle.position[0]), height - int(particle.position[1])), 3, 0)
    pygame.display.update()
  time.sleep(0.1)

#def check_collision(particle_list):
#  position_list = list()
#  duplicates_list = list()
#  index_list = list()
#  velocity_list = list()
#  duplicates = 0
#  for particle in particle_list:
#    position_list.append(particle.position)
#  for i in range(0,len(position_list) - 1):
#    for j in range(0,len(position_list) - 1):
#      if position_list[i] == position_list[j]:
#        duplicates += 1
#      duplicates_list.append(duplicates)
#  for index in range(0, len(duplicates_list) - 1):
#    if duplicates_list[index] > 1:
#      index_list.append(index)
#  for particle in range(0, len(particle_list) - 1):
#    for index in index_list:
#      if particle == index:
#        velocity_list.append(particle_list[index].velocity)
#  for particle in range(0, len(particle_list) - 1):
#    x_vel = -particle_list[particle].velocity[0]
#    y_vel = -particle_list[particle].velocity[1]
#    particle_list[particle].velocity = (x_vel, y_vel)
#    for velocity in velocity_list:
#      if particle_list[particle].velocity != velocity:
#        x_vel = velocity[0] + particle_list[particle].velocity[0]
#        y_vel = velocity[1] + particle_list[particle].velocity[1]








#### Set up Pygame #####
background_colour = (255, 255, 255)
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()
########################

particle_list, planetary_obj = read_input("freeFalling-2.txt")


interval = 0.4
timer = 0
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  for particle in particle_list:
    particle.set_position(interval, planetary_obj)
    particle.check_bounds(width, height, interval)
  #check_collision(particle_list)
  refresh_img(particle_list)

pygame.quit()


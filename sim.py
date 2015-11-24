from particle import Particle
from read_input import read_input
import pygame, time

##### Functions #####
def refresh_img(particle_list):
  for particle in particle_list:
    screen.fill(background_colour)
    pygame.draw.circle(screen, (0, 0, 0), (int(particle.position[0]), height - int(particle.position[1])), 5, 5)
    pygame.display.update()
  time.sleep(0.1)

#####################

#### Set up Pygame #####
background_colour = (255, 255, 255)
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()
########################

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    ##########################
    ########## Start #########
    ##########################

  particle_list = read_input("freeFalling-2.txt")

  interval = 0.05
  timer = 0
  while timer < 300:
    for particle in particle_list:
      particle.set_position(interval)
      particle.check_bounds(width, height, interval)
    if timer < 300:
      refresh_img(particle_list)
      timer += 1
    else:
      break

    ##########################
    ########## End ###########
    ##########################
  break



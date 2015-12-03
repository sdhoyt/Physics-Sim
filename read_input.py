from particle import Particle
from particle import Planet
from particle import Earth
planets = {1: 'Earth', 2: 'Moon', 3: 'Mars'}
def read_input(input_file):
    particle_list = list()
    inputFile = open(input_file)
    input = inputFile.readlines()
    new_input = list()
    for index in range(0, len(input)):
        if input[index][0] != '#':
            new_input.append(input[index])
    number_of_particles = int(new_input[0])
    gravity = int(new_input[1])

    if gravity == 1:
        planetary_obj = Earth()

    del new_input[0]
    del new_input[1]
    for index in range(0, number_of_particles):
        particle_list.append(Particle(mass = int(new_input[0]),position = (int(new_input[1]), int(new_input[2])),velocity = (int(new_input[3]), int(new_input[4])),acceleration = (int(new_input[5]), int(new_input[6]))))
        del new_input[0:7]

    return particle_list, planetary_obj


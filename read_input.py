from particle import Particle

def read_input(input_file):
    particle_list = list()
    inputFile = open(input_file)
    input = inputFile.readlines()
    new_input = list()
    for index in range(0, len(input)):
        if input[index][0] != '#':
            new_input.append(input[index])

    for index in range(0, int(new_input[0])):
        particle_list.append(Particle())

    del new_input[0]
    for index in range(1, len(particle_list) + 1):
        particle_list[index - 1].mass = int(new_input[0])
        particle_list[index - 1].initial_position = (int(new_input[1]), int(new_input[2]))
        particle_list[index - 1].initial_velocity = (int(new_input[3]), int(new_input[4]))
        particle_list[index - 1].initial_acceleration = (int(new_input[5]), int(new_input[6]))
        del new_input[0:7]

    return particle_list


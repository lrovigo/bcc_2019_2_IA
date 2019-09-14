import matplotlib.pyplot as plt
from random import randint
import json
import logging

from typing import List

CLEAN = 'ASPIRAR'
RIGHT = 'DIREITA'
LEFT = 'ESQUERDA'
DOWN = 'BAIXO'
UP = 'CIMA'
NOOP = 'NOOP'

def build_matrix(high, length):
    logging.debug('building matrix')
    matrix = list()
    for i in range(high):
        matrix.append(list())
        for j in range(length):
            wall = i == 0 or i == high -1 or j == 0 or j == length -1
            matrix[i].append(1 if wall else 0)
    logging.debug('matrix: %s' % (str(matrix),))

    return matrix

def make_dirty(matrix):
    logging.debug('making dirt')
    global world_size
    high, length = world_size
    dirt_number = randint(2, 5)
    logging.debug('dirt_number: %s' %(str(dirt_number),))
    dirt_set = set()
    while len(dirt_set) < dirt_number:
        dirt_set.add((randint(0, high-3)+1, randint(0, length-3)+1))
    logging.debug('dirt_set: %s' %(str(dirt_set)))
    for x, y in dirt_set:
        matrix[x][y] = 2
    logging.debug('matrix: %s' % (str(matrix),))
    return (matrix, dirt_number)


def load_matrix(file_path):
    logging.debug('opening file: %s' % (str(file_path)))
    with open(file_path) as file_buf:
        input_dict = json.load(file_buf)
        logging.debug('input_dict: %s' % (str(input_dict)))
        if 'length' in input_dict:
            length = input_dict['length']
            logging.debug('length: %s' % (str(length)))
            if 'high' in input_dict:
                high = input_dict['high']
            else:
                logging.debug('No high, using length')
                high = length
            logging.debug('high: %s' % (str(high)))
            matrix = build_matrix(high, length)
        else:
            raise Exception('Invalid input file')

    global world_size
    world_size = (high, length)

    matrix, dirt_number = make_dirty(matrix)

    return (matrix, world_size, dirt_number)
    
def show(matrix, position):
    plt.imshow(matrix, 'gray')
    plt.show(block=False)
    plt.plot(position[1], position[0], '*r', 'LineWidth', 5)
    plt.pause(0.2)
    plt.clf()

def move(direction, position):

    logging.debug('moveging %s' % (str(direction)))
    logging.debug('position: %s' % (str(position)))

    if direction == RIGHT:
        position[1] += 1
    elif direction == LEFT:
        position[1] -= 1
    elif direction == UP:
        position[0] -= 1
    elif direction == DOWN:
        position[0] += 1
    logging.debug('position: %s' % (str(position)))
    return position


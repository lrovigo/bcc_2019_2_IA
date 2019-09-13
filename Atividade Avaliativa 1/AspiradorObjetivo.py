import matplotlib.pyplot as plt
from random import randint
import json
import logging

CLEAN = 'ASPIRAR'
RIGHT = 'DIREITA'
LEFT = 'ESQUERDA'
DOWN = 'BAIXO'
UP = 'CIMA'
NOOP = 'NOOP'
dirt_number = 0
position = [1,1]
state = [
        RIGHT,  # dirrection it's corrently moveing
        DOWN,   # vertical next direction
        RIGHT,  # horizontal next direction
        ]

def load_matrix(file_path):
    with open(file_path) as file_buf:
        matrix = json.load(file_buf)['base_map']
    global dirt_number
    dirt_number = randint(1, 16)
    dirt_set = set()
    while len(dirt_set) < dirt_number:
        dirt_set.add((randint(0, 3)+1, randint(0, 3)+1))

    for x, y in dirt_set:
        matrix[x][y] = 2

    return matrix
    
def main():
    matrix = load_matrix('map.json')
    points = 0
    global position
    global dirt_number
    
    while True:
        show(matrix)

        posX, posY = position

        currState = matrix[posX][posY]
        logging.debug('matrix: %s' % (str(matrix)))
        logging.debug('posX: %s' % (str(posX)))
        logging.debug('posY: %s' % (str(posY)))
        logging.debug('currState: %s' % (str(currState)))
        action = agenteReativoSimples(currState,CheckRoom())

        print('Acao escolhida: %s' % (action))
        logging.info('Acao escolhida: %s' % (action))
        
        if(action == NOOP):
            print('Points: %s' % (points))
            break
        if action == CLEAN:
            matrix[posX][posY] = 0
            dirt_number -= 1
        else:
            move(action)
        points += 1

def show(matrix):
    global position
    plt.imshow(matrix, 'gray')
    plt.show(block=False)
    plt.plot(position[1], position[0], '*r', 'LineWidth', 5)
    plt.pause(0.2)
    plt.clf()

def CheckRoom():
    global dirt_number
    if(dirt_number <= 0):
        return NOOP
    
def move(direction):
    global position

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

def agenteReativoSimples(percepcao, roomState):
    logging.debug('percepcao: %s' % (str(percepcao)))
    if roomState == NOOP:
        return NOOP
    if percepcao == 2:
        return CLEAN

    # Load the agent state and position
    global state
    global position

    direction, directionV, directionH = state
    posX, posY = position

    logging.debug('direction: %s' % (str(direction)))
    logging.debug('directionV: %s' % (str(directionV)))
    logging.debug('directionH: %s' % (str(directionH)))
    logging.debug('posX: %s' % (str(posX)))
    logging.debug('posY: %s' % (str(posY)))

    moveingLeftWall = (direction == LEFT and posY == 1)
    movingRightWall = (direction == RIGHT and posY == 4)
    moveingVertival = (direction in (UP, DOWN))
    isTop = (posX == 1)
    isBotton = (posX == 4)

    logging.debug('moveingLeftWall: %s' % (str(moveingLeftWall)))
    logging.debug('movingRightWall: %s' % (str(movingRightWall)))
    logging.debug('moveingVertival: %s' % (str(moveingVertival)))
    logging.debug('isTop: %s' % (str(isTop)))
    logging.debug('isBotton: %s' % (str(isBotton)))

    if moveingLeftWall: 
        direction = directionV
        directionH = RIGHT
    elif movingRightWall: # TODO: change to not be static
        direction = directionV
        directionH = LEFT
    elif moveingVertival:
        if isTop:
            directionV = DOWN
        elif isBotton:
            directionV = UP

        direction = directionH

    # Overite the state of the agent
    state = [direction, directionV, directionH]
    return direction
            
if __name__ == "__main__":
    logging.basicConfig(level = logging.DEBUG)
    main()

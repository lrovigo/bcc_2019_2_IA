from common import *
import logging

state = [
        RIGHT,  # direction it's currently moving
        DOWN,   # vertical next direction
        RIGHT,  # horizontal next direction
        ]
world_size = (0, 0)

def main():
    global world_size
    # inicializa o mundo e seus atributos
    matrix, world_size, dirt_number = load_matrix('generic.json')

    position = [1,1]
    
    while True:
        # atualiza apresentação
        show(matrix, position)

        posX, posY = position

        currState = matrix[posX][posY]
        perception = (currState, position)

        logging.debug('matrix: %s' % (str(matrix)))
        logging.debug('posX: %s' % (str(posX)))
        logging.debug('posY: %s' % (str(posY)))
        logging.debug('currState: %s' % (str(currState)))

        # Obtém ação com o agente
        action = agenteReativoSimples(perception)

        print('Acao escolhida: %s' % (action))
        logging.info('Acao escolhida: %s' % (action))

        # executa ação
        if action == CLEAN:
            matrix[posX][posY] = 0
        else:
            position = move(action, position)

def agenteReativoSimples(percepcao):

    logging.debug('percepcao: %s' % (str(percepcao)))

    slot_state, position = percepcao
    
    if slot_state == 2:
        return CLEAN

    # Load the agent state and position
    global state
    global world_size

    direction, directionV, directionH = state
    posX, posY = position

    high, length = world_size

    logging.debug('direction: %s' % (str(direction)))
    logging.debug('directionV: %s' % (str(directionV)))
    logging.debug('directionH: %s' % (str(directionH)))
    logging.debug('posX: %s' % (str(posX)))
    logging.debug('posY: %s' % (str(posY)))

    moveingLeftWall = (direction == LEFT and posY == 1)
    movingRightWall = (direction == RIGHT and posY == length-2)
    moveingVertival = (direction in (UP, DOWN))
    isTop = (posX == 1)
    isBotton = (posX == high-2)

    logging.debug('moveingLeftWall: %s' % (str(moveingLeftWall)))
    logging.debug('movingRightWall: %s' % (str(movingRightWall)))
    logging.debug('moveingVertival: %s' % (str(moveingVertival)))
    logging.debug('isTop: %s' % (str(isTop)))
    logging.debug('isBotton: %s' % (str(isBotton)))

    # se estiver indo em direção à uma parede, inverte a direção pretedida para essa orientação.
    # i.e.: se o movimento horizontal é a esquerda e está chegando a uma parede à esquerda, muda para o movimento horizontal ser à direita.
    #
    # Se estiver chegando a uma parede lareral, muda a direção efetiva para baixo.
    # Se estivesse se movendo verticalmente, altera para horizontal
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

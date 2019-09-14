from common import *
import logging
import itertools

state = [
        RIGHT,  # direction it's currently moving
        DOWN,   # vertical next direction
        RIGHT,  # horizontal next direction
        ]
world_size = (0, 0)
plan = []

def all_combinations_recursiv(pending, items, combinations):
    if not pending:
        combinations.append(items)
        return 
    for i in range(len(pending)):
        new_pending = pending[:i] + pending[i+1:]
        all_combinations_recursiv(new_pending, items + [pending[i]], combinations)

def all_combinations(pending):
    combinations = list()
    all_combinations_recursiv(pending, list(), combinations)
    return combinations

def calc_distance(positions):
    distance = 0
    for orig, dest in zip(positions[:-1], positions[1:]):
        orig_x, orig_y = orig
        dest_x, dest_y = dest
        distance += abs(orig_x - dest_x)
        distance += abs(orig_y - dest_y)

    return distance

def make_plan(rout):
    plan = list()
    for orig, dest in zip(rout[:-1], rout[1:]):
        vert_move = DOWN if orig[0] < dest[0] else UP
        hori_move = RIGHT if orig[1] < dest[1] else LEFT
        plan += abs(orig[0] - dest[0])*[vert_move]
        plan += abs(orig[1] - dest[1])*[hori_move]
    return plan


def build_clean_plan(start_position, matrix):

    position_set = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                position_set.add((i,j,))
    
    all_possible_routes = [[start_position] + rout for rout in all_combinations(list(position_set))]

    minimun = (-1, -1)
    for ind, rout in enumerate(all_possible_routes):
        distance = calc_distance(rout)
        if distance < minimun[1] or minimun[1] == -1:
            minimun = (ind, distance)

    rout = all_possible_routes[minimun[0]]
    logging.debug('rout: %s' % (str(rout)))
    plan = make_plan(rout)

    return plan

def main():
    global world_size
    matrix, world_size, dirt_number = load_matrix('generic.json')

    points = 0

    position = [1,1]

    global plan
    plan = build_clean_plan(position, matrix)
    logging.debug('plan: %s' % (str(plan)))
    
    while True:
        show(matrix, position)

        posX, posY = position

        currState = matrix[posX][posY]
        perception = (currState, position)

        logging.debug('matrix: %s' % (str(matrix)))
        logging.debug('posX: %s' % (str(posX)))
        logging.debug('posY: %s' % (str(posY)))
        logging.debug('currState: %s' % (str(currState)))

        action = agenteReativoSimples(perception, matrix)

        if(action == NOOP):
            print('Points: %s' % (points))
            input()
            break

        print('Acao escolhida: %s' % (action))
        logging.info('Acao escolhida: %s' % (action))

        if action == CLEAN:
            matrix[posX][posY] = 0
            dirt_number -= 1
        else:
            position = move(action, position)
        points += 1


def agenteReativoSimples(percepcao, roomState):
    logging.debug('percepcao: %s' % (str(percepcao)))
    logging.debug('roomState: %s' % (str(roomState)))

    slot_state, position = percepcao

    if max(itertools.chain.from_iterable(roomState)) < 2:
        return NOOP

    if slot_state == 2:
        return CLEAN

    global plan
    if not plan:
        raise Exception('Fairule! incomplete plan')
    return plan.pop(0)
            
if __name__ == "__main__":
    logging.basicConfig(level = logging.DEBUG)
    # print(build_clean_plan((0,0), [[0,0,2], [0,0,2], [0, 0, 0]]))
    main()

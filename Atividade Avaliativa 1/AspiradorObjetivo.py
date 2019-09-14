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
    """Identifica todas as combinações possíveis para uma lista de valores
    
    Isso é realizado recursivametne verificando todos os itens não verificados.
    Parâmetros:
        -> pending = itens a serem organizados
        -> items = itens já organizados
        -> combinations = organizações já identificadas
    
    Se não há itens itens a serem organizados, os itens já organizados são iseridos como uma nova ordem no parâmetro combinations
    Se há, para cada um dele, será feita uma chamada recursiva removendo esse item de pending e inserindo no final de itens.
    
    Uma chamada all_combinations_recursiv([1, 2, 3], [], []) geraria as chamadas recursivas:
        -> all_combinations_recursiv([2, 3], [1], []):
            -> all_combinations_recursiv([3], [1, 2], []):
                -> all_combinations_recursiv([], [1, 2, 3], []):
            -> all_combinations_recursiv([2], [1, 3], []):
                -> all_combinations_recursiv([], [1, 3, 2], []):
                -> all_combinations_recursiv([], [1, 3, 2], []):

                ...
        
        """
    if not pending:
        combinations.append(items)
        return 
    for i in range(len(pending)):
        new_pending = pending[:i] + pending[i+1:]
        all_combinations_recursiv(new_pending, items + [pending[i]], combinations)

def all_combinations(pending):
    """Gera todas as ordens possíveis de uma lista e retorna, ver all_combinations_recursiv"""
    combinations = list()
    all_combinations_recursiv(pending, list(), combinations)
    return combinations

def calc_distance(positions):
    """Para uma lista de tuplas, calcula a distance da primeira para a segunda, da segunda para a terceira...
    
    Para isso, passa por cada par n, n+1, e soma o valor absoluta das diferenças do primeiro e do segundo valor"""
    distance = 0
    for orig, dest in zip(positions[:-1], positions[1:]):
        orig_x, orig_y = orig
        dest_x, dest_y = dest
        distance += abs(orig_x - dest_x)
        distance += abs(orig_y - dest_y)

    return distance

def make_plan(rout):
    """Transforma uma sequencia de tuplas (rota) em uma sequencia de passos (plano).

    Para cada par n e n+1, calcula a direção vertical e horizontal, e adiciona a quantidade de vezes da diferença absoluta.
    """
    plan = list()
    for orig, dest in zip(rout[:-1], rout[1:]):
        vert_move = DOWN if orig[0] < dest[0] else UP
        hori_move = RIGHT if orig[1] < dest[1] else LEFT
        plan += abs(orig[0] - dest[0])*[vert_move]
        plan += abs(orig[1] - dest[1])*[hori_move]
    return plan


def build_clean_plan(start_position, matrix):
    """Partindo de uma posição inicial e uma grade onde serão identificadas as
    posições de sugeiras, identifica os passos para passar por todas no menor
    trajeto possível """

    position_set = set()

    for i in range(len(matrix)):  # Identifica todos os pontos sujos
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                position_set.add((i,j,))
    
    # identifica todas as possiveis rotas (e.g.: [[(1, 1), (2, 3), (4, 4)], [(1, 1), (4, 4), (2, 3)]]
    all_possible_routes = [[start_position] + rout for rout in all_combinations(list(position_set))]

    minimun = (-1, -1)
    for ind, rout in enumerate(all_possible_routes): # identifica a rota com o menor soma de distancias
        distance = calc_distance(rout)
        if distance < minimun[1] or minimun[1] == -1:
            minimun = (ind, distance)

    rout = all_possible_routes[minimun[0]]
    logging.debug('rout: %s' % (str(rout)))
    plan = make_plan(rout) # transforma a rota em um plano (passos) e retorna.

    return plan

def main():
    global world_size
    # Controi um mapa (matrix)
    matrix, world_size, dirt_number = load_matrix('generic.json') 

    # inicializa um contador de pontos
    points = 0

    # inicializa a posição de partida
    position = [1,1]

    # define um plano
    global plan
    plan = build_clean_plan(position, matrix)
    logging.debug('plan: %s' % (str(plan)))
    
    while True:
        # Atualiza tela
        show(matrix, position)

        # Identifica informações sobre o ambiente (posição atual, estado do slot)
        posX, posY = position
        currState = matrix[posX][posY]
        perception = (currState, position)

        logging.debug('matrix: %s' % (str(matrix)))
        logging.debug('posX: %s' % (str(posX)))
        logging.debug('posY: %s' % (str(posY)))
        logging.debug('currState: %s' % (str(currState)))

        # consulta agente para identificar ação
        action = agenteReativoSimples(perception, matrix)

        # se o agente diz que não há mais ações, para o processo
        if(action == NOOP):
            print('Points: %s' % (points))
            input()
            break

        print('Acao escolhida: %s' % (action))
        logging.info('Acao escolhida: %s' % (action))

        # Se a ação é limpar o slot corrente, limpa
        if action == CLEAN:
            matrix[posX][posY] = 0
            dirt_number -= 1
        else:
            position = move(action, position) # se não se move
        points += 1


def agenteReativoSimples(percepcao, roomState):
    logging.debug('percepcao: %s' % (str(percepcao)))
    logging.debug('roomState: %s' % (str(roomState)))

    slot_state, position = percepcao

    # Se não há mais slots sujos, para
    if max(itertools.chain.from_iterable(roomState)) < 2:
        return NOOP

    # Se o slot atual está sujo, limpa
    if slot_state == 2:
        return CLEAN

    # Se não, segue com plano
    global plan
    if not plan:
        raise Exception('Fairule! incomplete plan')
    return plan.pop(0)
            
if __name__ == "__main__":
    logging.basicConfig(level = logging.DEBUG)
    main()

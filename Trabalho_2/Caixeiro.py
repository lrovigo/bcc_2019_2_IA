"""
The population is going to be kept by a
"""

import random
import math
import typing
import matplotlib.pyplot as plt

City = typing.Tuple[float]
Chromosome = typing.List[City]
Population = typing.List[Chromosome]


def fitness(position_list: typing.List[typing.Tuple[int]]) -> int:
    """Generates a fitness value to a list of tuples.
    The distance in each step is calculated by euclidean.
    The bigger the worst.
    """
    distance = 0
    for ind in range(len(position_list)):
        a = position_list[ind]
        b = position_list[ind-1]
        x_delta = a[0] - b[0]
        y_delta = a[1] - b[1]
        distance += math.sqrt(x_delta ** 2 + y_delta ** 2)
    return distance


def generate_map(length:int = 20) -> Chromosome:
    """
    TODO: doc
    """
    city_list = list()
    for i in range(length):
        city_list.append((random.random(), random.random()))
    return city_list


def generate_population(city_list: Chromosome, length = 20) -> Population:
    """
    TODO: doc
    """
    matrix = list()
    for i in range(length):
        base = [x for x in city_list]
        random.shuffle(base)
        matrix.append(base)

    return matrix


def generate_probability(pop: Population) -> Population:
    """
    TODO: doc
    """
    len_pop = len(pop)
    len_prob = math.factorial(len_pop)
    prob = list()

    for i in range(len_pop):
        prob_i = len_pop - i
        for j in range(prob_i):
            prob.append(pop[i])

    return prob


def select_fathers(prob: Population, length: int = 5) -> Population:
    """
    TODO: doc
    """
    father_list = list()
    for i in range(length):
        father_list.append(random.choice(prob))

    return father_list


def crossover(father_pair: typing.Tuple[Chromosome]) -> typing.Tuple[Chromosome]:
    """
    TODO: doc
    """
    son_0 = [x for x in father_pair[0]]
    son_1 = [x for x in father_pair[1]]
    cut_point = random.randint(0, len(son_0)-1)
    cut_point_list = list()
    while True:
        temp = son_0[cut_point]
        son_0[cut_point] = son_1[cut_point]
        son_1[cut_point] = temp


        if len(set(son_0)) == len(son_0) and len(set(son_1)) == len(son_1):
            return (son_0, son_1)

        cut_point_list.append(cut_point)
        cut_point = 0
        for i in range(len(son_0)):
            for j in range(i+1, len(son_0)):
                if son_0[i] == son_0[j]: # or son_1[i] == son_1[j]:
                    if i not in cut_point_list:
                        cut_point = i
                        break
                    if j not in cut_point_list:
                        cut_point = j
                        break
            if cut_point:
                break


def mutate(ch: Chromosome) -> None:
    """
    TODO: doc
    """
    i = random.randint(0, len(ch)-1)
    j = random.randint(0, len(ch)-1)
    while i == j:
        j = random.randint(0, len(ch)-1)

    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp


def main():
    """
    TODO: doc
    """

    plots = list()

    city_list = generate_map()
    population = generate_population(city_list, 64)
    population.sort(key = fitness)

    top = 0
    top_gen = 0
    for i in range(1000):
        population.sort(key = fitness)

        if top != fitness(population[0]):
            top = fitness(population[0])
            top_gen = i
            plots.append(prepare(population[0]))
            print(i, len(plots), fitness(population[0]), fitness(population[-1]))

        population = population[0:int(len(population)/2)]
        probability = generate_probability(population)

        father_list_0 = select_fathers(probability, int(len(population)/2))
        father_list_1 = select_fathers(probability, int(len(population)/2))

        for father_pair in zip(father_list_0, father_list_1):
            son_0, son_1 = crossover(father_pair)

            if random.random() <= 0.05:
                mutate(son_0)
            if random.random() <= 0.05:
                mutate(son_1)
            population.append(son_0)
            population.append(son_1)
    
    population.sort(key = fitness)
    plots.append(prepare(population[0]))
    show(plots)


def prepare(chro):
    """
    TODO: doc
    """

    best_path_x = []
    best_path_y = []
    for city in chro:
        best_path_x.append(city[0])
        best_path_y.append(city[1])

    first_city = chro[0]
    best_path_x.append(first_city[0])
    best_path_y.append(first_city[1])

    return (best_path_x, best_path_y)

def show(plots):
    """
    TODO: doc
    """
    for p in plots:
        plt.plot(*p, "go-")
        if p == plots[-1]:
            plt.show()
            break
        plt.show(block=False)
        plt.pause(10/len(plots))
        plt.clf()


if __name__ == '__main__':
    main()

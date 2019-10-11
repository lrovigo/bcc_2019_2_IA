import math

def fitness(position_list):
    distance = 0
    for ind in range(len(position_list)):
        a = position_list[ind]
        b = position_list[ind-1]
        x_delta = a[0] - b[0]
        y_delta = a[1] - b[1]
        distance += math.sqrt(x_delta ** 2 + y_delta ** 2)
    return distance

print(fitness([(0, 0), (0, 200)]))
input()

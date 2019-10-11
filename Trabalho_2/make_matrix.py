import random

def new_matrix():
    matrix = list()
    for i in range(20):
        matrix.append(list())
        for j in range(20):
            v = random.randint(1, 20)
            matrix[i].append(v)
    print(matrix)
    input()
    return matrix
            
new_matrix()

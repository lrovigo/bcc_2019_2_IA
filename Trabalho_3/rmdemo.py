import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

from scipy.io import loadmat
import numpy as np


def get_data(file_path):
    """
    Obtain the data from a ``.mat`` file that describes a list of 3-tuple.
    """

    data_dict = loadmat(file_path)
    data = data_dict.get('data')

    return data


def main():
    data = get_data('Dados/data.mat')

    x = np.array(tuple(tuple((1, house[0], house[1])) for house in data))
    y = np.array(tuple((house[2],) for house in data))

    beta = calculate_betas(x, y)
    # plot_points(data)
    plot_line(beta, data)

    plt.show()


def plot_points(data):
    fig = plt.figure()
    ax = Axes3D(fig)
    scatter_data = zip(*tuple(map(tuple, data)))
    ax.scatter(*scatter_data, c='r', marker='^')


def plot_line(beta, data):
    
    size_list = tuple(house[0] for house in data)
    qt_room_list = tuple(house[1] for house in data)

    max_size = max(size_list)
    min_size = min(size_list)
    max_qt_room = max(qt_room_list)
    min_qt_room = min(qt_room_list)

    x = np.arange(min_size, max_size, 100)
    y = np.arange(min_qt_room, max_qt_room+1, 1)
    x, y = np.meshgrid(x, y)
    z = beta[0] + x * beta[1] + y * beta[2]

    fig = plt.figure()
    ax = Axes3D(fig)

    scatter_data = zip(*tuple(map(tuple, data)))
    ax.scatter(*scatter_data, c='r', marker='^', label='treinamento')
    ax.legend()

    ax.plot_surface(x, y, z, cmap='viridis', label='expectativa de preço')

    ax.set_xlabel('tamanho')
    ax.set_ylabel('quantidade de quartos')
    ax.set_zlabel('preço')



def calculate_betas(x, y):
    tra_x = np.transpose(x)
    inv_x = np.linalg.pinv(tra_x.dot(x))

    betas = inv_x.dot(tra_x.dot(y))

    return tuple(float(x) for x in betas)

def plot():
    data = get_data('Dados/data.mat')


if __name__ == '__main__':
    main()


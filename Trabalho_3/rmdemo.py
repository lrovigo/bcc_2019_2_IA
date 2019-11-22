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

    print(beta)

def calculate_betas(x, y):
    tra_x = np.transpose(x)
    inv_x = np.linalg.pinv(tra_x.dot(x))

    betas = inv_x.dot(tra_x.dot(y))

    return tuple(float(x) for x in betas)

if __name__ == '__main__':
    main()

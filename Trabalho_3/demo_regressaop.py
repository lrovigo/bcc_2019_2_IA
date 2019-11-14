from Regressao import correlacao, regressao
from scipy.io import loadmat
import numpy
from plotter import *
import random
from common import *


def eqm(testing, betas):
    """
    Calculates the quadratic average error

    ``eqm(testing, betas)``

    ``testing`` -> the testing populatios
        e.g.: ``[(0,0), (5, 5)]``

    ``betas`` -> a list of values describing each power values.

    i.e.:
        ``y = m1 * x^n1 + m2 * x^n2``
        ``[m1, m2]``

    e.g.:
        ``y = x^0 + 5x^1``
        ``[1, 5]``

    """
    value = 0.0
    for base, real in testing:
        expected = apply_poly(base, betas)
        diff = abs(real-expected)
        value += diff ** 2
    value /= len(testing)
    return value


def get_data(file_path):
    """
    Obtain the data from a ``.mat`` file that describes a list of ordered
    pairs.

    Returns the data separated 10% for test and 90% for training in a tuple.
    Returns also the biggest x value.
    i.e.: ``tuple(training, testing, max_x)``
    
    """


    data_dict = loadmat(file_path)
    data = data_dict.get('data')
    data = tuple(tuple(sub_d for sub_d in d) for d in data)

    max_x = max(map(float, tuple(d[0] for d in data)))

    length = len(data)

    testing_len = int(length * 0.1)
    testing = tuple(random.sample(tuple(d for d in data), testing_len))
    training = tuple(set(d for d in data)-set(testing))

    return (training, testing, max_x)

def main():
    # TODO: doc

    # Loads data, training set, testing set and how large the graphic must be.
    training, testing, graphic_lenth = get_data('Dados/data_preg.mat')

    # Plot the testing and training sets in different colors (Magenta and cyan)
    plot_dot(testing, c='m', label = 'testing')
    plot_dot(training, c='c', label = 'training')

    # Calculates the polyfit for 1, 2, 3 and 8 exponents
    zipped_training = tuple(zip(*training))
    n1 = tuple(numpy.polyfit(*zipped_training, 1))
    n2 = tuple(numpy.polyfit(*zipped_training, 2))
    n3 = tuple(numpy.polyfit(*zipped_training, 3))
    n8 = tuple(numpy.polyfit(*zipped_training, 8))

    # Calculates the error for the exponents
    eqm_n1 = eqm(testing, n1)
    eqm_n2 = eqm(testing, n2)
    eqm_n3 = eqm(testing, n3)
    eqm_n8 = eqm(testing, n8)

    # Create labels
    lbl_n1 = 'n1\neqm ' + str(round(float(eqm_n1), 5))
    lbl_n2 = 'n2\neqm ' + str(round(float(eqm_n2), 5))
    lbl_n3 = 'n3\neqm ' + str(round(float(eqm_n3), 5))
    lbl_n8 = 'n8\neqm ' + str(round(float(eqm_n8), 5))

    # Plot every curve calculated with the colors: red, green, blue and yellow
    plot_line_beta(n1, c='r', length=graphic_lenth, label=lbl_n1)
    plot_line_beta(n2, c='g', length=graphic_lenth, label=lbl_n2)
    plot_line_beta(n3, c='b', length=graphic_lenth, label=lbl_n3)
    plot_line_beta(n8, c='y', length=graphic_lenth, label=lbl_n8)

    #displays it
    show()

if __name__ == '__main__':
    main()

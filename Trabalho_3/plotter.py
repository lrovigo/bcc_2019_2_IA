import matplotlib.pyplot as plt
import numpy as np

def plot_dot(dots, c=''):
    """
    ``plot_dot(dots[, c])``
    or
    ``plot_dot(dots[, c=''])``
    
    ``dots`` -> list of coordination
        ``[(1, 1), (2, 2), (3, 3)]``

        If the dots coordinates are in two lists, ``[1, 2, 3], [1, 2, 3]``, it
        can be transformed using the ``zip`` build in function.

    ``c`` -> color that should be used to print the dots
    
        `` b ``          blue
        `` g ``          green
        `` r ``          red
        `` c ``          cyan
        `` m ``          magenta
        `` y ``          yellow
        `` k ``          black
        `` w ``          white
    """
    plt.plot(*list(zip(*dots)), c+'o')


def plot_line(dots, c=''):
    """
    ``plot_line(dots[, c])``
    or
    ``plot_line(dots[, c=''])``
    
    ``dots`` -> list of coordination
        ``[(1, 1), (2, 2), (3, 3)]``

        If the dots coordinates are in two lists, ``[1, 2, 3], [1, 2, 3]``, it
        can be transformed using the ``zip`` build in function.

    ``c`` -> color that should be used to print the line
    
        `` b ``          blue
        `` g ``          green
        `` r ``          red
        `` c ``          cyan
        `` m ``          magenta
        `` y ``          yellow
        `` k ``          black
        `` w ``          white
    """
    plt.plot(*list(zip(*dots)), c)

def plot_line_beta(beta_list, length=1, precision=3, c=''):
    """
    ``plot_line_beta(beta_list[, length=1][, precision=3][, c=''])``
    or
    ``plot_line_beta(beta_list[, length[, precision[, c]]])``
    
    ``beta_list`` -> betas that describe a polinomial function to be drawn.
        
        For the function ``y = 3x^2 + 2x + 1`` the ``beta_list`` will be
        ``[1, 2, 3]``.

    ``length`` -> for plotting a function, you can give how much the value can
    be plotted, passing one (the default value) means the function will be
    applied to values from zero to one.

    ``precision`` -> define how precise the function may be described, passing
    three means that the function will be plotted for every value between 0 and
    the ``length`` with up to ``precision`` decimal values. For the default
    values, it is going to be: ``[0, 0.001, 0.002, ..., 0.999]``

    ``c`` -> color that should be used to print the line
    
        `` b ``          blue
        `` g ``          green
        `` r ``          red
        `` c ``          cyan
        `` m ``          magenta
        `` y ``          yellow
        `` k ``          black
        `` w ``          white
    """
    precision_mod = 10 ** precision
    precision_lenth = precision_mod * length
    if precision_lenth > 100000000:
        raise Exception('too precise for that length')
    x = np.array([x/precision_mod for x in range(precision_lenth)])
    y = x * 0
    for i, beta in enumerate(beta_list):
        y += (x ** i) * beta
    plt.plot(x, y, c)

def main():
    plot_line([0, 0, 1], 100, 'r')
    plot_dot([0, 0, 1], [1, 2, 3], 'r')
    plt.show()


if __name__ == '__main__':
    main()

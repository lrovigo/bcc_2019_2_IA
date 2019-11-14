import matplotlib.pyplot as _plt
import numpy as _np
from common import *

_has_label = False

def _plot(*args, label=None, **key_args):
    """
    ``_plot(...)``

    Any positional arguments will be passed to ``matplotlib.pyplot.plot``.
    Any named arguments will be passed to ``matplotlib.pyplot.plot``.

    If there is a named argument ``label``, it will mark internal control
    variables to put the labels on show.
    """
    if bool(label):
        global _has_label
        _has_label = True
        _plt.plot(*args, label = label, **key_args)
    else:
        _plt.plot(*args, **key_args)

def plot_dot(dots, c = '', label = None):
    """
    ``plot_dot(dots [, c [, label] ] )``
    or
    ``plot_dot(dots [, c=''] [label=None] )``
    
    ``dots`` -> list of coordination
        e.g.: ``[(1, 1), (2, 2), (3, 3)]``

        If the dots coordinates are in two lists, ``[1, 2, 3], [1, 2, 3]``, it
        can be transformed using the ``zip`` build in function.

    ``c`` -> color that should be used to print the dots.

    i.e.: must be one of:
        `` b ``          blue
        `` g ``          green
        `` r ``          red
        `` c ``          cyan
        `` m ``          magenta
        `` y ``          yellow
        `` k ``          black
        `` w ``          white

    ``label`` -> label for that plot, by default is ``None``.
    """
    _plot(*list(zip(*dots)), c+'o', label = label)


def plot_line(dots, c='', label = None):
    """
    ``plot_line(dots [, c [, label] ] )``
    or
    ``plot_line(dots [, c=''] [, label=None] )``
    
    ``dots`` -> list of coordination
        e.g.: ``[(1, 1), (2, 2), (3, 3)]``

        If the dots coordinates are in two lists, ``[1, 2, 3], [1, 2, 3]``, it
        can be transformed using the ``zip`` build in function.

    i.e.: must be one of:
        `` b ``          blue
        `` g ``          green
        `` r ``          red
        `` c ``          cyan
        `` m ``          magenta
        `` y ``          yellow
        `` k ``          black
        `` w ``          white

    ``label`` -> label for that plot, by default is ``None``.
    """
    _plot(*list(zip(*dots)), c, label = label)

def plot_line_beta(beta_list, length=1, precision=3, c='', label = None):
    """
    ``plot_line_beta(beta_list [, length [, precision [, c [, label] ] ] ] )``
    or
    ``plot_line_beta(beta_list [, length=1]  [, precision=3] [, c=''] [, label] )``
    
    ``beta_list`` -> betas that describe a polinomial function to be drawn.
        
        i.e.: For the function ``y = 3x^2 + 2x + 1`` the ``beta_list`` will be
            ``[1, 2, 3]``.

    ``length`` -> for plotting a function, you can give how much the value can
    be plotted, passing one (the default value) means the function will be
    applied to values from zero to one.

    ``precision`` -> define how precise the function may be described, passing
    three means that the function will be plotted for every value between 0 and
    the ``length`` with up to ``precision`` decimal values. For the default
    values, it is going to be: ``[0, 0.001, 0.002, ..., 0.999]``.

    i.e.: must be one of:
        `` b ``          blue
        `` g ``          green
        `` r ``          red
        `` c ``          cyan
        `` m ``          magenta
        `` y ``          yellow
        `` k ``          black
        `` w ``          white

    ``label`` -> label for that plot, by default is ``None``.
    """
    precision_mod = 10 ** precision
    precision_lenth = precision_mod * length
    if precision_lenth > 100000000:
        raise Exception('too precise for that length')
    x = _np.array([x/precision_mod for x in range(int(precision_lenth))])
    y = apply_poly(x, beta_list)
    _plot(x, y, c, label = label)


def show():
    """Show plot and add label if any is available"""
    global _has_label
    if _has_label:
        _plt.legend(bbox_to_anchor=(1.05, 1), loc='best', borderaxespad=0.)
    _plt.show()


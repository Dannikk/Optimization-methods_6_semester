import numpy as np


def func(x: np.array):
    return x[0] ** 2 + x[1] ** 2


def func_rosenbrock(x: np.array):
    return (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2

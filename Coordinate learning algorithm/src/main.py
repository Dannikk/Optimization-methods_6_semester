import numpy as np
import math

INIT_PROB = 0.5


def get_probabilities(w: np.array, dim: int) -> np.array:
    p = np.zeros(dim)
    for i, w_i in enumerate(w):
        if w_i < -1:
            p[i] = 0
        elif w_i > 1:
            p[i] = 1
        else:
            p[i] = 0.5 * (1 + w_i)
    return p


def update_w(w: np.array, u1: np.array, u2: np.array, func, dim: int, beta: float, delta: float) -> np.array:
    w_new = np.empty(dim)
    for i, w_i, u1_i, u2_i in enumerate(zip(w, u1, u2)):
        w_new[i] = beta * w_i - delta * np.sign(func(u1) - func(u2) * (u1_i - u2_i))


def get_vector_epsilon(p: np.array, dim: int) -> np.array:
    epsilon = np.empty(dim)
    for i, p_i in enumerate(p):
        epsilon[i] = 2 * np.random.binomial(size=1, n=1, p=p_i) - 1
    return epsilon


def main(func, dim: int, start: float, beta: float, delta: float):
    """

    Parameters
    ----------
    delta : learning coefficient
    func :
    dim :
    start :
    beta : coefficient забывания
    """
    w = np.zeros(dim)
    while True:
        ...

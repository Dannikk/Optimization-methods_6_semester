import numpy as np
from src.func_utils import func

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
    for i, w_i, u1_i, u2_i in zip(range(dim), w, u1, u2):
        w_new[i] = beta * w_i - delta * np.sign((func(u1) - func(u2)) * (u1_i - u2_i))
    return w_new


def get_vector_xi(p: np.array, dim: int) -> np.array:
    epsilon = np.empty(dim)
    for i, p_i in enumerate(p):
        epsilon[i] = 2 * np.random.binomial(size=1, n=1, p=p_i) - 1
    return epsilon


def get_probability_vector(w: np.array, dim: int) -> np.array:
    probability_vector = np.empty(dim)
    for i, w_i in enumerate(w):
        if w_i < -1:
            probability_vector[i] = 0
        elif -1 <= w_i <= 1:
            probability_vector[i] = 0.5 * (1 + w_i)
        else:
            probability_vector[i] = 1
    return probability_vector


def main(func, dim: int, beta: float, delta: float, alpha: float):
    """
    Parameters
    ----------
    delta : learning coefficient
    func :
    dim :
    alpha :
    beta : coefficient забывания
    """

    x_1 = np.random.uniform(-1, 1, dim)

    w_1 = np.zeros(dim)
    p = get_probability_vector(w_1, dim)
    xi_vector = get_vector_xi(p, dim)

    x_2 = x_1 + alpha * xi_vector
    alpha /= 2

    for k in range(100):
        x_k = x_2 + alpha * xi_vector
        alpha /= 2
        print("x[" + str(k) + "] = " + str(x_k))
        print("xi = " + str(xi_vector))
        print("f(x) = ", func(x_k))
        w_k = update_w(w_1, x_2, x_1, func, dim, beta, delta)
        p = get_probability_vector(w_k, dim)
        xi_vector = get_vector_xi(p, dim)
        x_2, x_1 = x_k, x_2
        w_1 = w_k


main(func, 2, 1, 1, 1)

import numpy as np
from src.func_utils import func, func_rosenbrock
import random
from numpy.linalg import norm

INIT_PROB = 0.5


# def get_vector_xi(p: np.array, dim: int) -> np.array:
#     epsilon = np.empty(dim)
#     for i, p_i in enumerate(p):
#         epsilon[i] = 2 * np.random.binomial(size=1, n=1, p=p_i) - 1
#     return epsilon

# def get_probabilities(w: np.array, dim: int) -> np.array:
#     p = np.zeros(dim)
#     for i, w_i in enumerate(w):
#         if w_i < -1:
#             p[i] = 0
#         elif w_i > 1:
#             p[i] = 1
#         else:
#             p[i] = 0.5 * (1 + w_i)
#     return p


def update_w(w: np.array, u1: np.array, u2: np.array, function, dim: int, beta: float, delta: float,
             c: float) -> np.array:
    w_new = np.empty(dim)
    for i, w_i, u1_i, u2_i in zip(range(dim), w, u1, u2):
        w_new[i] = beta * w_i - delta * np.sign((function(u1) - function(u2)) * (u1_i - u2_i))
        if w_new[i] > c:
            w_new[i] = c
        elif w_new[i] < -c:
            w_new[i] = -c

    return w_new


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


def get_vector_xi(p: np.array, dim: int) -> np.array:
    xi = np.empty(dim)
    for i, p_i in enumerate(p):
        random.seed()
        xi[i] = random.choices([-1, 1], weights=[1 - p_i, p_i], k=1)[0]
    return xi


def main(function, dim: int, beta: float, delta: float, alpha: float, c: float, epsilon: float):
    """
    Parameters
    ----------
    delta : learning coefficient
    function :
    dim :
    alpha :
    c:
    beta : coefficient забывания
    """
    x_1 = np.random.uniform(0, 1, dim)
    print("x[1] = " + str(x_1))
    print("f(x) = ", func(x_1))

    w_1 = np.zeros(dim)
    p = get_probability_vector(w_1, dim)
    xi_vector = get_vector_xi(p, dim)

    x_2 = x_1 + alpha * xi_vector
    print("x[2] = " + str(x_2))
    print("xi = " + str(xi_vector))
    print("f(x) = ", func(x_2))

    k = 3
    while True:
        x_k = x_2 + alpha * xi_vector
        alpha *= 0.9
        print("x[" + str(k) + "] = " + str(x_k))
        print("xi = " + str(xi_vector))
        print("f(x) = ", func(x_k))
        w_k = update_w(w_1, x_2, x_1, function, dim, beta, delta, c)
        p = get_probability_vector(w_k, dim)
        xi_vector = get_vector_xi(p, dim)
        x_2, x_1 = x_k, x_2
        w_1 = w_k
        if norm(x_2 - x_1) < epsilon:
            break
        k += 1


main(func, 2, 2, 1, 0.9, 0.8, 0.001)

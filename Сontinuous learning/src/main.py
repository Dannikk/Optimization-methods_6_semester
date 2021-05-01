import numpy as np
from src.func_utils import func, func_rosenbrock
import random
from numpy.linalg import norm
import matplotlib.pyplot as plt

INIT_PROB = 0.5


def update_w(w: np.array, u1: np.array, u2: np.array, function, dim: int, beta: float, delta: float,
             c: float) -> np.array:
    w_new = np.empty(dim)
    flag = False
    for i, w_i, u1_i, u2_i in zip(range(dim), w, u1, u2):
        w_new[i] = beta * w_i - delta * np.sign((function(u1) - function(u2)) * (u1_i - u2_i))
        if w_new[i] > c or w_new[i] < -c:
            flag = True
    w_new = w_new / norm(w_new)

    return w_new


def get_vector_xi(w: np.array, dim: int) -> np.array:
    eta = np.random.uniform(-1, 1, dim)
    print("eta = ", eta)
    xi = (eta + w) / norm(eta + w)
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

    fig = plt.figure(figsize=(12, 7))
    plt.grid()
    x__ = []
    y__ = []

    # x_prev = np.random.uniform(-1, 1, dim)
    x_prev = np.array([0.1, 0.1])
    print("x[0] = " + str(x_prev))
    x__.append(x_prev[0])
    y__.append(x_prev[1])

    w_1 = np.zeros(dim)
    print("w_0 = ", w_1)
    x_k = x_prev + alpha * get_vector_xi(w_1, dim)
    print("x[1] = " + str(x_k))
    x__.append(x_k[0])
    y__.append(x_k[1])

    k = 2
    while True:
        w_k = update_w(w_1, x_k, x_prev, function, dim, beta, delta, c)
        print("w_k = ", w_k)
        xi_vector = get_vector_xi(w_k, dim)
        print("xi = " + str(xi_vector))
        x_prev = x_k
        x_k = x_prev + alpha * xi_vector

        print("x[" + str(k) + "] = " + str(x_k))
        print("______________________________")

        x__.append(x_k[0])
        y__.append(x_k[1])
        w_1 = w_k
        if func(x_k) < func(x_prev):
            alpha *= 1.1
        else:
            alpha *= 0.65

        # if norm(x_k - x_prev) < epsilon:
        if k > 15:
            ll = [str(i) for i in range(0, k)]
            plt.plot(np.array(x__), np.array(y__), "-o")
            ii = 0
            for x, y in zip(x__, y__):
                plt.text(x, y, str(ii), color='r')
                ii += 1
            plt.show()
            break
        k += 1


main(func, dim=2, beta=1.5, delta=1.8, alpha=0.2, c=10, epsilon=0.1)

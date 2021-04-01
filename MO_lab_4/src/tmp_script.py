import numpy as np
import numpy.linalg as ln
import scipy as sp
import scipy.optimize
import math as m


def f(x_: np.array, a: float = 4, b: float = 3, c: float = 3) -> float:
    return a * x_[0] ** 2 + x_[1] ** 2 + m.cos(b * x_[0] + c * x_[1]) - x_[0] + 2 * x_[1]


def f1(x_: np.array, a: float = 4, b: float = 3, c: float = 3) -> np.array:
    return np.array(
        [2 * a * x_[0] - b * m.sin(b * x_[0] + c * x_[1]) - 1, 2 * x_[1] - c * m.sin(b * x_[0] + c * x_[1]) + 2])


def bfgs_method(f, fprime, x0, maxiter=None, epsi=10e-3):
    """
    Minimize a function func using the BFGS algorithm.

    Parameters
    ----------
    func : f(x)
        Function to minimise.
    x0 : ndarray
        Initial guess.
    fprime : fprime(x)
        The gradient of `func`.
    """

    if maxiter is None:
        maxiter = len(x0) * 200

    # initial values
    k = 0
    gfk = fprime(x0)
    N = len(x0)
    # Set the Identity matrix I.
    I = np.eye(N, dtype=int)
    Hk = I
    xk = x0

    __count = 0

    while ln.norm(gfk) > epsi and k < maxiter:
        # pk - direction of search

        print(f'Шаг: {k}')

        print("Текущая точка:\n", xk)

        pk = -np.dot(Hk, gfk)
        print("обратная матрица Гессе:\n", Hk)
        print("градиент: ", gfk)

        # Line search constants for the Wolfe conditions.
        # Repeating the line search

        # line_search returns not only alpha
        # but only this value is interesting for us

        line_search = sp.optimize.line_search(f, f1, xk, pk)
        alpha_k = line_search[0]
        if not alpha_k:
            alpha_k = 0.5

        # print(type(alpha_k), type(pk))
        print("Альфа: ", alpha_k)

        xkp1 = xk + alpha_k * pk
        sk = xkp1 - xk
        xk = xkp1

        print("Новый x_k:\n", xkp1)
        print("Разность относительно предыдущего:\n", sk)

        gfkp1 = fprime(xkp1)
        yk = gfkp1 - gfk
        gfk = gfkp1

        print("Новый градиент:\n", gfkp1)
        print("Разность относительно предыдущего градинта:\n", yk)

        k += 1

        ro = 1.0 / (np.dot(yk, sk))

        print("Ро вот такой: ", ro)

        A1 = I - ro * sk[:, np.newaxis] * yk[np.newaxis, :]
        A2 = I - ro * yk[:, np.newaxis] * sk[np.newaxis, :]
        Hk = np.dot(A1, np.dot(Hk, A2)) + (ro * sk[:, np.newaxis] *
                                           sk[np.newaxis, :])

        print("Новая обратная Гессе матрица:\n", Hk)

        print("__________________________________________________")

    return (xk, k)


result, k = bfgs_method(f, f1, np.array([0, -1]))

print('Result of BFGS method:')
print('Final Result (best point): %s' % (result))
print('Iteration Count: %s' % (k))

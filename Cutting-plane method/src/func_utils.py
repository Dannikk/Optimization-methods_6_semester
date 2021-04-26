import math as m
import numpy as np


def func(x_, a: float = 4, b: float = 3, c: float = 3) -> float:
    return a * x_[0] ** 2 + x_[1] ** 2 + m.cos(b * x_[0] + c * x_[1]) - x_[0] + 2 * x_[1] - x_[2]


def grad_func(x_, a: float = 4, b: float = 3, c: float = 3):
    return [2 * a * x_[0] - b * m.sin(b * x_[0] + c * x_[1]) - 1,
            2 * x_[1] - c * m.sin(b * x_[0] + c * x_[1]) + 2,
            -1]


def nl_func(x_):
    # костыль
    assert x_[1] <= 0
    return -x_[0] - 5*m.sqrt(-x_[1] - 0.75) + 2


def nl_grad(x_):
    return [-1, 5 / (2 * m.sqrt(-x_[1] - 0.75)), 0]


def l_func(x_, c_, const):
    return np.array(x_) @ np.array(c_) + const


def l_grad(x_, c_, const):
    c = c_.copy()
    return c

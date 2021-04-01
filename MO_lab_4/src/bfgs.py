import math as m
from numpy import *
from numpy.linalg import norm, inv
from scipy import optimize as opt

count = 0
d_count = 0
h_count = 0


def func(x_: array, a: float = 4, b: float = 3, c: float = 3) -> float:
    global count
    count += 1
    return a * x_[0] ** 2 + x_[1] ** 2 + m.cos(b * x_[0] + c * x_[1]) - x_[0] + 2 * x_[1]


def grad_func(x_: array, a: float = 4, b: float = 3, c: float = 3) -> array:
    global d_count
    d_count += 1
    return array(
        [2 * a * x_[0] - b * m.sin(b * x_[0] + c * x_[1]) - 1, 2 * x_[1] - c * m.sin(b * x_[0] + c * x_[1]) + 2])


# Так же рабочий алгоритм
def bfgs_step(a: array, x_d: array, omega_d: array) -> array:
    r = (a @ omega_d) / (omega_d @ (a @ omega_d)) - x_d / (x_d @ omega_d)
    a_ = a - outer(x_d, x_d) / (omega_d @ x_d) - \
         dot(outer(a @ omega_d, omega_d), a.transpose()) / (omega_d @ (a @ omega_d)) + \
         (omega_d @ (a @ omega_d)) * outer(r, r)
    return a_


# Работает некорректно
def wolfe_cond(x_k: array, p_k: array, c_1=0.0001, c_2=0.999) -> float:
    tmp = []
    for al in linspace(c_1, c_2, 100):
        if func(x_k + al*p_k) <= func(x_k) + c_1*al*(grad_func(x_k) @ p_k):
            if (grad_func(x_k + al*p_k) @ p_k) >= (c_2 * (grad_func(x_k) @ p_k)):
                tmp.append(al)
    if len(tmp) == 0:
        return False
    f_tmp = array([func(x_k + alpha*p_k) for alpha in tmp])
    tmpal = tmp[f_tmp.argmin()]
    return tmpal


def bfgs_step_2(a: array, x_d: array, omega_d: array) -> array:
    y = - omega_d
    s = x_d
    ro = 1 / float(y @ s)
    E = eye(2, dtype=float)
    a__ = ((E - ro * outer(s, y)) @ a) @ (E - ro * outer(y, s)) + outer(s, s) * ro

    return a__


def solver(start: array, eps: float) -> array:
    x = array(start)
    a_ = eye(2, dtype=float)
    step_count = 0
    while True:

        grad = grad_func(x)
        omega = - grad
        if norm(grad) < eps:
            print("Количество шагов: ", step_count)
            return x

        alpha_list = opt.line_search(func, grad_func, x, a_ @ omega)
        alpha = alpha_list[0]

        x_prev = x
        x = x + alpha * (a_ @ omega)
        delta_x = x - x_prev
        delta_omega = (- grad_func(x)) - omega

        a_ = bfgs_step_2(a_, delta_x, delta_omega)
        # a_ = bfgs_step(a_, delta_x, delta_omega)

        step_count += 1


def main():
    accurate_answer = array([0.09576339013, -1.116946441])
    print("\nМетод БФГШ\n")
    epsilons = [0.1, 0.01, 0.001, 0.0001]
    begin = (0, -1)
    for epsilon in epsilons:
        answer = solver(begin, epsilon)
        print("Ответ c точностью {:1.1e}: ".format(epsilon))
        for i in answer:
            print("{:1.3e}".format(i), end='  ')
        print("\nНорма невязки: {:1.3e}".format(norm(accurate_answer - answer)))
        print("_____________________________")


main()
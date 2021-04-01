import math as m
from src.golden_ratio import *
from numpy import *
from numpy.linalg import norm

count = 0
d_count = 0


def func(x_: array, a: float = 4, b: float = 3, c: float = 3) -> float:
    global count
    count += 1
    return a * x_[0] ** 2 + x_[1] ** 2 + m.cos(b * x_[0] + c * x_[1]) - x_[0] + 2 * x_[1]


def grad_func(x_: array, a: float = 4, b: float = 3, c: float = 3) -> array:
    global d_count
    d_count += 1
    return array([2 * a * x_[0] - b * m.sin(b * x_[0] + c * x_[1]) - 1,
                  2 * x_[1] - c * m.sin(b * x_[0] + c * x_[1]) + 2])


def solver(start: array, eps: float) -> array:
    x = array(start)
    step_count = 0
    while True:
        grad = grad_func(x)
        if norm(grad) < eps:
            print("Количество шагов: ", step_count)
            return x
        alpha = golden_solver(lambda al: func(x - al * grad))
        x = x - alpha * grad
        step_count += 1


def main():
    accurate_answer = array([ 0.09576339013, -1.116946441])
    print("\nГрадиентный метод наискорейшего спуска\n")
    epsilons = [0.1, 0.01, 0.001, 0.0001]
    begin = (0, 0)
    for epsilon in epsilons:
        answer = solver(begin, epsilon)
        print("Ответ c точностью {:1.1e}: ".format(epsilon))
        for i in answer:
            print("{:1.3e}".format(i), end='  ')
        print("\nНорма невязки: {:1.3e}".format(norm(accurate_answer - answer)))
        print("_____________________________")


main()

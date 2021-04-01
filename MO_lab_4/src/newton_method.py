import math as m
from numpy import *
from numpy.linalg import norm, inv

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
    return array([2 * a * x_[0] - b * m.sin(b * x_[0] + c * x_[1]) - 1,
                  2 * x_[1] - c * m.sin(b * x_[0] + c * x_[1]) + 2])


def hess(x_: array, a: float = 4, b: float = 3, c: float = 3) -> array:
    global h_count
    h_count += 1
    return array([[2 * a - m.cos(b * x_[0] + c * x_[1]) * b ** 2, - c * b * m.cos(b * x_[0] + c * x_[1])],
                 [- b * c * m.cos(b * x_[0] + c * x_[1]), 2 - m.cos(b * x_[0] + c * x_[1]) * c ** 2]])


def solver(start: array, eps: float, alpha: float = 1):
    x = array(start)
    step_count = 0
    while True:
        # print("Номер шага: {}".format(step_count))
        grad = grad_func(x)
        if norm(grad) < eps:
            # print("Ответ найден!")
            print("Количество шагов: ", step_count)
            return x
        hessian = hess(x)
        # print(hessian)
        # print(inv(hessian))
        # print(grad)
        # print(dot(inv(hessian), grad))
        x = x - alpha * dot(inv(hessian), grad)
        step_count += 1


def main():
    accurate_answer = array([ 0.09576339013, -1.116946441])
    print("\nМетод Ньютона\n")
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

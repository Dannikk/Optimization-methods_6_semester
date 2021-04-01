import math as mt

count = 0
a = 1.5
b = 2.0
delta = (b - a)*0.0001
epsilons = [0.1, 0.05, 0.01, 0.001]


def func(x: float) -> float:
    global count
    count += 1
    return x**4 + 4*x**2 - 32*x + 1


def solve(left: float, right: float, epsilon: float):
    global count
    count = 0
    while right - left > epsilon:
        x_1 = (left + right)/2 - delta
        x_2 = (left + right)/2 + delta
        f_1 = func(x_1)
        f_2 = func(x_2)
        if f_1 < f_2:
            right = x_2
        else:
            left = x_1

    answer = (left+right)/2
    print("Ответ: ", answer)
    print("Погрешность: {0:E}".format(mt.fabs(answer - 1.67)))
    print("Количество вызовов функции:", count)


for eps in epsilons:
    solve(a, b, eps)
    print("___________________")


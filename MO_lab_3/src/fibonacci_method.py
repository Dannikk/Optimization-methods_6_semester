import math as mt

count = 0
a = 1.5
b = 2.0
epsilons = [0.1, 0.05, 0.01, 0.001]
fib_list = [1, 1]


def func(x: float) -> float:
    global count
    count += 1
    return 4.2*x**2 + 23/x
    # return x**4 + 4*x**2 - 32*x + 1


def get_fibonacci(n: int):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return b


def fill_fib_list(fibs: list, size: int):
    while len(fibs) < size + 1:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def solve(left: float, right: float, fibs: list, number: int, epsilon: float):
    if len(fibs) <= number:
        fibs = fill_fib_list(fibs, number)
    global count
    count = 0
    i = 1
    x_1 = left + (right - left) * fibs[number - i - 1] / fibs[number - i + 1]
    x_2 = left + (right - left) * fibs[number - i] / fibs[number - i + 1]
    f_1 = func(x_1)
    f_2 = func(x_2)
    i += 1
    flag = ""
    while i < number:
        if f_1 < f_2:
            right = x_2
            x_2 = x_1
            x_1 = left + (right - left) * fibs[number - i - 1] / fibs[number - i + 1]
            f_2 = f_1
            flag = "left"
        else:
            left = x_1
            x_1 = x_2
            x_2 = left + (right - left) * fibs[number - i] / fibs[number - i + 1]
            f_1 = f_2
            flag = "right"

        if abs(right - left) < epsilon:
            break

        if right < left:
            print("uuuuuuuuuuuu")

        if flag == "left":
            f_1 = func(x_1)
        else:
            f_2 = func(x_2)
        i += 1
    answer = (left+right)/2

    print("Ответ: {0:2.5e}".format(answer))
    print("Погрешность: {0:E}".format(mt.fabs(answer - 1.67)))
    print("Количество вызовов функции:", count)
    return answer, left, right, abs(right - left) < epsilon


def solver_complex(left: float, right: float, fibs: list, num: int, epsilon: float):
    counter = 0
    global count
    while True:
        ans, left, right, success = solve(left, right, fibs, num, epsilon)
        print("left border {0:2.6e}, right border {1:2.6e}, function call {2:d}".format(left, right, count))
        counter += count
        if success:
            print("___________________________")
            print("Ответ: {0:2.5e}".format(ans))
            print("Итоговая погрешность: {0:E}".format(mt.fabs(ans - 1.67)))
            print("Итоговое количество вызовов функции:", counter)
            break


# for i, eps in zip([6, 7, 10, 15], [0.1, 0.05, 0.01, 0.001]):
#     print("N = ", i)
#     solve(a, b, fib_list, i, eps)
#     print("___________________")
#
# print()

# for i, eps in zip([5, 8], [10**-5, 10**-5]):
#     print("N = ", i)
#     solver_complex(a, b, fib_list, i, eps)
#     print("___________________")

# print(dict(zip(range(0, len(fib_list)), fill_fib_list(fib_list, 20))))

solve(0, 8, fib_list, 6, 0.001)
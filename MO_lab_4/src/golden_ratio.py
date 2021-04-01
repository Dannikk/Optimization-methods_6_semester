

def golden_solver(func, left: float = 0, right: float = 1, epsilon=10**-8) -> float:
    phi = (1 + 5 ** 0.5) / 2

    # while True:
    #     if right - left < epsilon:
    #         return (right - left) / 2
    #     a = left + (right - left) * (2 - phi)
    #     b = left + (right - left) * (1 / phi)
    #     f_1 = func(a)
    #     f_2 = func(b)
    #     if f_1 < f_2:
    #         left, right = left, b
    #     else:
    #         left, right = a, right

    if right - left < epsilon:
        return (right - left) / 2

    a = left + (right - left) * (2 - phi)
    b = left + (right - left) * (1 / phi)
    f_1 = func(a)
    f_2 = func(b)

    # step_count = 0
    while True:
        if right - left < epsilon:
            return (right + left) / 2
        # print(step_count)
        # step_count += 1
        if f_1 < f_2:
            right = b
            b = a
            a = left + (right - left) * (2 - phi)
            f_1, f_2 = func(a), f_1
        else:
            left = a
            a = b
            b = left + (right - left) * (1 / phi)
            f_1, f_2 = f_2, func(b)

import numpy as np
from numpy.linalg import norm
from src.simplex_utils import solve_simplex_method
import src.func_utils as funcs
import matplotlib.pyplot as plt


class Simplex:

    def __init__(self, A: list, b: list, restrictions: list):
        self.A = A
        self.b = b
        self.rests = restrictions
        assert (len(b) == len(A))
        self.height_of_A_matrix = len(b)
        self.width_of_A_matrix = len(A[0])

    # def get_value_of_phi_i(self, x: list, index: int) -> float:
    #     value = 0
    #     for cell_i, x_i in zip(self.A[index], x):
    #         value += cell_i * x_i
    #     value -= self.b[index]
    #     return value
    #
    # def get_phi(self, x: list):
    #     values = np.array([self.get_value_of_phi_i(x, i) for i in range(self.height_of_A_matrix)])
    #     index = values.argmax()
    #     return values[index], index

    # def get_grad(self, index: int):
    #     return self.A[index].copy()

    # def get_I_set(self, x: list) -> list:
    #     I_set = []
    #     for i in range(self.height_of_A_matrix):
    #         if self.get_value_of_phi_i(x, i) == self.get_phi(x)[0]:
    #             I_set.append(i)
    #     return I_set

    def get_value_of_phi_i(self, x: list, index: int) -> float:
        # value = 0
        # for cell_i, x_i in zip(self.rests[index], x):
        #     value += cell_i * x_i
        # value -= self.b[index]
        # if index == 0:
        #     return -1
        value = self.rests[index]['func'](x)
        return value

    def get_phi(self, x: list):
        values = np.array([self.get_value_of_phi_i(x, i) for i in range(len(self.rests))])
        # print("vals ", values)

        index = values.argmax()
        return values[index], index

    def get_grad(self, x: list):
        _, index = self.get_phi(x)
        # print("index", index)
        return self.rests[index].get("grad")(x)

    def add_cond(self, a: list, b: float):
        self.A.append(a)
        self.b.append(b)

    def get_A(self):
        return self.A

    def get_b(self):
        return self.b

    def height(self):
        return len(self.A)

    def width(self):
        return self.width_of_A_matrix


def vector_error(x1: list, x2: list):
    assert (len(x1) == len(x2))
    return norm(np.array(x1) - np.array(x2))


def main_step(S: Simplex, eps: float, acc_x: np.array):
    x_prev = [0 for i in range(S.width())]
    accuracy = []
    count = 0
    while True:
        # print(S.get_A(), "\n",  S.get_b())
        x = solve_simplex_method([0, 0, 1], S.get_A(), S.get_b())['x']

        #print(f"x_{count}: ", x)
        count += 1
        acc = np.linalg.norm(acc_x - np.array(x))
        accuracy.append(acc)
        # print("delta: ", acc)

        er_tmp = vector_error(x, x_prev)
        if er_tmp < eps:
            # print("Size = ", S.height())
            return x, accuracy

        a_k = S.get_grad(x)
        print(f"a_{count} = ", a_k)
        phi_k = S.get_phi(x)[0]
        b_k = np.array(a_k) @ np.array(x)
        b_k -= phi_k
        # b_k = np.array(a_k) @ np.array(x)
        # # print(x)
        # print("b_k = ", b_k)
        S.add_cond(a_k, b_k)

        x_prev = x


A_ = [[10, -7, 0],
      [-5, -3, 0],
      [0, 0, -1],
      [0, 0, 1],
      [0, 1, 0]]

b_ = [11, 4, 3, 0, -0.94]

# ???? ??????????????: 2.8720223735066988
rests = [{"type": "nonlinear", "func": funcs.func, "grad": funcs.grad_func},

         {"type": "linear", "func": lambda x: funcs.l_func(x, [10, -7, 0], const=-11),
          "grad": lambda x: funcs.l_grad(x, [10, -7, 0], const=-11)},

         {"type": "linear", "func": lambda x: funcs.l_func(x, [-5, -3, 0], const=-2.8720223735066988),
          "grad": lambda x: funcs.l_grad(x, [-5, -3, 0], const=-2.8720223735066988)},

         {"type": "nonlinear", "func": funcs.nl_func,
          "grad": funcs.nl_grad}]

# test_x = [[1, -1, 0],
#           [0, -1, 0],
#           [0, -1, 1],
#           [1, -1, 1],
#           [10, -10, 10]]

# for x__ in test_x:
#     print("for x = ", x__)
#     for i in range(len(rests)):
#         print("\t", rests[i]['func'](x__), "\t", rests[i]['grad'](x__))
#     print("_________________________________________")


accurate_answer = np.array([0.095763390134155385036, -1.1169464413924918844, -2.042360563911747473])
# epsilons = [10**-i for i in range(1, 10)]
# for eps in epsilons:
#     s = Simplex(A_, b_, rests)
#     answer, accuracy_seq = main_step(s, eps=eps, acc_x=accurate_answer)
#     print('????????????????: {:2.1e}'.format(eps), answer)
eps = 10**-6
s = Simplex(A_, b_, rests)
answer, accuracy_seq = main_step(s, eps=eps, acc_x=accurate_answer)

# fig = plt.figure()

x_ = np.linspace(1, len(accuracy_seq), len(accuracy_seq))
_, ax = plt.subplots(figsize=(10, 4))

ax.plot(x_, accuracy_seq, color='#539caf', alpha=1)
ax.scatter(x_, accuracy_seq, marker='o', c='r')

ax.set_title('???????????? ???????????? ?????????????????? ??????????????????????')
ax.set_xlabel("???????????????????????????????????? ?????????????? x_k")
ax.set_ylabel("????????????????")
ax.set_yscale('log')
# ax.set_xscale('log')

ax.grid(True)

# plt.grid(b=True)
# plt.plot(x_, accuracy_seq)
# plt.scatter(x_, accuracy_seq, marker='o', c='r')
plt.show()
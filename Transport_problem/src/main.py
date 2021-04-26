from src.transport_problem_solver import Solver
from numpy import *
import src.alien_mop as am

# rates_matrix = [[8, 2, 5, 3, 14],
#                 [10, 4, 5, 7, 15],
#                 [5, 1, 2, 1, 10],
#                 [6, 3, 2, 4, 15]]
#
# storage_volumes = [8, 3, 11, 5]
# destination_volumes = [4, 5, 4, 9, 5]

rates_matrix_1 = [[4.0, 4.5, 5.0, 5.5],
                  [4.2, 4.0, 4.5, 5.0],
                  [4.4, 4.2, 4.0, 4.5],
                  [4.6, 4.4, 4.2, 4.0]]

storage_volumes_1 = [50, 180, 280, 270]
destination_volumes_1 = [100, 200, 180, 300]

problem = Solver(rates_matrix_1, storage_volumes_1, destination_volumes_1)
problem.get_nord_west_decision()
print("Answer: {0:4.2f}".format(problem.potential_method()))

# x, u, m, n = am.method_of_potentials(array(rates_matrix), array(storage_volumes), array(destination_volumes))
# print(x, u, m, n)
# c, r = range(4), range(6)
# print(c[0], r[0])
# for i in c:
#     print(i, end="_")
# print()
# for i in r:
#     print(i, end="_")
# print()
# c = c[1:]
# for i in c:
#     print(i, end="_")
# print()
# for i in r:
#     print(i, end="_")
# print()
# am.method_of_potentials(array(rates_matrix), array(storage_volumes), array(destination_volumes))

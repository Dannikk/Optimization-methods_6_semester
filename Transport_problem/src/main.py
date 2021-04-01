from src.transport_problem_solver import Solver
from numpy import *
import src.alien_mop as am

rates_matrix = [[8, 2, 5, 3, 14],
                [10, 4, 5, 7, 15],
                [5, 1, 2, 1, 10],
                [6, 3, 2, 4, 15]]

storage_volumes = [8, 3, 11, 5]
destination_volumes = [4, 5, 4, 9, 5]

problem = Solver(rates_matrix, storage_volumes, destination_volumes)
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
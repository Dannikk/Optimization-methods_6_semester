import math
from typing import List, Any

from numpy import *

eps = 10 ** -13


class Solver:

    def __init__(self, rates_matrix, storages, destinations):
        self.rates = array(rates_matrix)
        self.dimension = self.rates.shape
        self.storages = array(storages)
        self.destinations = array(destinations)
        self.sup_vec_len = len(storages) + len(destinations) - 1
        self.sup_vec = []
        self.volumes_matrix = []
        m, n = self.rates.shape
        self.u_p, self.v_p = zeros(m), zeros(n)
        self.u_p[1:], self.v_p[:] = inf, inf
        self.coords_list = []
        for _ in storages:
            self.volumes_matrix.append(list('*' * len(self.destinations)))

        if sum(storages) != sum(destinations):
            print("Transport problem is not balanced!!!")

    def print_volumes_matrix(self):
        print("_" * 7 * len(self.volumes_matrix[0]))
        for string in self.volumes_matrix:
            for sym in string:
                if type(sym) == str:
                    print(" " * 6 + sym, end="")
                else:
                    print("{0:7.0f}".format(sym), end=""),
            print()
        print("_" * 7 * len(self.volumes_matrix[0]))

    def get_sup_vec_len(self) -> int:
        count = 0
        for string in self.volumes_matrix:
            count += string.count("*")
        return len(self.destinations) * len(self.storages) - count

    @staticmethod
    def get_rare_row_and_column(matrix_) -> list:
        i_rare = []
        j_rare = []
        for i, string in enumerate(matrix_):
            if string.count('*') == len(matrix_[0]) - 1:
                i_rare.append(i)
        for j in range(len(matrix_[0])):
            count = 0
            for i in range(len(matrix_)):
                if matrix_[i][j] != '*':
                    count += 1
            if count == 1:
                j_rare.append(j)
        coords = []
        for i in i_rare:
            for j in j_rare:
                coords.append((i, j))
        for index, (i, j) in enumerate(coords):
            if matrix_[i][j] != "*":
                coords.remove(coords[index])
        return coords

    def redegenerate_vec(self, count: int):
        coords = self.get_rare_row_and_column(self.volumes_matrix)
        for _ in range(count):
            if len(coords) != 0:
                self.volumes_matrix[coords[0][0]][coords[0][1]] = eps
                self.coords_list.append((coords[0][0], coords[0][1]))
                coords.remove(coords[0])

    def get_nord_west_decision(self):
        i, j, cell = 0, 0, 0
        stors = self.storages.copy()
        dests = self.destinations.copy()

        while j < len(dests) and i < len(stors):
            if dests[j] < stors[i]:
                self.volumes_matrix[i][j] = dests[j]
                dests[j] -= self.volumes_matrix[i][j]
                stors[i] -= self.volumes_matrix[i][j]
                self.coords_list.append((i, j))
                # j += 1
            else:
                self.volumes_matrix[i][j] = stors[i]
                dests[j] -= self.volumes_matrix[i][j]
                stors[i] -= self.volumes_matrix[i][j]
                self.coords_list.append((i, j))
                # i += 1
            # if strings in if/else are wrong
            if stors[i] == 0:
                i += 1
            if dests[j] == 0:
                j += 1

            # self.print_volumes_matrix()
        veclen = self.get_sup_vec_len()
        if veclen != self.sup_vec_len:
            self.redegenerate_vec(self.sup_vec_len - veclen)
        for i, string in enumerate(self.volumes_matrix):
            for j, num in enumerate(string):
                if num == "*":
                    self.volumes_matrix[i][j] = 0
        self.volumes_matrix = array(self.volumes_matrix)
        # self.coords_list = array(self.coords_list)
        self.print_volumes_matrix()

    def get_potentials(self):
        _u = []
        m, n = self.rates.shape
        self.u_p, self.v_p = zeros(m), zeros(n)
        self.u_p[1:], self.v_p[:] = inf, inf
        while len(_u) != len(self.coords_list):
            for i, j in self.coords_list:
                if not (i, j) in _u and not (isinf(self.u_p[i]) and isinf(self.v_p[j])):
                    if isinf(self.u_p[i]):
                        self.u_p[i] = self.v_p[j] - self.rates[i, j]
                    elif isinf(self.v_p[j]):
                        self.v_p[j] = self.rates[i, j] + self.u_p[i]
                    _u.append((i, j))

    @staticmethod
    def create_graph(E):
        G = {}
        for x, y in E:
            if x in G:
                G[x].append(y)
            else:
                G[x] = [y]
            if y in G:
                G[y].append(x)
            else:
                G[y] = [x]
        return G

    def dfs(self, graph, start, finish, cycle_path):
        cycle_path.append(start)
        if start == finish:
            return True, cycle_path
        for v in graph[start]:
            if v not in cycle_path:
                res = self.dfs(graph, v, finish, cycle_path)
                if res[0]:
                    return res
        cycle_path.pop()
        return False, []

    def get_cycle(self, max_from_deltas):
        _coords_list = list(map(lambda u: (u[0] - self.dimension[0], u[1]), self.coords_list))
        current_graph = self.create_graph(_coords_list)
        path = self.dfs(current_graph, max_from_deltas[0] - self.dimension[0], max_from_deltas[1], [])[1]
        cycle = [max_from_deltas]
        cycle.extend([(path[i] + self.dimension[0], path[i + 1])
                      if i % 2 == 0 else (path[i + 1] + self.dimension[0], path[i]) for i in range(len(path) - 1)])
        return cycle

    def potential_method(self):
        iterations = 0
        deltas = zeros(self.dimension)
        while True:
            self.get_potentials()
            for i in range(self.dimension[0]):
                for j in range(self.dimension[1]):
                    deltas[i, j] = self.v_p[j] - self.u_p[i] - self.rates[i, j]
            if (deltas <= 0).all():
                print("Optimum:")
                self.print_volumes_matrix()
                print("Iterations number: ", iterations)
                return sum(self.volumes_matrix * self.rates)
            max_from_deltas = unravel_index(deltas.argmax(), deltas.shape)
            current_cycle = self.get_cycle(max_from_deltas)
            neg_cycle_nodes = current_cycle[1::2]
            index = int(argmin([self.volumes_matrix[i, j] for i, j in neg_cycle_nodes]))
            i1, j1 = neg_cycle_nodes[index][0], neg_cycle_nodes[index][1]
            theta = self.volumes_matrix[i1, j1]
            for ind, (i, j) in enumerate(current_cycle):
                if ind % 2 == 0:
                    self.volumes_matrix[i, j] += theta
                else:
                    self.volumes_matrix[i, j] -= theta
            self.coords_list.remove((i1, j1))
            self.coords_list.append(max_from_deltas)
            iterations += 1

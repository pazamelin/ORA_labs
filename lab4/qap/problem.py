from typing import List
from random import randrange
from random import shuffle


class QAProblem:
    n: int
    dists: List[List[int]]
    flows: List[List[int]]

    def __init__(self, dists, flows):
        self.n = len(dists)
        self.dists = dists
        self.flows = flows


class QASolution:
    problem: QAProblem
    assignment: List[int]
    cost: int

    def __init__(self, problem, assignment=None, generate_random=False):
        self.problem = problem
        if assignment is None and generate_random:
            # generate random assignment
            self.assignment = [*range(0, problem.n, 1)]
            shuffle(self.assignment)

    def swap_two(self):
        # 2-opt -- swap two factories
        n = self.problem.n
        if n > 2:
            lhs = randrange(0, self.problem.n, 1)
            rhs = randrange(0, self.problem.n, 1)
            while lhs != rhs:
                rhs = randrange(0, self.problem.n, 1)
            self.assignment[lhs], self.assignment[rhs] = self.assignment[rhs], self.assignment[lhs]

    def swap(self, left, right):
        l_index = self.assignment.index(left)
        r_index = self.assignment.index(right)
        self.assignment[l_index] = right
        self.assignment[r_index] = left

    def swap_stochastic_2_opt(self):
        n = self.problem.n
        if n > 2:
            # choose 2 random cities
            lhs = randrange(0, self.problem.n, 1)
            rhs = randrange(0, self.problem.n, 1)
            while lhs != rhs:
                rhs = randrange(0, self.problem.n, 1)
            # rearrange cities in between
            mid = self.assignment[lhs:rhs]
            mid.reverse()
            self.assignment[lhs:rhs] = mid

    def compute_cost(self):
        result = 0
        n = self.problem.n
        for i in range(0, n, 1):
            for j in range(0, n, 1):
                for k in range(0, n, 1):
                    for l in range(0, n, 1):
                        if self.assignment[k] == i and self.assignment[l] == j:
                            result += self.problem.dists[i][j] * self.problem.flows[k][l]

        self.cost = result
        return result


def read_problem(filename):
    ifstream = open(filename, 'r')

    n = 0
    dists: List[List[int]] = []
    flows: List[List[int]] = []

    # read n
    line = ifstream.readline()
    line_split = line.split()
    n = int(line_split[0])

    # read distances
    for i in range(0, n, 1):
        line = ifstream.readline()
        line_split = line.split()
        map_object = map(int, line_split)
        dists.append(list(map_object))

    # discard the empty line
    ifstream.readline()

    # read flows
    for i in range(0, n, 1):
        line = ifstream.readline()
        line_split = line.split()
        map_object = map(int, line_split)
        flows.append(list(map_object))

    return QAProblem(dists, flows)


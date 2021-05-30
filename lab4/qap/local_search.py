import copy
from itertools import combinations
import numpy as np
from problem import *

def local_search(problem: QAProblem,
                 start_point: QASolution,
                 n_iterations: int):
    current_solution = start_point
    current_cost = start_point.compute_cost()
    print(start_point.assignment)
    dont_look_bits = np.zeros(problem.n, dtype=bool)
    for i in range(n_iterations):
        comb = combinations(np.arange(problem.n), 2)
        if np.all(dont_look_bits):
            break
        curr_city = 0
        counter = 0
        for opt in comb:
            if dont_look_bits[opt[0]] or dont_look_bits[opt[1]]:
                continue
            opt = list(opt)
            tmp_solution = copy.deepcopy(current_solution)
            tmp_solution.swap(opt[0], opt[1])
            cost = tmp_solution.compute_cost()
            if curr_city != opt[0] and counter == problem.n - 1 - curr_city:
                dont_look_bits[curr_city] = 1
                curr_city += 1
                counter = 0
            elif curr_city != opt[0]:
                curr_city += 1
                counter = 0
            if cost < current_cost:
                current_cost = cost
                current_solution = tmp_solution
                break
            elif curr_city == opt[0]:
                counter += 1

    return current_solution, current_cost


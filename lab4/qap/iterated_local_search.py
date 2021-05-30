from qap.problem import *
from qap.local_search import *

import copy


def iterated_local_search(problem, n_iterations, step_size, n_restarts):
    start_0 = QASolution(problem, assignment=None, generate_random=True)
    best_solution, best_cost = local_search(problem, start_0, n_iterations)

    for n in range(n_restarts):
        start_point = copy.deepcopy(best_solution)
        start_point.swap_stochastic_2_opt()

        solution, solution_cost = local_search(problem, start_point, n_iterations)
        # acceptance criterion
        if solution_cost < best_cost:
            best_solution, best_cost = solution, solution_cost

    return [best_solution, best_cost]
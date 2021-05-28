from problem import *

import copy


# hill climbing local search algorithm
def local_search(problem: QAProblem,
                 start_point: QASolution,
                 n_iterations: int,
                 step_size: int):

    # store the initial point
    solution = start_point
    solution_cost = start_point.compute_cost()

    # run the hill climb
    for i in range(0, n_iterations, 1):
        # take a step
        candidate = copy.deepcopy(solution)
        for j in range(0, step_size, 1):
            candidate.swap_two()

        # evaluate candidate point
        candidate_cost = candidate.compute_cost()
        # check if we should keep the new point
        if candidate_cost <= solution_cost:
            # store the new point
            solution, solution_eval = candidate, candidate_cost
    return [solution, solution_cost]


# iterated local search algorithm
def iterated_local_search(problem, n_iter, step_size, n_restarts, p_size):
    # define starting point
    best = QASolution(problem, assignment=None, generate_random=True)
    # evaluate current best point
    best_eval = best.compute_cost()

    # enumerate restarts
    for n in range(n_restarts):
        # generate an initial point as a perturbed version of the last best
        start_point = copy.deepcopy(best)
        for j in range(0, step_size, 1):
            start_point.swap_two()

        # perform a stochastic hill climbing search
        solution, solution_eval = local_search(problem, start_point, n_iter, step_size)
        # check for new best
        if solution_eval < best_eval:
            best, best_eval = solution, solution_eval

    return [best, best_eval]
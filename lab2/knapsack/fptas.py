from knapsack.problem import KnapsackProblem, KnapsackSolution
from knapsack.dynprog import knapsack_dp

from copy import deepcopy
from queue import Queue

import math


def fptas(problem, eps_parameter=0.5):
    """
        Fully Polynomial Time Approximation Scheme (FPTAS)
    """
    # find the maximum valued item
    max_valued_item = max(problem.items, key=lambda item: item.price)

    # compute prices adjustment factor
    k = (max_valued_item.price * eps_parameter) / problem.items.number_of_items

    # adjust prices
    for index in range(0, problem.number_of_items):
        problem.prices[index] = math.floor(problem.prices[index] / k)

    # run dp algorithm
    return knapsack_dp(problem)

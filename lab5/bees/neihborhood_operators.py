import random

from bees.problem import *

from typing import List, Dict
from random import randrange, shuffle, randint
import numpy as np


def random_swap(solution: VRSolution):
    lhs = random.randint(0, len(solution.routes) - 1)
    rhs = random.randint(0, len(solution.routes) - 1)
    solution.routes[lhs], solution.routes[rhs] = solution.routes[rhs], solution.routes[lhs]
    return solution


def reversing_subsequence(solution: VRSolution, sequence_length=5):
    start = random.randint(0, len(solution.routes) - 1)
    end = min(start + sequence_length, len(solution.routes))
    solution.routes[start:end] = reversed(solution.routes[start:end])
    return solution


def random_insert(solution: VRSolution):
    insert_point = random.randint(0, len(solution.routes) - 1)
    insert_position = random.randint(0, len(solution.routes) - 1)

    new_solution_vector = []
    if insert_point > insert_position:
        new_solution_vector = solution.routes[:insert_position]
        new_solution_vector.append(solution.routes[insert_point])
        new_solution_vector.append(solution.routes[insert_position:insert_point])
        new_solution_vector.append(solution.routes[insert_point:])
    else:
        new_solution_vector = solution.routes[:insert_point]
        new_solution_vector.append(solution.routes[insert_point:insert_position])
        new_solution_vector.append(solution.routes[insert_point])
        new_solution_vector.append(solution.routes[insert_position:])

    solution.routes = new_solution_vector
    return solution

from knapsack.problem import KnapsackProblem, KnapsackSolution
from knapsack.branch_and_bound import branch_and_bound

import random

random.seed(0)


def generate_problem(capacity, price_min, price_max, weight_min, weight_max, n):
    prices = []
    weights = []

    for i in range(0, n):
        prices.append(random.randint(price_min, price_max))
        weights.append(random.randint(weight_min, weight_max))

    return KnapsackProblem(capacity, prices, weights)


def stress_test_template(exact_algorithm_lhs,
                         exact_algorithm_rhs,
                         capacity=100,
                         price_min=10,
                         price_max=100,
                         weight_min=1,
                         weight_max=10,
                         n=100):
    problem = generate_problem(capacity, price_min, price_max, weight_min, weight_max, n)
    solution_lhs = exact_algorithm_lhs(problem)
    solution_rhs = exact_algorithm_rhs(problem)
    assert (solution_lhs == solution_rhs)

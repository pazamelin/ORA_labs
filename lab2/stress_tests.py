from knapsack.problem import KnapsackProblem, KnapsackSolution
from knapsack.branch_and_bound import branch_and_bound
from knapsack.dynprog import knapsack_dp
import random


# random.seed(0)


class ProblemGenerator:
    def __init__(self, capacity, seed=random.randint(0, 1000000)):
        self.capacity = capacity
        random.seed(seed)

        self.weight_min = 1
        self.weight_max = capacity - 1
        self.price_min = self.weight_min * 2
        self.price_max = self.weight_max * 2

    def __call__(self, number_of_items):
        prices = []
        weights = []

        for i in range(0, number_of_items):
            prices.append(random.randint(self.price_min, self.price_max))
            weights.append(random.randint(self.weight_min, self.weight_max))

        return KnapsackProblem(self.capacity, prices, weights)


def are_equal(solution_lhs, solution_rhs):
    return solution_lhs.profit == solution_rhs.profit


def stress_test_template(exact_algorithm_lhs,
                         exact_algorithm_rhs,
                         problem_generator,
                         n_min, n_max, n_step,
                         iterations_per_step=10,
                         verbose=False):

    for n in range(n_min, n_max, n_step):
        for iteration in range(0, iterations_per_step, 1):
            problem = problem_generator(n)
            solution_lhs = exact_algorithm_lhs(problem)
            solution_rhs = exact_algorithm_rhs(problem)
            result = are_equal(solution_lhs, solution_rhs)
            if verbose:
                result_label = 'OK' if result else 'FAIL'
                print('size: {}, iteration: {} --> {}'.format(n, iteration, result_label))


generator = ProblemGenerator(capacity=50)
stress_test_template(exact_algorithm_lhs=branch_and_bound,
                     exact_algorithm_rhs=knapsack_dp,
                     problem_generator=generator,
                     n_min=1, n_max=20, n_step=1,
                     verbose=True)

from knapsack.problem import KnapsackProblem, KnapsackSolution
from knapsack.dynprog import knapsack_dp
from knapsack.approx import approx
from knapsack.branch_and_bound import branch_and_bound
from knapsack.fptas import fptas
import numpy as np
import time


def read_int(file_path):
    result = np.loadtxt(file_path, delimiter='\t', dtype=np.int)
    result = int(result)
    return result


def read_list(file_path):
    result = np.loadtxt(file_path, delimiter='\t', dtype=np.int)
    result = list(result)
    return result


def solving_problem(file_path, algorithm):
    capacity = read_int(file_path + "/capacity.txt")
    weights = read_list(file_path + "/weights.txt")
    profits = read_list(file_path + "/profits.txt")
    solution = read_list(file_path + "/solution.txt")

    problem = KnapsackProblem(capacity, profits, weights)
    start_time = time.time()
    solution = algorithm(problem)
    running_time = (time.time() - start_time)

    return running_time


# problem 1

running_time_dp = solving_problem("benchmarks/01", knapsack_dp)
running_time_approx = solving_problem("benchmarks/01", approx)
running_time_bb = solving_problem("benchmarks/01", branch_and_bound)
running_time_fptas = solving_problem("benchmarks/01", fptas)

# problem 2

running_time_dp = solving_problem("benchmarks/02", knapsack_dp)
running_time_approx = solving_problem("benchmarks/02", approx)
running_time_bb = solving_problem("benchmarks/02", branch_and_bound)
running_time_fptas = solving_problem("benchmarks/02", fptas)

# problem 3

running_time_dp = solving_problem("benchmarks/03", knapsack_dp)
running_time_approx = solving_problem("benchmarks/03", approx)
running_time_bb = solving_problem("benchmarks/03", branch_and_bound)
running_time_fptas = solving_problem("benchmarks/03", fptas)

# problem 4

running_time_dp = solving_problem("benchmarks/04", knapsack_dp)
running_time_approx = solving_problem("benchmarks/04", approx)
running_time_bb = solving_problem("benchmarks/04", branch_and_bound)
running_time_fptas = solving_problem("benchmarks/04", fptas)

# problem 5

running_time_dp = solving_problem("benchmarks/05", knapsack_dp)
running_time_approx = solving_problem("benchmarks/05", approx)
running_time_bb = solving_problem("benchmarks/05", branch_and_bound)
running_time_fptas = solving_problem("benchmarks/05", fptas)

# problem 6

running_time_dp = solving_problem("benchmarks/06", knapsack_dp)
running_time_approx = solving_problem("benchmarks/06", approx)
running_time_bb = solving_problem("benchmarks/06", branch_and_bound)
running_time_fptas = solving_problem("benchmarks/06", fptas)

# problem 7

running_time_dp = solving_problem("benchmarks/07", knapsack_dp)
running_time_approx = solving_problem("benchmarks/07", approx)
running_time_bb = solving_problem("benchmarks/07", branch_and_bound)
running_time_fptas = solving_problem("benchmarks/07", fptas)

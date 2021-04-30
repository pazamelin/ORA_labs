from knapsack.problem import KnapsackProblem, KnapsackSolution
from knapsack.dynprog import knapsack_dp
from knapsack.approx import approx
from knapsack.branch_and_bound import branch_and_bound
from knapsack.fptas import fptas
import numpy as np
import time


def read_capacity(file_path):
    capacity = np.loadtxt(file_path, delimiter='\t', dtype=np.int)
    capacity = int(capacity)
    return capacity


def read_weights(file_path):
    weights = np.loadtxt(file_path, delimiter='\t', dtype=np.int)
    weights = list(weights)
    return weights


def read_profits(file_path):
    profits = np.loadtxt(file_path, delimiter='\t', dtype=np.int)
    profits = list(profits)
    return profits


def read_solution(file_path):
    solution = np.loadtxt(file_path, delimiter='\t', dtype=np.int)
    solution = list(solution)
    return solution


# problem 1

capacity = read_capacity("benchmarks/01/capacity.txt")
weights = read_weights("benchmarks/01/weights.txt")
profits = read_profits("benchmarks/01/profits.txt")
solution = read_solution("benchmarks/01/solution.txt")

problem = KnapsackProblem(capacity, profits, weights)

# dynprog

start_time = time.time()
solution_dp = knapsack_dp(problem)
time_dp_problem1 = (time.time() - start_time)

# 2-approx

start_time = time.time()
solution_approx = approx(problem)
time_approx_problem1 = (time.time() - start_time)

# branch_and_bound

start_time = time.time()
solution_bb = branch_and_bound(problem)
time_bb_problem1 = (time.time() - start_time)

# fptas

start_time = time.time()
solution_fptas = fptas(problem)
time_fptas_problem1 = (time.time() - start_time)


# problem 2

capacity = read_capacity("benchmarks/02/capacity.txt")
weights = read_weights("benchmarks/02/weights.txt")
profits = read_profits("benchmarks/02/profits.txt")
solution = read_solution("benchmarks/02/solution.txt")

problem = KnapsackProblem(capacity, profits, weights)

# dynprog

start_time = time.time()
solution_dp = knapsack_dp(problem)
time_dp_problem2 = (time.time() - start_time)

# 2-approx

start_time = time.time()
solution_approx = approx(problem)
time_approx_problem2 = (time.time() - start_time)

# branch_and_bound

start_time = time.time()
solution_bb = branch_and_bound(problem)
time_bb_problem2 = (time.time() - start_time)

# fptas

start_time = time.time()
solution_fptas = fptas(problem)
time_fptas_problem2 = (time.time() - start_time)

# problem 3

capacity = read_capacity("benchmarks/03/capacity.txt")
weights = read_weights("benchmarks/03/weights.txt")
profits = read_profits("benchmarks/03/profits.txt")
solution = read_solution("benchmarks/03/solution.txt")

problem = KnapsackProblem(capacity, profits, weights)

# dynprog

start_time = time.time()
solution_dp = knapsack_dp(problem)
time_dp_problem3 = (time.time() - start_time)

# 2-approx

start_time = time.time()
solution_approx = approx(problem)
time_approx_problem3 = (time.time() - start_time)

# branch_and_bound

start_time = time.time()
solution_bb = branch_and_bound(problem)
time_bb_problem3 = (time.time() - start_time)

# fptas

start_time = time.time()
solution_fptas = fptas(problem)
time_fptas_problem3 = (time.time() - start_time)

# problem 4

capacity = read_capacity("benchmarks/04/capacity.txt")
weights = read_weights("benchmarks/04/weights.txt")
profits = read_profits("benchmarks/04/profits.txt")
solution = read_solution("benchmarks/04/solution.txt")

problem = KnapsackProblem(capacity, profits, weights)

# dynprog

start_time = time.time()
solution_dp = knapsack_dp(problem)
time_dp_problem4 = (time.time() - start_time)

# 2-approx

start_time = time.time()
solution_approx = approx(problem)
time_approx_problem4 = (time.time() - start_time)

# branch_and_bound

start_time = time.time()
solution_bb = branch_and_bound(problem)
time_bb_problem4 = (time.time() - start_time)

# fptas

start_time = time.time()
solution_fptas = fptas(problem)
time_fptas_problem4 = (time.time() - start_time)

# problem 5

capacity = read_capacity("benchmarks/05/capacity.txt")
weights = read_weights("benchmarks/05/weights.txt")
profits = read_profits("benchmarks/05/profits.txt")
solution = read_solution("benchmarks/05/solution.txt")

problem = KnapsackProblem(capacity, profits, weights)

# dynprog

start_time = time.time()
solution_dp = knapsack_dp(problem)
time_dp_problem5 = (time.time() - start_time)

# 2-approx

start_time = time.time()
solution_approx = approx(problem)
time_approx_problem5 = (time.time() - start_time)

# branch_and_bound

start_time = time.time()
solution_bb = branch_and_bound(problem)
time_bb_problem5 = (time.time() - start_time)

# fptas

start_time = time.time()
solution_fptas = fptas(problem)
time_fptas_problem5 = (time.time() - start_time)

# problem 6

capacity = read_capacity("benchmarks/06/capacity.txt")
weights = read_weights("benchmarks/06/weights.txt")
profits = read_profits("benchmarks/06/profits.txt")
solution = read_solution("benchmarks/06/solution.txt")

problem = KnapsackProblem(capacity, profits, weights)

# dynprog

start_time = time.time()
solution_dp = knapsack_dp(problem)
time_dp_problem6 = (time.time() - start_time)

# 2-approx

start_time = time.time()
solution_approx = approx(problem)
time_approx_problem6 = (time.time() - start_time)

# branch_and_bound

start_time = time.time()
solution_bb = branch_and_bound(problem)
time_bb_problem6 = (time.time() - start_time)

# fptas

start_time = time.time()
solution_fptas = fptas(problem)
time_fptas_problem6 = (time.time() - start_time)

# problem 7

capacity = read_capacity("benchmarks/07/capacity.txt")
weights = read_weights("benchmarks/07/weights.txt")
profits = read_profits("benchmarks/07/profits.txt")
solution = read_solution("benchmarks/07/solution.txt")

problem = KnapsackProblem(capacity, profits, weights)

# dynprog

start_time = time.time()
solution_dp = knapsack_dp(problem)
time_dp_problem7 = (time.time() - start_time)

# 2-approx

start_time = time.time()
solution_approx = approx(problem)
time_approx_problem7 = (time.time() - start_time)

# branch_and_bound

start_time = time.time()
solution_bb = branch_and_bound(problem)
time_bb_problem7 = (time.time() - start_time)

# fptas

start_time = time.time()
solution_fptas = fptas(problem)
time_fptas_problem7 = (time.time() - start_time)

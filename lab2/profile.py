from knapsack.problem import KnapsackProblem, KnapsackSolution
from knapsack.dynprog import knapsack_dp
from knapsack.approx import approx
from knapsack.branch_and_bound import branch_and_bound
from knapsack.fptas import fptas
import numpy as np
import pandas as pd
import time


def put(dataframe, filename):
    """
    saves pandas dataframe to a csv file named @filename
    """
    dataframe.to_csv(filename, index=True)


def read_int(file_path):
    result = np.loadtxt(file_path, delimiter='\t', dtype=np.int)
    result = int(result)
    return result


def read_list(file_path):
    result = np.loadtxt(file_path, delimiter='\t', dtype=np.int)
    result = list(result)
    return result


def solving_problem(file_path, algorithm):
    capacity_data = read_int(file_path + "/capacity.txt")
    weights_data = read_list(file_path + "/weights.txt")
    profits_data = read_list(file_path + "/profits.txt")
    solution_data = read_list(file_path + "/solution.txt")

    profit_data = 0
    for i in range(0, len(solution_data), 1):
        if solution_data[i]:
            profit_data += profits_data[i]

    problem = KnapsackProblem(capacity_data, profits_data, weights_data)

    start_time = time.time()
    solution = algorithm(problem)
    running_time = (time.time() - start_time)

    return running_time, solution.counter_of_comparisons, solution.profit, profit_data


algorithms = [knapsack_dp, approx, branch_and_bound, fptas]
names = ['knapsack_dp', 'approx', 'branch_and_bound', 'fptas']
profiling_results = pd.DataFrame(columns=['benchmark', 'algorithm', 'time', 'operations', 'profit', 'profit_dataset'])

row_index = 0
for benchmark_index in range(1, 8, 1):
    for algorithm_index in range(0, len(algorithms), 1):
        running_time, comparisons, profit, profit_d = solving_problem("benchmarks/0" + str(benchmark_index),
                                                                      algorithms[algorithm_index])

        profiling_results.loc[row_index] = [str(benchmark_index),
                                            names[algorithm_index],
                                            running_time,
                                            comparisons,
                                            profit,
                                            profit_d]
        print(row_index)
        row_index += 1

put(profiling_results, 'results.csv')

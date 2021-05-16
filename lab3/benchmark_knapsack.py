from knapsack.knapsack import genetic_knapsack
from knapsack.knapsack import Item

import numpy as np
import pandas as pd
import time


def put(dataframe, filename):
    dataframe.to_csv(filename, index=True)


def read_int(file_path):
    result = np.loadtxt(file_path, delimiter='\t', dtype=np.int)
    result = int(result)
    return result


def read_list(file_path):
    result = np.loadtxt(file_path, delimiter='\t', dtype=np.int)
    result = list(result)
    return result


def solving_problem(file_path):
    capacity_data = read_int(file_path + "/capacity.txt")
    weights_data = read_list(file_path + "/weights.txt")
    profits_data = read_list(file_path + "/profits.txt")
    solution_data = read_list(file_path + "/solution.txt")

    items = []
    for i in range(len(weights_data)):
        items.append(Item(p=profits_data[i], w=weights_data[i]))

    start_time = time.time()
    solution, solution_fit = genetic_knapsack(items, capacity_data)
    running_time = (time.time() - start_time)

    return running_time, solution, solution_data, solution_fit


profiling_results = pd.DataFrame(columns=['benchmark', 'average time', 'genetic solution', 'best solution'])
repeats = 5
row_index = 0
solutions_fits = []
solutions = []
average_time = 0
best_solution = []

for benchmark_index in range(1, 8, 1):
    for iteration in range(0, repeats, 1):
        running_time, solution, solution_data, solution_fit = solving_problem("benchmarks/knapsack/0"
                                                                              + str(benchmark_index))
        average_time += running_time
        solutions_fits.append(solution_fit)
        solutions.append(solution)
        best_solution = solution_data

    average_time /= repeats
    solution_index = solutions_fits.index(max(solutions_fits))

    profiling_results.loc[row_index] = [str(benchmark_index),
                                        average_time,
                                        solutions[solution_index],
                                        best_solution]
    print(row_index)
    row_index += 1

put(profiling_results, "benchmarks/knapsack/result.csv")
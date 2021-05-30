from qap.problem import *
from qap.local_search import *
from qap.iterated_local_search import *

import time
import pandas as pd


def put(dataframe, filename):
    dataframe.to_csv(filename, index=True)


path = 'benchmarks/data/'
names = ['tai20a', 'tai40a', 'tai60a', 'tai80a', 'tai100a']
result = pd.DataFrame(columns=['benchmark', 'algorithm', 'time', 'answer'])
repeat = 2
result_row = 0

n_iterations = 5
step_size = 5
restarts = 2

for name in names:
    problem = read_problem(path + name)
    ls_total_time = 0.0
    ils_total_time = 0.0
    ls_best_solution = QASolution(problem, assignment=None, generate_random=True)
    ils_best_solution = QASolution(problem, assignment=None, generate_random=True)
    ls_best_cost = float("inf")
    ils_best_cost = float("inf")

    for i in range(1, repeat, 1):
        print(i)

        # LS
        random_point = QASolution(problem, assignment=None, generate_random=True)
        start = time.time()
        ls_solution, ls_cost = local_search(problem, random_point, n_iterations)
        end = time.time()
        ls_total_time += end - start
        if ls_cost < ls_best_cost:
            ls_best_solution, ls_best_cost = ls_solution, ls_cost

        # ILS
        random_point = QASolution(problem, assignment=None, generate_random=True)
        start = time.time()
        ils_solution, ils_cost = iterated_local_search(problem, n_iterations, step_size, restarts)
        end = time.time()
        ils_total_time += end - start
        if ils_cost < ils_best_cost:
            ils_best_solution, ils_best_cost = ils_solution, ils_cost

    ls_average_time = ls_total_time / repeat
    result.loc[result_row] = [name, 'LS', ls_best_cost, ls_average_time]
    result_row += 1

    ls_solution_file = open('benchmarks/solutions/local_search/' + name + '.sol', 'w')
    ls_solution_str = [str(factory) for factory in ls_best_solution.assignment]
    ls_solution_file.write(' '.join(ls_solution_str))
    ls_solution_file.close()

    ils_average_time = ils_total_time / repeat
    result.loc[result_row] = [name, 'ILS', ils_best_cost, ils_average_time]
    result_row += 1

    ils_solution_file = open('benchmarks/solutions/iterated_local_search/' + name + '.sol', 'w')
    ils_solution_str = [str(factory) for factory in ils_best_solution.assignment]
    ils_solution_file.write(' '.join(ils_solution_str))
    ils_solution_file.close()

put(result, "result.csv")
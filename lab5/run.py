from bees.problem import *
from bees.algorithm import *

import time
import pandas as pd
import os


def read_benchmark(filename):
    file = open(os.path.join(path, benchmark), 'r')

    # discard name line
    file.readline()

    # read comment line
    comment = file.readline()

    # extract number of trucks
    i1 = comment.find('No of trucks: ') + len('No of trucks: ')
    i2 = comment.find(',', i1)
    number_of_trucks = int(comment[i1:i2])

    # extract optimal value
    i1 = comment.find('Optimal value: ') + len('Optimal value: ')
    i2 = comment.find(')', i1)
    optimal_value = int(comment[i1:i2])

    # read dimension
    file.readline()
    dimension = file.readline()
    i1 = dimension.find('DIMENSION : ') + len('DIMENSION : ')
    dimension = int(dimension[i1:])

    # read capacity
    file.readline()
    capacity = file.readline()
    i1 = capacity.find('CAPACITY : ') + len('CAPACITY : ')
    capacity = int(capacity[i1:])

    nodes = {}

    # read node coordinates section
    file.readline()
    for i in range(0, dimension):
        values = file.readline().split()
        index, x, y = [int(values[i]) for i in (0, 1, 2)]
        nodes[index] = Node(index, -1, x, y)

    # read demand section
    file.readline()
    for i in range(0, dimension):
        values = file.readline().split()
        index, demand = [int(values[i]) for i in (0, 1)]
        nodes[index].demand = demand

    file.close()

    nodes_list = list(nodes.values())
    result = VRProblem(number_of_trucks, capacity, nodes_list)
    return result, optimal_value


def save_solutions(solution_to_save, filename):
    f = open(filename, "w")

    route_delimiters = [i for i, x in enumerate(solution_to_save.routes) if x == 0]
    route_delimiters.append(len(solution_to_save.routes))

    current_route = 1
    current_position = 0
    # enumerating routes:
    for route in range(0, len(route_delimiters), 1):
        if route_delimiters[route] <= len(solution_to_save.routes):
            route_list = solution_to_save.routes[current_position:route_delimiters[route]]
            f.write('Route #{}: '.format(current_route) + ' '.join([str(node) for node in route_list]) + '\n')

            current_route += 1
            current_position += abs(current_position - route_delimiters[route]) + 1

    f.write('cost {}\n'.format(solution_to_save.cost_clean))
    f.close()


folder = 'benchmarks/data/'
prefixes = ['A/', 'B/']
#prefixes = ['A/']
#prefixes = ['B/']
benchmarks_A = []
results_A = []
optimals_A = []

benchmarks_B = []
results_B = []
optimals_B = []

for prefix in prefixes:
    path = folder + prefix
    benchmark_list = os.listdir(path)
    for benchmark in benchmark_list:
        if os.path.isfile(os.path.join(path, benchmark)):
            problem, optimal_value = read_benchmark(filename=path + benchmark)
            length_limit = (problem.number_of_nodes / problem.number_of_trucks) * 2
            problem.set_cost_function_parameters(0.5, 0.5, problem.truck_capacity, length_limit)

            print('running {} ...'.format(benchmark))

            solution = bee_algorithm(problem, 10, 10, 50, 20)
            save_solutions(solution, 'benchmarks/solutions/' + prefix + '/' + benchmark[:-3] + 'sol')

            print('done {}!'.format(benchmark))
            print()

            if prefix == 'A/':
                benchmarks_A.append(benchmark)
                results_A.append(solution.cost_clean)
                optimals_A.append(optimal_value)
            else:
                benchmarks_B.append(benchmark)
                results_B.append(solution.cost_clean)
                optimals_B.append(optimal_value)

# result plots:
import plot
plot.plot_benchmarking_results(benchmarks_A, results_A, optimals_A, 'A_cmp')
plot.plot_benchmarking_results(benchmarks_B, results_B, optimals_B, 'B_cmp')
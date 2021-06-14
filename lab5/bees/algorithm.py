from bees.problem import *
from bees.neihborhood_operators import *
from typing import List, Dict
from random import randrange
from random import shuffle
import random
from itertools import repeat
import numpy as np
import copy


def generate_random_solution(problem):
    # A solution is constructed by assigning one node at a time to one of the m vehicle routes.
    # The selection of the node is randomly made
    # m = number_of_trucks

    routes: List[List[int]] = [[] for i in repeat(None, problem.number_of_trucks)]
    nodes = [i for i in range(1, problem.number_of_nodes + 1)]
    random.shuffle(nodes)

    for node_index in nodes:
        # The node is then assigned to the location that
        # minimizes the cost of assigning this customer over the current set of vehicle routes.

        assigning_costs = []
        for route in range(0, problem.number_of_trucks):
            assigning_cost = 0
            node = problem.node_by_index[node_index]

            if len(routes[route]) == 0:
                # if route is empty, than assigning cost is equal to distance from
                # the warehouse to the node
                warehouse = problem.node_by_index[1]
                assigning_cost = warehouse.distance(node)
            else:
                # assigning cost is equal to distance from the last node in the route
                last_node = problem.node_by_index[routes[route][-1]]
                assigning_cost = last_node.distance(node)

            assigning_costs.append(assigning_cost)

        min_assigning_cost, idx = min((val, idx) for (idx, val) in enumerate(assigning_costs))
        routes[idx].append(node_index)

    # Join routes to one solution vector with delimiters
    route_list: List[int] = []
    for route in routes:
        for node_index in route:
            route_list.append(node_index)
        route_list.append(0)

    route_list.pop()

    return VRSolution(problem, route_list)


def roulette_wheel_selection(food_sources: List[VRSolution]):
    # The total sum of the food_sources fitness
    total_fitness = sum([(1.0 / source.cost_function()) for source in food_sources])
    food_sources_indexes = range(0, len(food_sources), 1)

    # Selection probabilities for each source
    source_probabilities = [(1.0 / source.cost_function()) / total_fitness for source in food_sources]

    # Selects one source based on the computed probabilities
    chosen_index = np.random.choice(food_sources_indexes, 1, p=source_probabilities)
    return chosen_index[0]

def apply_neighbor_operator(solution, neighborhood_operators):
    # generate neighbor
    neighbor = copy.deepcopy(solution)
    neighborhood_operator_index = random.randint(0, len(neighborhood_operators) - 1)
    neighborhood_operator = neighborhood_operators[neighborhood_operator_index]
    neighbor = neighborhood_operator(neighbor)
    return neighbor


def bee_algorithm(problem, workers, observers, iterations_limit, updates_attempts_limit):
    neighborhood_operators = [random_swap, reversing_subsequence, random_insert]
    food_sources: List[VRSolution] = []

    # generate initial food sources (solutions)
    for i in range(0, workers):
        random_food_source = generate_random_solution(problem)
        random_food_source.cost = random_food_source.cost_function()
        food_sources.append(random_food_source)

    for iteration in range(0, iterations_limit):
        for k in range(0, len(food_sources)):
            # worker generates neighbor for it's food source
            neighbor = apply_neighbor_operator(food_sources[k], neighborhood_operators)

            # check if better
            neighbor.cost = neighbor.cost_function()
            if neighbor.cost < food_sources[k].cost:
                # is better - replace and zero out the UA counter
                food_sources[k].update_attempt_counter = 0
                food_sources[k] = neighbor
            else:
                food_sources[k].update_attempt_counter += 1

        neighbor_solutions = {}
        for k in range(0, observers):
            # observer chooses a food source
            index = roulette_wheel_selection(food_sources)
            # observer generates neighbor for the food source
            neighbor = apply_neighbor_operator(food_sources[index], neighborhood_operators)
            neighbor.cost = neighbor.cost_function()
            # save generated neighbor to the set of neighbor solutions
            if index not in neighbor_solutions:
                neighbor_solutions[index] = []
            neighbor_solutions[index].append(neighbor)

        for k in range(0, len(food_sources)):
            if k in neighbor_solutions:
                best_neighbor = max(neighbor_solutions[k], key=lambda solution: solution.cost)

                # check if the best neighbor better
                best_neighbor.cost = best_neighbor.cost_function()
                if best_neighbor.cost < food_sources[k].cost:
                    # is better - replace and zero out the UA counter
                    food_sources[k].update_attempt_counter = 0
                    food_sources[k] = best_neighbor
                else:
                    food_sources[k].update_attempt_counter += 1

        food_sources_with_violated_capacity = 0
        food_sources_with_violated_length = 0

        for k in range(0, len(food_sources)):
            if food_sources[k].update_attempt_counter == updates_attempts_limit:
                random_food_source = generate_random_solution(problem)
                random_food_source.cost = random_food_source.cost_function()
                food_sources[k] = random_food_source

            if food_sources[k].is_capacity_violated:
                food_sources_with_violated_capacity += 1

            if food_sources[k].is_length_violated:
                food_sources_with_violated_length += 1

        if food_sources_with_violated_capacity > len(food_sources) / 2:
            problem.alpha /= 2
        else:
            problem.alpha *= 2

        if food_sources_with_violated_length > len(food_sources) / 2:
            problem.beta /= 2
        else:
            problem.beta *= 2

    best_solution_yet = max(food_sources, key=lambda solution: solution.cost)
    return best_solution_yet

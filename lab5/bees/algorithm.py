from bees.problem import *

from typing import List, Dict
from random import randrange
from random import shuffle
import random
from itertools import repeat



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


def bee_algorithm(problem):
    pass

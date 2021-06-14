from typing import List, Dict
from random import randrange
from random import shuffle
import numpy as np


class Node:
    index: int
    demand: int
    x: int
    y: int

    def __init__(self, index, demand, x, y):
        self.index = index
        self.demand = demand
        self.x = x
        self.y = y

    def distance(self, other):
        self_to_c = abs(self.x - other.x)
        c_to_other = abs(self.y - other.y)
        distance = np.sqrt(self_to_c ** 2 + c_to_other ** 2)
        return distance


class VRProblem:
    number_of_trucks: int
    truck_capacity: int
    number_of_nodes: int
    nodes: List[Node]
    node_by_index: Dict[int, Node]

    # cost function parameters:
    alpha: int
    beta: int
    route_capacity_limit: int
    route_length_limit: int

    def __init__(self, number_of_trucks, truck_capacity, nodes):
        self.number_of_trucks = number_of_trucks
        self.truck_capacity = truck_capacity
        self.number_of_nodes = len(nodes)
        self.nodes = nodes

        self.node_by_index = {}
        for node in nodes:
            self.node_by_index[node.index] = node

    def set_cost_function_parameters(self, alpha, beta, route_capacity_limit, route_length_limit):
        self.alpha = alpha
        self.beta = beta
        self.route_capacity_limit = route_capacity_limit
        self.route_length_limit = route_length_limit


class VRSolution:
    routes: List[int]
    problem: VRProblem
    update_attempt_counter: int = 0
    cost: float
    cost_clean: float

    is_capacity_violated = False
    is_length_violated = False

    def __init__(self, problem, routes):
        self.routes = routes
        self.problem = problem

    def cost_function(self):
        # solution form:
        # 1 2 0 3 4 0 5 6
        #  0 - route delimiter

        total_cost = 0
        total_length_violation = 0
        total_capacity_violation = 0

        route_delimiters = [i for i, x in enumerate(self.routes) if x == 0]
        route_delimiters.append(len(self.routes))

        current_position = 0
        # enumerating routes:
        for route in range(0, len(route_delimiters), 1):
            if route_delimiters[route] <= len(self.routes):
                route_cost, \
                route_length_violation, \
                route_capacity_violation = \
                    self.route_cost_function(current_position, route_delimiters[route])

                total_cost += route_cost
                total_length_violation += route_length_violation
                total_capacity_violation += route_capacity_violation

                current_position += abs(current_position - route_delimiters[route]) + 1

        result = total_cost
        result += self.problem.alpha * total_capacity_violation
        result += self.problem.beta * total_length_violation

        if total_length_violation > 0:
            self.is_length_violated = True

        if total_capacity_violation > 0:
            self.is_capacity_violated = True

        self.cost_clean = total_cost
        return result

    def route_cost_function(self, route_start, route_end):
        # print(route_start, '--', route_end)
        route_cost = 0
        route_length = 0
        route_capacity = 0

        if route_start == route_end:
            return 0, 0, 0

        # add distance from the warehouse
        warehouse = self.problem.node_by_index[1]
        first_node = self.problem.node_by_index[self.routes[route_start]]
        route_cost += warehouse.distance(first_node)

        for j in range(route_start, route_end, 1):
            node_index = self.routes[j]
            node = self.problem.node_by_index[node_index]

            # add distance to the next node in the route
            if j != route_end - 1:
                next_node_index = self.routes[j + 1]
                next_node = self.problem.node_by_index[next_node_index]
                route_cost += node.distance(next_node)

            route_length += 1
            route_capacity += node.demand

            # add distance to the warehouse
        warehouse = self.problem.node_by_index[1]
        last_node = self.problem.node_by_index[self.routes[route_end - 1]]
        route_cost += warehouse.distance(last_node)

        length_violation = abs(self.problem.route_length_limit - route_length)
        capacity_violation = abs(self.problem.route_capacity_limit - route_capacity)

        return route_cost, length_violation, capacity_violation

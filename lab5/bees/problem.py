from typing import List
from random import randrange
from random import shuffle


class Node:
    index: int
    demand: int
    x: int
    y: int

    def __init__(self, index, demand, x, y):
        self.index = index
        self.x = x
        self.y = y


class VRProblem:
    number_of_trucks: int
    truck_capacity: int
    number_of_nodes: int
    nodes: List[Node]

    def __init__(self, number_of_trucks, truck_capacity, nodes):
        self.number_of_trucks = number_of_trucks
        self.truck_capacity = truck_capacity
        self.number_of_nodes = len(nodes)
        self.nodes = nodes

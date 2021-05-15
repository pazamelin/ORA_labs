import numpy as np
import random
from typing import List
import matplotlib.pyplot as plt


class City:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        self_to_c = abs(self.x - other.x)
        c_to_other = abs(self.y - other.y)
        distance = np.sqrt(self_to_c ** 2 + c_to_other ** 2)
        return distance

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class Route:
    cities: List[City]
    distance: int = None

    def __init__(self, cities):
        self.cities = cities

    def __getitem__(self, index):
        return self.cities[index]

    def __setitem__(self, index, value):
        self.cities[index] = value

    def __len__(self):
        return len(self.cities)

    def get_distance(self):
        self.distance = 0
        for src, dst in zip(self.cities[:-1], self.cities[1:]):
            self.distance += src.distance(dst)
        return self.distance


def random_route(cities: List[City]):
    route_cities = random.sample(cities, len(cities))
    return Route(route_cities)


def roulette_wheel_selection(population: List[Route], size):
    # The total sum of the population distance
    population_fitness = sum([(1.0 / route.get_distance()) for route in population])
    population_indexes = range(0, len(population), 1)

    # Selection probabilities for each route
    route_probabilities = [(1.0 / route.get_distance()) / population_fitness for route in population]
    # route_probabilities = 1 - np.array(route_probabilities)

    # Selects one chromosome based on the computed probabilities
    chosen_indexes = np.random.choice(population_indexes, size, p=route_probabilities)
    parents = [population[i] for i in chosen_indexes]
    return parents


def mutate(route: Route):
    n = len(route)
    if n > 1:
        lhs = random.randint(0, n - 1)
        rhs = random.randint(0, n - 1)
        while rhs != lhs:
            rhs = random.randint(0, n - 1)

        route[lhs], route[rhs] = route[rhs], route[lhs]


def crossover(route_lhs: Route, route_rhs: Route):
    n = len(route_lhs)
    crossover_point = random.randint(0, n - 1)

    new_route = route_lhs.cities[:crossover_point]
    cities_taken = set(new_route)
    for city in route_rhs.cities:
        if city not in cities_taken:
            cities_taken.add(city)
            new_route.append(city)

    return Route(new_route)


def run(cities: List[City], population_size, selection_size, mutation_rate, iterations, name=''):
    population: List[Route] = []
    best_for_iteration = []

    for i in range(0, population_size, 1):
        population.append(random_route(cities))

    for iteration in range(0, iterations, 1):
        print(iteration)
        parents = roulette_wheel_selection(population, selection_size)

        next_generation = parents
        while len(next_generation) < population_size:
            parent_lhs = parents[random.randint(0, len(parents) - 1)]
            parent_rhs = parents[random.randint(0, len(parents) - 1)]
            next_generation.append(crossover(parent_lhs, parent_rhs))

        for member in next_generation:
            is_mutate = np.random.choice([False, True], 1, p=[1 - mutation_rate, mutation_rate])
            if is_mutate:
                mutate(member)

        population = next_generation
        best_for_iteration.append(max(population, key=lambda m: m.get_distance()))

    plot_progress(best_for_iteration, name)
    return best_for_iteration[-1]


def plot_progress(best_for_iteration: List[Route], name):
    # plot
    xsize = 15
    ysize = 5
    max_xlabels = 50

    fig = plt.figure(figsize=(xsize, ysize))
    ax = plt.axes()
    ax.xaxis.set_major_locator(plt.MaxNLocator(max_xlabels))

    plt.xticks(rotation=90)
    plt.xlabel('iteration')
    plt.ylabel('weight')
    plt.grid()

    ax.plot(range(0, len(best_for_iteration), 1),
            [route.get_distance() for route in best_for_iteration])

    plt.savefig('benchmarks/tsp/plots/' + name + '.png')

import random


class Item(object):
    def __init__(self, p, w):
        self.profit = p
        self.weight = w


population_size = 30

numb_of_generations = 30


def fitness(target, items, capacity):
    total_value = 0
    total_weight = 0
    index = 0
    for i in target:
        if index >= len(items):
            break
        if i == 1:
            total_value += items[index].profit
            total_weight += items[index].weight
        index += 1

    if total_weight > capacity:
        return 0
    else:
        return total_value


def mutate(target):
    r = random.randint(0, len(target)-1)
    if target[r] == 1:
        target[r] = 0
    else:
        target[r] = 1


def evolve_population(population):
    parent_eligibility = 0.2
    mutation_chance = 0.05
    parent_lottery = 0.05

    parent_length = int(parent_eligibility*len(population))
    parents = population[:parent_length]
    nonparents = population[parent_length:]

    for np in nonparents:
        if parent_lottery > random.random():
            parents.append(np)

    for p in parents:
        if mutation_chance > random.random():
            mutate(p)

    children = []
    desired_length = len(population) - len(parents)
    while len(children) < desired_length:
        male = population[random.randint(0, len(parents)-1)]
        female = population[random.randint(0, len(parents)-1)]
        half = len(male)/2
        half = int(half)
        child = male[:half] + female[half:]
        if mutation_chance > random.random():
            mutate(child)
        children.append(child)

    parents.extend(children)
    return parents


def genetic_knapsack(items, capacity):
    population = [[random.randint(0, 1) for x in range(0, len(items))] for x in range(0, population_size)]
    result = []
    res_fit = 0
    for g in range(0, numb_of_generations):
        population = sorted(population, key=lambda x: fitness(x, items, capacity), reverse=True)
        population = evolve_population(population)

    for i in range(population_size - 1, 0, -1):
        if fitness(population[i], items, capacity) > 0:
            result = population[i]
            break
    res_fit = fitness(result, items, capacity)

    return result, res_fit

from typing import List


def is_positive_integer(x):
    return x > 0


class KnapsackItem:
    """ Class holding Knapsack item data """

    def __init__(self, price, weight):
        self.price = price
        self.weight = weight


class KnapsackProblem:
    """ Class holding 0-1 Knapsack problem data """
    capacity: int
    items: List[KnapsackItem]
    number_of_items: int

    def __init__(self,
                 capacity: int,
                 prices: List[int],
                 weights: List[int]):

        """ Initialize 0-1 Knapsack problem data """

        '''
            Without loss of generality one can assume that
            capacity, prices and weights are positive integers
        '''

        self.items: List[KnapsackItem] = []
        for price, weight in zip(prices, weights):
            if not is_positive_integer(price):
                raise AssertionError("price {} is not a positive integer".format(price))
            if not is_positive_integer(weight):
                raise AssertionError("weight {} is not a positive integer".format(weight))
            self.items.append(KnapsackItem(price, weight))

        # sort items in decreasing order of values of the profit per unit weight
        self.items = sorted(self.items, key=lambda item:  item.weight / item.price)

        # assert the assumption holds:
        if not is_positive_integer(capacity):
            raise AssertionError("capacity {} is not a positive integer".format(capacity))

        self.capacity = capacity
        self.number_of_items = len(self.items)
        self.prices = prices
        self.weights = weights


class KnapsackSolution:
    """ Class holding 0-1 Knapsack problem solution """
    counter_of_comparisons: int

    def __init__(self, number_of_items, knapsack_capacity):
        self.is_item_taken: List[bool] = [False] * number_of_items
        self.residual_capacity: int = knapsack_capacity
        self.level_index = 0
        self.weight = 0
        self.profit = 0
        self.counter_of_comparisons = 0

    def take_item(self, index, item):
        """
            Tries to insert the item and update the solution
        """
        if item.weight <= self.residual_capacity:
            self.is_item_taken[index] = True
            self.residual_capacity -= item.weight
            self.weight += item.weight
            self.profit += item.price
            return True
        else:
            return False

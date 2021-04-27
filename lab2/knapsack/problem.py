from typing import List


class KnapsackProblem:
    """ Class holding 0-1 Knapsack problem data """

    def __init__(self,
                 capacity: int,
                 prices: List[int],
                 weights: List[int]):

        """ Initialize 0-1 Knapsack problem data """
        if len(prices) != len(weights):
            raise AssertionError("len(prices) != len(weights)")

        '''
            Without loss of generality one can assume that
            capacity, prices and weights are positive integers
        '''

        def is_positive_integer(x):
            return x > 0 and isinstance(x, int)

        # assert the assumption holds:
        if not is_positive_integer(capacity):
            raise AssertionError("capacity {} is not a positive integer".format(capacity))

        if any(not is_positive_integer(x) for x in prices):
            raise AssertionError("prices are not positive integers")

        if any(not is_positive_integer(x) for x in weights):
            raise AssertionError("weights are not positive integers")

        self.capacity = capacity
        self.prices = prices
        self.weights = weights


class KnapsackSolution:
    """ Class holding 0-1 Knapsack problem solution """

    def __init__(self, number_of_items, knapsack_capacity):
        self.is_item_taken: List[bool] = [False] * number_of_items
        self.residual_capacity: int = knapsack_capacity
        self.last_inserted_index = 0
        self.weight = 0
        self.profit = 0

    def __len__(self):
        return len(self.is_item_taken)

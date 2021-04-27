from knapsack.problem import KnapsackProblem, KnapsackSolution, KnapsackItem
from knapsack.branch_and_bound import branch_and_bound


def bnb_unit_1():
    task = KnapsackProblem(capacity=50,
                           prices=[70, 20, 39, 37, 7, 5, 10],
                           weights=[31, 10, 20, 19, 4, 3, 6])

    solution = branch_and_bound(task)
    print(solution.profit)
    assert solution.profit == 107


def bnb_unit_2():
    task = KnapsackProblem(capacity=10,
                           prices=[40, 50, 100, 95, 30],
                           weights=[2, 3, 2, 5, 3])

    solution = branch_and_bound(task)
    print(solution.profit)


bnb_unit_2()

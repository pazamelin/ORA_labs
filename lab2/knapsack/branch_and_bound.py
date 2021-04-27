from problem import KnapsackProblem, KnapsackSolution

from queue import Queue
import warnings


def assert_is_solution_partial(problem, partial_solution):
    k = len(partial_solution)
    n = len(problem.weights)

    if k > n:
        raise AssertionError("partial solution is out of range")
    if k == n:
        warnings.warn("the solution is not partial")
        return partial_solution.profit


def profit_upper_bound(problem, partial_solution):
    """
        Find an upper bound on a partial solution by
        solving relaxation problem from it
    """
    assert_is_solution_partial(problem, partial_solution)

    k = len(partial_solution)
    profit = partial_solution.profit
    residual_capacity = partial_solution.residual_capacity

    for price, weight in zip(problem.prices[:k],
                             problem.weights[:k]):
        residual_capacity -= weight
        if residual_capacity > 0:
            # take the item
            profit += price
        else:
            # take as big part of the item as possible
            profit += price * (-residual_capacity / weight)
            break

    return profit


def horowitz_sahni_forward_move(problem, partial_solution):
    """
        A forward move consists of inserting the largest possible set
        of new consecutive items into the current solution
    """
    k = len(partial_solution)
    n = len(problem.weights)
    partial_solution.last_inserted_index = None
    next_index = None

    for i in range(k, n, 1):
        weight = problem.weights[i]
        price = problem.prices[i]

        if weight <= partial_solution.residual_capacity:
            partial_solution.residual_capacity -= weight
            partial_solution.profit += price
            partial_solution.is_item_taken.append(True)
            partial_solution.last_inserted = i
            next_index = i
        else:
            break

    return next_index


def horowitz_sahni_backtracking_move(problem, partial_solution, current_index):
    """
        A backtracking move consists of removing the last inserted item
        from the current solution
    """
    next_index = None

    backtrack_index = current_index - 1
    while backtrack_index > 0 and not partial_solution.is_item_taken[backtrack_index]:
        backtrack_index -= 1

    if partial_solution.is_item_taken[backtrack_index]:
        partial_solution.is_item_taken[backtrack_index] = 0
        partial_solution.profit -= problem.prices[backtrack_index]
        partial_solution.weight -= problem.weights[backtrack_index]
        partial_solution.residual_capacity += problem.weights[backtrack_index]

        next_index = backtrack_index + 1

    return next_index


def horowitz_sahni(problem):
    # Initialize
    best_solution = KnapsackSolution(problem.number_of_items,
                                     knapsack_capacity=problem.capacity)
    solutions_queue = Queue()
    solutions_queue.put(best_solution)

    while not solutions_queue.empty():
        current_solution = solutions_queue.get()




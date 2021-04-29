from knapsack.problem import KnapsackProblem, KnapsackSolution
from copy import deepcopy

from queue import Queue


def upper_bound(problem, partial_solution):
    """
        Find an upper bound on a partial solution by
        solving relaxation problem from it
    """
    k = partial_solution.level_index
    profit = partial_solution.profit
    residual_capacity = partial_solution.residual_capacity

    for item in problem.items:
        residual_capacity -= item.weight
        if residual_capacity >= 0:
            # take the item
            profit += item.price
        else:
            # take as big part of the item as possible
            profit += item.price * ((item.weight + residual_capacity) / item.weight)
            break

    return profit


def branch_and_bound(problem):
    best_solution = KnapsackSolution(problem.number_of_items,
                                     knapsack_capacity=problem.capacity)
    solutions_queue = Queue()
    solutions_queue.put(best_solution)

    while not solutions_queue.empty():
        current_solution = solutions_queue.get()
        # index of the last added (or not) element from [0, n] range
        index = current_solution.level_index

        if current_solution.profit > best_solution.profit:
            # update best solution if needed
            best_solution = deepcopy(current_solution)

        if index != problem.number_of_items:
            profit_upper_bound = upper_bound(problem, current_solution)
            if profit_upper_bound >= best_solution.profit:
                # if the partial solution can possibly result in a better solution

                # add (current solution + x_index as not taken) in the queue
                new_solution_lhs = deepcopy(current_solution)
                new_solution_lhs.level_index = index + 1
                solutions_queue.put(new_solution_lhs)

                # add (current solution + x_index as taken) in the queue
                new_solution_rhs = deepcopy(current_solution)
                has_inserted = new_solution_rhs.take_item(index, problem.items[index])
                if has_inserted:
                    new_solution_rhs.level_index = index + 1
                    solutions_queue.put(new_solution_rhs)

    return best_solution

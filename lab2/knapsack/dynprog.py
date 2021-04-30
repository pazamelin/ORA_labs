from knapsack.problem import KnapsackProblem, KnapsackSolution


def knapsack_dp(problem):
    solution = KnapsackSolution(problem.number_of_items, knapsack_capacity=problem.capacity)
    K = [[0 for x in range(problem.capacity + 1)] for x in range(problem.number_of_items + 1)]
    ans = [0 for x in range(problem.number_of_items)]
    counter = 0

    for i in range(problem.number_of_items + 1):
        for w in range(problem.capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif problem.weights[i-1] <= w:
                K[i][w] = max(problem.prices[i-1]
                              + K[i-1][w-problem.weights[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    findsubjects(problem.number_of_items, problem.capacity, K, problem.weights, ans, counter)

    for i in range(problem.number_of_items):
        if ans[i] == 1:
            solution.weight += problem.weights[i]
            solution.is_item_taken = True
    solution.profit = K[problem.number_of_items][problem.capacity]
    solution.residual_capacity -= solution.weight
    solution.counter_of_comparisons = counter

    return solution


def findsubjects(i, w, K, weights, ans, counter):
    if K[i][w] == 0:
        return

    if K[i - 1][w] == K[i][w]:
        findsubjects(i - 1, w, K, weights, ans)
        counter += 1
    else:
        ans[i - 1] = 1
        findsubjects(i - 1, w - weights[i - 1], K, weights, ans)
        counter += 1

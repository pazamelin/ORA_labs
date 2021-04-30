from knapsack.problem import KnapsackProblem, KnapsackSolution


def approx(problem):
    solution = KnapsackSolution(problem.number_of_items, knapsack_capacity=problem.capacity)
    T = {}
    ans = [0 for x in range(problem.number_of_items)]
    for i in range(problem.number_of_items):
        T[float(problem.weights[i])/float(problem.prices[i])] = i

    K = T.keys()
    K = sorted(K)

    price = 0
    weight = 0
    for i in K:
        if weight + problem.weights[T[i]] <= problem.capacity:
            weight += problem.weights[T[i]]
            price += problem.prices[T[i]]
            ans[T[i]] = 1
            solution.counter_of_comparisons += 1
        else:
            price_greedy = problem.prices[T[i]]
            solution.counter_of_comparisons += 1
            if price_greedy > price:
                solution.profit = price_greedy
                solution.weight = problem.weights[T[i]]
                solution.residual_capacity -= solution.weight
                ans = [0 for x in range(problem.number_of_items)]
                ans[T[i]] = 1
            else:
                solution.profit = price
                solution.weight = weight
                solution.residual_capacity -= solution.weight

    for i in range(problem.number_of_items):
        if ans[i] == 1:
            solution.is_item_taken = True

    return solution

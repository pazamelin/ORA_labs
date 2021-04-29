from knapsack.problem import KnapsackProblem, KnapsackSolution


def knapsack_greedy(W, wt, val, n):
    solution = KnapsackSolution(problem.number_of_items, knapsack_capacity=problem.capacity)
    T = {}
    for i in range(n):
        T[float(wt[i])/float(val[i])] = i

    K = T.keys()
    K = sorted(K)

    C_greedy=0
    W_greedy=0
    for i in K:
        if W_greedy + wt[T[i]] <= W:
            W_greedy = W_greedy + wt[T[i]]
            C_greedy = C_greedy + val[T[i]]
        else:
            C_max = val[T[i]]
            if C_max > C_greedy:
                solution.profit = C_max
                solution.weight = wt[T[i]]
                solution.residual_capacity -= solution.weight

    solution.profit = C_result

    return C_result
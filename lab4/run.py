from qap.problem import *

path = 'benchmarks/data/'
names = ['tai20a', 'tai40a', 'tai60a', 'tai80a', 'tai100a']

for name in names:
    problem = read_problem(path + name)
    print(problem.n)
    for line in problem.dists:
        print(line)
    print('')
    for line in problem.flows:
        print(line)
    print('')
    print('===============================================')
    print('')

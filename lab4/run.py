from qap.problem import *

path = 'benchmarks/data/'
names = ['tai20a', 'tai40a', 'tai60a', 'tai80a', 'tai100a']

for name in names:
    problem = read_problem(path + name)
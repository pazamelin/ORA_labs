from typing import List


class QAProblem:
    n: int
    dists: List[List[int]]
    flows: List[List[int]]

    def __init__(self, dists, flows):
        self.n = len(dists)
        self.dists = dists
        self.flows = flows


class QASolution:
    assignment: List[int]


def read_problem(filename):
    ifstream = open(filename, 'r')

    n = 0
    dists: List[List[int]] = []
    flows: List[List[int]] = []

    # read n
    line = ifstream.readline()
    line_split = line.split()
    n = int(line_split[0])

    # read distances
    for i in range(0, n, 1):
        line = ifstream.readline()
        line_split = line.split()
        map_object = map(int, line_split)
        dists.append(list(map_object))

    # discard the empty line
    ifstream.readline()

    # read flows
    for i in range(0, n, 1):
        line = ifstream.readline()
        line_split = line.split()
        map_object = map(int, line_split)
        flows.append(list(map_object))

    return QAProblem(dists, flows)

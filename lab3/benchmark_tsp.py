import copy

import tsp.genetic_tsp as gtsp

import pandas as pd
import time


def get(path_or_url):
    return pd.read_csv(path_or_url)


def put(dataframe, filename):
    dataframe.to_csv(filename, index=True)


path = 'benchmarks/tsp/data/'
files = ['a280.csv', 'att48.csv',  'ch150.csv', 'fl417.csv']
result = pd.DataFrame(columns=['benchmark', 'answer', 'time'])
repeats = 5

result_row = 0
for file in files:
    best_route = None
    total_time = 0.0
    print(file)
    for iteration in range(0, repeats, 1):
        dataframe = get(path + file)
        dataframe.columns = ['i', 'x', 'y']

        cities = []
        for index, row in dataframe.iterrows():
            cities.append(gtsp.City(row['x'], row['y']))

        start = time.time()

        best_route_i = gtsp.run(cities,
                                population_size=50,
                                selection_size=10,
                                mutation_rate=0.02,
                                iterations=20,
                                name=file[:-4])
        end = time.time()
        total_time += end - start
        if best_route is None or best_route_i.get_distance() < best_route.get_distance():
            best_route = copy.deepcopy(best_route_i)

    average_time = total_time / repeats
    result.loc[result_row] = [file[:-4], best_route.get_distance(), average_time]
    result_row += 1


put(result, "benchmarks/tsp/result.csv")
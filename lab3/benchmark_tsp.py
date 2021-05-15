import tsp.genetic_tsp as gtsp

import pandas as pd
import time


def get(path_or_url):
    return pd.read_csv(path_or_url)


def put(dataframe, filename):
    dataframe.to_csv(filename, index=True)


path = 'benchmarks/tsp/data/'
files = ['a280.csv']
result = pd.DataFrame(columns=['benchmark', 'answer', 'time'])

result_row = 0
for file in files:
    dataframe = get(path + file)
    dataframe.columns = ['i', 'x', 'y']

    cities = []
    for index, row in dataframe.iterrows():
        cities.append(gtsp.City(row['x'], row['y']))

    start = time.time()

    best_route = gtsp.run(cities,
                          population_size=50,
                          selection_size=10,
                          mutation_rate=0.05,
                          iterations=50,
                          name=file[:-4])

    end = time.time()

    result.loc[result_row] = [file[:-4], best_route.get_distance(), end - start]

put(result, "benchmarks/tsp/result.csv")
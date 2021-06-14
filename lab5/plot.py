import numpy as np
import random
from typing import List
import matplotlib.pyplot as plt

def plot_benchmarking_results(benchmarks, costs, optimums, png_filename):
    # plot
    xsize = 15
    ysize = 5
    max_xlabels = 50

    fig = plt.figure(figsize=(xsize, ysize))
    ax = plt.axes()
    ax.xaxis.set_major_locator(plt.MaxNLocator(max_xlabels))

    plt.xticks(rotation=90)
    plt.xlabel('benchmark')
    plt.ylabel('cost')
    plt.grid()

    plt.plot(benchmarks, costs, label='run result')
    plt.plot(benchmarks, optimums, label='optimal')
    plt.legend()

    plt.savefig('benchmarks/solutions/' + png_filename + '.png')
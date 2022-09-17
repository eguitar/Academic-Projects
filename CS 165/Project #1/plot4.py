# plotting of algorithms

import matplotlib.pyplot as plt

from benchmark import PermutationType, get_data_path

from collections import defaultdict
import csv
import numpy as np

def load_data(algorithm_name: str, permutation: PermutationType):
    path = get_data_path(permutation, algorithm_name)

    data = defaultdict(list)

    with path.open() as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            data[int(float(row[0]))].append(int(float(row[1])))
        
    return data

def load_avg_data(algorithm_name: str, permutation: PermutationType):
    data = load_data(algorithm_name, permutation)
    sizes, avg_times = list(), list()
    
    for size, elapsed_times in sorted(data.items()):

            sizes.append(size)
            avg_times.append(sum(elapsed_times) / len(elapsed_times))

    return sizes, avg_times

def add_to_plot(algorithm_name: str, permutation: PermutationType, k: int):
    sizes, avg_times = load_avg_data(algorithm_name, permutation)

    x, y = sizes, avg_times
    logx, logy = np.log(x), np.log(y)

    m, b = np.polyfit(logx[k:], logy[k:], 1)
    fit = np.poly1d((m, b))

    expected_y = fit(logx[k:])

    print(m, b, fit)

    p = plt.loglog(x,y, '.', base = 2, label = '_nolegend_')
    
    plt.loglog(x[k:], np.exp(expected_y), '--', base = 2,
        color = p[-1].get_color())

    return fit



if __name__ == '__main__':
    plt.figure(num = 1, figsize = (8,5),
        dpi = 150, facecolor = 'w', edgecolor = 'k')
    plt.title('Elapsed Time vs. Input Size (hybrid_sort - almost)')
    plt.xlabel('Input Size (n # elements)')
    plt.ylabel('Elapsed Time (nanoseconds)')

    fit1 = "hs1: " + str(add_to_plot('hybrid_sort1',PermutationType.ALMOST_SORTED,3))
    fit2 = "hs2: " + str(add_to_plot('hybrid_sort2',PermutationType.ALMOST_SORTED,3))
    fit3 = "hs3: " + str(add_to_plot('hybrid_sort3',PermutationType.ALMOST_SORTED,4))

    plt.legend([fit1,fit2,fit3])
    
    plt.show()



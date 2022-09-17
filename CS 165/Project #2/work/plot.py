# plotting of algorithms

from weakref import WeakSet
import matplotlib.pyplot as plt

from benchmark import get_data_path

from collections import defaultdict
import csv
import numpy as np

def load_data(algorithm_name: str):
    path = get_data_path(algorithm_name)

    data = defaultdict(list)

    with path.open() as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            data[float(row[0])].append(float(row[1]))
        
    return data

def load_avg_data(algorithm_name: str):
    data = load_data(algorithm_name)
    size_list, waste_list = list(), list()
    
    for size, waste in sorted(data.items()):
        # print(size)
        # print()
        # print(waste[0])
        # print()
        # print()
        size_list.append(size)
        waste_list.append(waste[0])

    return size_list, waste_list

def add_to_plot(algorithm_name: str):
    size, waste = load_avg_data(algorithm_name)

    x, y = size, waste
    logx, logy = np.log(x), np.log(y)

    m, b = np.polyfit(logx, logy, 1)
    fit = np.poly1d((m, b))

    expected_y = fit(logx)

    print(m, b, fit)

    p = plt.loglog(x,y, '.', base = 2, label = '_nolegend_')
    
    plt.loglog(x, np.exp(expected_y), '--', base = 2,
        color = p[-1].get_color())

    return fit



if __name__ == '__main__':
    plt.figure(num = 1, figsize = (8,5),
        dpi = 150, facecolor = 'w', edgecolor = 'k')
    plt.title('Waste vs. Input Size')
    plt.xlabel('Input Size (n # items)')
    plt.ylabel('Waste (units of space)')

    # fit1 = "nf: " + str(add_to_plot('next_fit'))
    # fit2 = "ff: " + str(add_to_plot('first_fit'))
    # fit3 = "bf: " + str(add_to_plot('best_fit'))
    fit = "ffd: " + str(add_to_plot('first_fit_decreasing'))
    # fit = "bfd: " + str(add_to_plot('best_fit_decreasing'))

    plt.legend([fit])
    # plt.legend([fit1,fit2,fit3])
    
    plt.show()



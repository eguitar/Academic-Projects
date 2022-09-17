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
    x_list, y_list = list(), list()
    
    for x, y in sorted(data.items()):
        x_list.append(x)
        y_list.append(y[0])

    return x_list, y_list

# def add_loglog_plot(algorithm_name: str):
#     x, y = load_avg_data(algorithm_name)
#     x, y = zip(*sorted(zip(x,y)))
#     logx, logy = np.log(x), np.log(y)

#     # m, b = np.polyfit(logx, logy, 1)
#     # fit = np.poly1d((m, b))

#     # expected_y = fit(logx)

#     # print(m, b, fit)

#     plt.loglog(logx, logy, '.-', base = 2, label = '_nolegend_')
    
#     # plt.loglog(x, np.exp(expected_y), '--', base = 2,
#     #     color = p[-1].get_color())

#     # return fit

def add_loglog_plot(algorithm_name: str):
    x, y = load_avg_data(algorithm_name)
    x, y = zip(*sorted(zip(x,y)))
    logx, logy = np.log(x), np.log(y)

    m, b = np.polyfit(logx, logy, 1)
    fit = np.poly1d((m, b))

    expected_y = fit(logx)

    print(m, b, fit)

    p = plt.loglog(x, y, '.', base = 2, label = '_nolegend_')
    
    plt.loglog(x, np.exp(expected_y), '--', base = 2,
        color = p[-1].get_color())
    return fit


def add_linlog_plot(algorithm_name: str):
    x, y = load_avg_data(algorithm_name)
    x, y = zip(*sorted(zip(x,y)))
    # plt.semilogy(x,y,'.-', label = '_nolegend_')
    plt.semilogy(x,y,'.', label = '_nolegend_')


# def add_linlog_plot(algorithm_name: str):
#     x, y = load_avg_data(algorithm_name)

#     x, y = zip(*sorted(zip(x,y)))

#     # x, y = size, waste
#     logy = np.log(y)

#     # m, b = np.polyfit(logx, logy, 1)
#     # fit = np.poly1d((m, b))

#     # expected_y = fit(logx)

#     # print(m, b, fit)

#     # p = plt.loglog(x,y, '.', base = 2, label = '_nolegend_')
    
#     # plt.loglog(x, np.exp(expected_y), '--', base = 2,
#     #     color = p[-1].get_color())


#     p = plt.semilogy(x,logy,'.', label = '_nolegend_')

#     # return fit
#     # return 0

def add_linlin_plot(algorithm_name: str):
    x, y = load_avg_data(algorithm_name)
    x, y = zip(*sorted(zip(x,y)))
    plt.plot(x,y,'.-', label = '_nolegend_')
    # plt.plot(x,y,'.-', label = '_nolegend_')



if __name__ == '__main__':
    plt.figure(num = 1, figsize = (8,5),
        dpi = 150, facecolor = 'w', edgecolor = 'k')
    
    
    # plt.title('Diameter vs Graph Size (Erdos-Renyi) - linlog')
    # plt.xlabel('Number of Vertices')
    # plt.ylabel('Diameter')

    # add_linlog_plot('er_diameter')

    # plt.title('Diameter vs Graph Size (Erdos-Renyi) - loglog')
    # plt.xlabel('Number of Vertices')
    # plt.ylabel('Diameter')

    # fit = "best fit: " + str(add_loglog_plot('er_diameter'))
    # plt.legend([fit])

    plt.title('Diameter vs Graph Size (Barabasi-Albert) - linlog')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Diameter')

    add_linlog_plot('ba_diameter')

    # plt.title('Diameter vs Graph Size (Barabasi-Albert) - loglog')
    # plt.xlabel('Number of Vertices')
    # plt.ylabel('Diameter')

    # fit = "best fit: " + str(add_loglog_plot('ba_diameter'))
    # plt.legend([fit])



    # plt.title('Cluster Coefficient vs Graph Size (Erdos-Renyi) - linlog')
    # plt.xlabel('Number of Vertices')
    # plt.ylabel('Clustering Coefficient')

    # add_linlog_plot('er_cluster')

    # plt.title('Cluster Coefficient vs Graph Size (Erdos-Renyi) - loglog')
    # plt.xlabel('Number of Vertices')
    # plt.ylabel('Clustering Coefficient')

    # fit = "best fit: " + str(add_loglog_plot('er_cluster'))
    # plt.legend([fit])
    

    # plt.title('Cluster Coefficient vs Graph Size (Barabasi-Albert) - linlog')
    # plt.xlabel('Number of Vertices')
    # plt.ylabel('Clustering Coefficient')

    # add_linlog_plot('ba_cluster')

    # plt.title('Cluster Coefficient vs Graph Size (Barabasi-Albert) - loglog')
    # plt.xlabel('Number of Vertices')
    # plt.ylabel('Clustering Coefficient')

    # fit = "best fit: " + str(add_loglog_plot('ba_cluster'))
    # plt.legend([fit])








    # ---------------------------------------------------------------------

    # plt.title('Degree Distribution (Erdos-Renyi | n = 1,000)')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # add_linlin_plot('er_degree1000')

    # plt.title('Degree Distribution (Erdos-Renyi | n = 10,000)')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # add_linlin_plot('er_degree10000')

    # plt.title('Degree Distribution (Erdos-Renyi | n = 100,000)')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # add_linlin_plot('er_degree100000')

    # ---------------------------------------------------------------------

    # plt.title('Degree Distribution (Erdos-Renyi | n = 1,000) - loglog')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # add_loglog_plot('er_degree1000')

    # plt.title('Degree Distribution (Erdos-Renyi | n = 10,000) - loglog')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # add_loglog_plot('er_degree10000')

    # plt.title('Degree Distribution (Erdos-Renyi | n = 100,000) - loglog')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # add_loglog_plot('er_degree100000')


    # DEGREE BA LIN
    # ---------------------------------------------------------------------

    # plt.title('Degree Distribution (Barabasi-Albert | n = 1,000)')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # add_linlin_plot('ba_degree1000')

    # plt.title('Degree Distribution (Barabasi-Albert | n = 10,000)')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # add_linlin_plot('ba_degree10000')

    # plt.title('Degree Distribution (Barabasi-Albert | n = 100,000)')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # add_linlin_plot('ba_degree100000')

    # DEGREE BA LOG
    # ---------------------------------------------------------------------

    # plt.title('Degree Distribution (Barabasi-Albert | n = 1,000) - loglog')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # fit = "best fit: " + str(add_loglog_plot('ba_degree1000'))
    # plt.legend([fit])

    # plt.title('Degree Distribution (Barabasi-Albert | n = 10,000) - loglog')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # fit = "best fit: " + str(add_loglog_plot('ba_degree10000'))
    # plt.legend([fit])

    # plt.title('Degree Distribution (Barabasi-Albert | n = 100,000) - loglog')
    # plt.xlabel('Degree')
    # plt.ylabel('Frequency')

    # fit = "best fit: " + str(add_loglog_plot('ba_degree100000'))
    # plt.legend([fit])
    
    plt.show()



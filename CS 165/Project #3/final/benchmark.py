# benchmarks algorithms
from graph import *
import csv
from pathlib import Path

DATA_DIRECTORY = Path('data')


def get_data_path(algorithm_name: str):
    directory = DATA_DIRECTORY
    directory.mkdir(parents = True, exist_ok = True)
    return (directory / algorithm_name).with_suffix('.csv')


def save_data(algorithm_name: str, size: int, waste: int):
    path = get_data_path(algorithm_name)
    with path.open('a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([size, waste])


if __name__ == '__main__':
    
    for n in range(1000,500000,5000):
        print(f"---------{n}")

        # er_d = 0
        # ba_d = 0


        # for p in range(5):

        edges = generate_er_graph(n)
        size = len(edges)
        er_g = Graph(size,edges)

        edges = generate_ba_graph(n)
        size = len(edges)
        ba_g = Graph(size,edges)

        er_d = er_g.get_diameter()
        ba_d = ba_g.get_diameter()

        # er_d = int(er_d / 5)
        # ba_d = int(ba_d / 5)

        # save_data('er_cluster',n,er_g.get_cluster())

        # save_data('ba_cluster',n,ba_g.get_cluster())

        save_data('er_diameter',n,er_d)

        save_data('ba_diameter',n,ba_d)



    # for i in range(10):
    #     for n in [1000, 10000, 100000]:
    #         print(f"---------{n}")

    #         edges = generate_er_graph(n)
    #         size = len(edges)
    #         g = Graph(size,edges)

    #         x = g.get_degree()

    #         for j in x:
    #             save_data('er_degree'+str(n),j,x[j])

    #         edges = generate_ba_graph(n)
    #         size = len(edges)
    #         g = Graph(size,edges)

    #         x = g.get_degree()

    #         for j in x:
    #             save_data('ba_degree'+str(n),j,x[j])
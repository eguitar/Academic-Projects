# benchmarks algorithms

import argparse

import requirements
import random
import csv
import math
from pathlib import Path
from CFloat import CFloat

DATA_DIRECTORY = Path('data')

ALGORITHMS = {
    'next_fit': requirements.next_fit,
    'first_fit': requirements.first_fit,
    'first_fit_decreasing': requirements.first_fit_decreasing,
    'best_fit': requirements.best_fit,
    'best_fit_decreasing': requirements.best_fit_decreasing,
}


def generate_list(size: int) -> list[CFloat]:
    nums = []
    for i in range(size):
        nums.append(random.uniform(0.0, 0.6))
    return nums


def benchmark(nums: list[int], algorithm: 'function') -> int:
    free_space = []
    assignment = [0] * len(nums)
    algorithm(nums, assignment, free_space)
    waste = sum(free_space)

    return (len(nums), waste)


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
    
    for i in [100,250,500,750,1000,2500,5000,7500,10000,25000,50000,75000,100000,250000,500000]:
        print(f"INPUT SIZE : --------------- {i}\n")

        nf_waste = 0
        ff_waste = 0
        ffd_waste = 0
        bf_waste = 0
        bfd_waste = 0

        for j in range(5):
            nums = generate_list(i)

            nf_waste = nf_waste + benchmark(nums, ALGORITHMS['next_fit'])[1]
            ff_waste = ff_waste + benchmark(nums, ALGORITHMS['first_fit'])[1]
            ffd_waste = ffd_waste + benchmark(nums, ALGORITHMS['first_fit_decreasing'])[1]
            bf_waste = bf_waste + benchmark(nums, ALGORITHMS['best_fit'])[1]
            bfd_waste = bfd_waste + benchmark(nums, ALGORITHMS['best_fit_decreasing'])[1]

        nf_waste = nf_waste / 5
        ff_waste = ff_waste / 5
        ffd_waste = ffd_waste / 5
        bf_waste = bf_waste / 5
        bfd_waste = bfd_waste / 5

        save_data('next_fit', i, nf_waste)
        save_data('first_fit', i, ff_waste)
        save_data('first_fit_decreasing', i, ffd_waste)
        save_data('best_fit', i, bf_waste)
        save_data('best_fit_decreasing', i, bfd_waste)
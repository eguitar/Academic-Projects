# benchmarks algorithms

import argparse

from enum import Enum

import requirements
import random
import time
import csv
import math
from pathlib import Path

DATA_DIRECTORY = Path('data')

class PermutationType(Enum):
    UNIFORMLY_DISTRIBUTED = 'random'
    REVERSE_SORTED = 'reverse'
    ALMOST_SORTED = 'almost_sorted'

SORTING_ALGORITHMS = {
    'insertion_sort': requirements.insertion_sort,
    'merge_sort': requirements.merge_sort,
    'shell_sort1': requirements.shell_sort1,
    'shell_sort2': requirements.shell_sort2,
    'shell_sort3': requirements.shell_sort3,
    'shell_sort4': requirements.shell_sort4,
    'hybrid_sort1': requirements.hybrid_sort1,
    'hybrid_sort2': requirements.hybrid_sort2,
    'hybrid_sort3': requirements.hybrid_sort3
    }

parser = argparse.ArgumentParser(
    description = 'Benchmark several algorithms.')


parser.add_argument('--permutation',
    choices = [e.value for e in PermutationType],
    help = 'the input permutation to use', default = 'random')

# parser.add_argument('--algorithm', dest = 'algorithm_name',
#     choices = SORTING_ALGORITHMS.keys(),
#     help = 'the sorting algorithm to use', required = True)

args = parser.parse_args()
args.permutation = PermutationType(args.permutation)
# args.algorithm = SORTING_ALGORITHMS[args.algorithm_name]

# print(args.permutation)
# print(args.algorithm)

def get_data_path(permutation: PermutationType, algorithm_name: str):
    directory = DATA_DIRECTORY / algorithm_name
    directory.mkdir(parents = True, exist_ok = True)
    return (directory / permutation.value).with_suffix('.csv')

def generate_list(permutation: PermutationType, size: int) -> list[int]:
    nums = list(range(size))
    
    match permutation:
        case PermutationType.UNIFORMLY_DISTRIBUTED:
            random.shuffle(nums)
        case PermutationType.REVERSE_SORTED:
            nums.reverse()
        case PermutationType.ALMOST_SORTED:
            n = 2 * int(math.log(size))
            for i in range(n):
                a = random.randrange(size)
                b = random.randrange(size)
                nums[a],nums[b] = nums[b],nums[a]
        

    return nums


def benchmark(nums: list[int], algorithm: 'function') -> int:
    start_time = time.process_time_ns()
    algorithm(nums)
    end_time = time.process_time_ns()

    return end_time - start_time


# def save_data(permutation: PermutationType, algorithm_name: str, size: int, elapsed_time: int):
#     path = get_data_path(permutation, algorithm_name)
#     field = ('Size', 'Runtime')
#     with path.open('a') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow([size, elapsed_time])


if __name__ == '__main__':
    # size_list = [500,750,1000,2500,5000,7500,10000,25000,50000,75000,100000] # for insertion and merge
    size_list = [500,750,1000,2500,5000,7500,10000,25000,50000,75000] # for shell and hybrid

    
    
    
    # -------------------------------------------------------------------------------
    path = get_data_path(args.permutation, "shell_sort1")

    with open(path,'a',newline='') as csvfile:
        wr = csv.writer(csvfile)
        
        for s in size_list:
            sum = 0
            nums = generate_list(args.permutation, s)
            for i in range(3):
                sum = sum + benchmark(nums, requirements.shell_sort1)
                elapsed_time = sum / 5
            wr.writerow([s, elapsed_time])
            print(elapsed_time)
            print("\n")

        csvfile.close()

    # -------------------------------------------------------------------------------
    # path = get_data_path(args.permutation, "shell_sort2")

    # with open(path,'a',newline='') as csvfile:
    #     wr = csv.writer(csvfile)
        
    #     for s in size_list:
    #         sum = 0
    #         nums = generate_list(args.permutation, s)
    #         for i in range(3):
    #             sum = sum + benchmark(nums, requirements.shell_sort2)
    #             elapsed_time = sum / 5
    #         wr.writerow([s, elapsed_time])
    #         print(elapsed_time)
    #         print("\n")

    #     csvfile.close()

    # # -------------------------------------------------------------------------------
    # path = get_data_path(args.permutation, "shell_sort3")

    # with open(path,'a',newline='') as csvfile:
    #     wr = csv.writer(csvfile)
        
    #     for s in size_list:
    #         sum = 0
    #         nums = generate_list(args.permutation, s)
    #         for i in range(3):
    #             sum = sum + benchmark(nums, requirements.shell_sort3)
    #             elapsed_time = sum / 5
    #         wr.writerow([s, elapsed_time])
    #         print(elapsed_time)
    #         print("\n")

    #     csvfile.close()

    # # -------------------------------------------------------------------------------
    # path = get_data_path(args.permutation, "shell_sort4")

    # with open(path,'a',newline='') as csvfile:
    #     wr = csv.writer(csvfile)
        
    #     for s in size_list:
    #         sum = 0
    #         nums = generate_list(args.permutation, s)
    #         for i in range(3):
    #             sum = sum + benchmark(nums, requirements.shell_sort4)
    #             elapsed_time = sum / 5
    #         wr.writerow([s, elapsed_time])
    #         print(elapsed_time)
    #         print("\n")

    #     csvfile.close()
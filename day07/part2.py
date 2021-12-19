import numpy as np

input_file = r'D:\PycharmProjects\advent_of_code\day07\input.csv'

with open(input_file, 'r+') as file:
    read_file = file.readline()

input = read_file.split(',')
input_int = [int(i) for i in input]

# arr_sort = np.array(sorted([16,1,2,0,4,2,7,1,2,14]))
arr_sort = np.array(sorted(input_int), dtype=np.int)
mean = int(np.round(np.mean(arr_sort), 0))
abs_diff = (np.abs(arr_sort - mean))

sums_of_fuel = np.array(list(map(lambda x: sum(np.array(range(1, x + 1))), abs_diff)))
result = np.sum(sums_of_fuel)

print(f'Minimum moves is {result}.')

import numpy as np

input_file = r'D:\PycharmProjects\advent_of_code\day07\input.csv'

with open(input_file, 'r+') as file:
    # asss = file.readlines()
    read_file = file.readline()

input = read_file.split(',')
input_int = [int(i) for i in input]

# arr_sort = np.array(sorted([16,1,2,0,4,2,7,1,2,14]))

arr_sort = np.array(sorted(input_int), dtype=np.int)
meadian = np.median(arr_sort)
result = np.sum(np.abs(arr_sort - meadian), dtype=np.int)

print(f'Minimum moves is {result}.')

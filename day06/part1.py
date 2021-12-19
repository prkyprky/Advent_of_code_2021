import numpy as np

input_file = r'D:\PycharmProjects\advent_of_code\day06\input.csv'

with open(input_file, 'r') as file:
    read_file = file.readline()

input = read_file.split(',')
input_int = [int(i) for i in input]
input_arr = np.array(input_int)

# input_arr = np.array([3,4,3,1,2], dtype=np.int8)

# prvni den
odecteno = input_arr - 1
count_of_zero = np.count_nonzero(odecteno == 0)

# ostatni dny
for n in range(79):
    odecteno = odecteno - 1
    odecteno = np.append(odecteno, np.array([8] * count_of_zero, dtype=np.int8))
    odecteno = np.where(odecteno == -1, 6, odecteno)
    count_of_zero = np.count_nonzero(odecteno == 0)
    print(f'Day {1 + n}')
    print(len(odecteno))

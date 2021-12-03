# part 1


def get_value_from_list(list_of_moves):
    map_val = map(lambda x: int(x.split(' ')[-1]), list_of_moves)
    return sum(list(map_val))


def get_value_from_string(string):
    return int(string.split(' ')[-1])


movements = ['forward 9','down 9','up 4','down 5','down 6','up 6','down 7','down 1','forward 6','down 4','forward 8','up 5','forward 9','down 1','down 4','up 4','up 5','up 4','down 1','forward 8','down 1','forward 2','forward 8','down 9','forward 2','down 6','down 2','up 8','down 6','forward 9','forward 7','down 6','forward 3','down 2','forward 4','down 5','up 2','down 9','down 8','up 5','forward 5','forward 4','up 9','forward 9','down 8','forward 8','forward 2','up 8','down 7','forward 8','down 3','forward 6','up 9','forward 9','forward 4','forward 9','forward 6','down 4','up 2','forward 4','up 5','up 6','forward 9','down 3','forward 4','forward 9','down 1','forward 1','up 6','up 4','forward 7','up 7','up 3','forward 2','forward 8','forward 6','down 4','forward 2','forward 3','down 7','down 5','down 8','down 5','forward 1','down 8','down 2','down 8','down 3','forward 4','forward 8','forward 9','down 1','forward 8','down 1','down 6','down 7','down 7','forward 5','forward 3','down 2','down 1','forward 2','forward 1','down 6','down 4','up 5','up 9','down 4','forward 9','down 2','down 5','down 4','down 2','forward 2','forward 4','forward 6','forward 6','forward 3','down 6','up 5','forward 8','forward 3','down 9','down 3','forward 4','forward 2','down 9','down 8','down 7','down 3','forward 2','down 7','down 3','down 5','forward 6','up 9','up 8','forward 5','down 6','down 1','down 6','down 5','forward 7','down 2','forward 8','forward 7','forward 2','forward 8','up 6','forward 5','down 2','down 5','up 8','up 6','forward 1','down 4','up 5','up 5','up 5','forward 4','up 1','forward 3','down 9','down 6','up 1','forward 1','forward 2','forward 1','forward 4','forward 6','forward 6','up 7','down 7','down 7','down 9','forward 9','down 1','down 5','down 1','down 7','down 1','up 6','forward 2','down 4','up 3','up 2','forward 6','up 4','down 1','down 5','forward 9','up 4','up 3','forward 3','up 7','forward 2','forward 5','down 9','forward 7','forward 4','down 1','up 2','forward 4','up 4','down 2','forward 4','up 5','up 1','down 9','down 3','up 6','forward 7','up 7','forward 2','down 4','up 3','up 3','forward 4','up 5','down 3','up 8','forward 6','forward 8','down 1','down 9','down 7','forward 7','forward 5','forward 2','up 9','forward 3','forward 1','down 7','down 6','forward 5','up 3','forward 6','down 4','forward 9','down 7','forward 9','down 9','down 5','down 6','down 2','down 2','down 8','down 3','down 9','forward 5','up 6','forward 1','down 3','down 2','up 1','up 6','forward 3','down 6','down 6','up 9','up 8','forward 2','down 7','forward 5','up 9','down 7','down 3','forward 2','forward 2','up 9','forward 1','forward 7','down 9','forward 6','forward 7','up 8','down 7','down 5','down 3','up 6','down 5','forward 6','down 9','down 6','up 9','down 7','forward 2','down 5','up 4','down 4','down 8','forward 7','down 9','forward 8','forward 6','down 7','down 1','forward 5','up 6','forward 4','up 7','up 4','up 5','forward 9','forward 5','forward 4','down 6','down 5','forward 2','forward 7','down 8','forward 3','up 5','down 2','up 3','forward 4','up 5','up 2','forward 4','forward 1','forward 1','forward 4','forward 4','down 2','forward 1','forward 1','up 5','up 7','down 8','down 4','forward 2','forward 2','down 3','forward 7','down 8','up 3','forward 2','down 2','forward 3','up 2','forward 3','up 6','down 7','up 7','down 3','up 9','forward 3','forward 7','down 7','up 9','down 6','down 2','forward 8','forward 8','up 7','down 6','forward 2','forward 1','down 4','up 2','forward 6','up 7','down 5','up 1','forward 3','forward 9','up 4','forward 5','forward 8','down 3','up 5','forward 9','down 6','up 9','forward 5','down 4','down 1','down 6','up 9','up 2','forward 5','down 1','up 3','down 5','forward 2','down 4','forward 5','down 6','down 4','down 4','forward 1','down 7','down 2','forward 4','forward 5','up 9','down 6','down 2','forward 7','up 8','down 9','forward 7','down 5','down 2','down 8','down 8','up 4','up 3','down 3','down 7','forward 4','forward 6','down 4','up 7','forward 4','forward 4','forward 1','down 3','down 2','forward 7','forward 2','up 9','down 7','up 7','forward 2','forward 6','forward 9','down 3','forward 7','forward 5','up 5','up 1','forward 6','forward 4','down 2','forward 3','forward 9','down 1','forward 6','forward 7','forward 1','up 7','up 4','forward 7','forward 8','down 7','down 8','down 9','forward 7','down 9','up 6','down 7','up 3','down 7','forward 4','forward 9','forward 1','down 4','forward 1','up 4','up 4','forward 9','forward 8','up 4','down 2','forward 4','forward 2','forward 8','down 2','up 6','down 4','forward 6','forward 5','down 2','forward 9','down 5','forward 5','down 3','down 2','up 9','down 3','forward 6','forward 6','up 9','down 1','forward 4','up 3','forward 1','forward 3','forward 3','down 6','down 2','forward 8','down 4','forward 8','forward 8','forward 5','up 6','forward 3','down 1','down 8','forward 3','forward 4','down 2','down 7','up 8','forward 3','forward 8','up 2','forward 6','down 4','forward 9','forward 5','down 1','forward 6','forward 2','down 3','up 4','down 7','down 2','up 2','forward 7','down 6','down 2','up 5','up 5','down 9','down 7','down 3','down 1','down 9','forward 4','down 4','forward 7','forward 8','forward 4','up 6','forward 6','forward 9','down 2','forward 4','down 8','down 4','forward 5','forward 2','up 4','down 3','up 8','up 1','down 1','forward 9','up 3','up 1','forward 1','forward 7','forward 1','down 7','forward 7','forward 7','down 7','forward 4','up 6','forward 3','down 1','up 1','up 8','forward 5','forward 2','up 4','forward 7','down 2','down 3','down 8','up 7','up 5','forward 8','down 5','down 3','down 9','forward 6','forward 4','down 9','up 5','forward 3','up 7','up 9','up 1','forward 1','forward 3','forward 1','up 8','up 4','down 1','down 8','down 3','down 1','down 1','down 9','forward 4','down 3','forward 9','forward 2','down 1','forward 9','up 7','forward 6','up 4','forward 8','forward 3','down 2','down 2','down 2','up 5','forward 1','up 1','forward 7','down 1','forward 1','down 8','up 4','up 1','forward 7','down 8','down 9','forward 2','forward 1','up 3','forward 4','up 8','forward 5','down 2','forward 6','forward 8','up 9','forward 2','down 7','down 4','up 3','forward 1','forward 6','forward 9','down 1','down 8','down 1','down 2','forward 3','forward 9','forward 2','forward 4','forward 7','forward 3','up 8','up 9','forward 3','forward 6','down 5','up 6','down 8','forward 5','up 4','up 9','forward 6','forward 3','up 9','forward 8','forward 5','forward 9','forward 7','up 6','forward 3','forward 1','up 4','forward 9','forward 8','up 1','up 2','down 3','down 4','down 9','down 4','down 5','down 6','down 2','down 5','forward 6','forward 4','up 2','up 7','down 5','down 9','forward 3','down 5','forward 6','down 7','forward 1','forward 7','forward 9','forward 7','forward 4','forward 4','up 1','up 4','down 6','up 2','up 1','down 4','forward 2','down 4','forward 6','down 3','up 6','down 2','up 3','forward 1','forward 9','forward 3','up 9','forward 7','forward 5','forward 4','down 5','down 9','forward 6','forward 7','up 1','forward 7','forward 2','forward 2','forward 5','forward 6','down 3','down 7','down 3','down 4','down 6','down 1','forward 2','down 8','forward 4','forward 7','up 1','down 4','down 1','down 2','down 3','up 3','forward 9','forward 2','down 8','up 3','forward 8','forward 7','up 8','down 8','forward 2','down 9','down 9','down 5','forward 1','forward 3','forward 6','up 1','up 2','forward 1','down 3','up 6','forward 2','forward 8','forward 2','down 3','forward 8','forward 9','down 7','down 3','down 2','down 9','down 3','up 6','forward 9','forward 5','forward 1','forward 9','down 9','up 2','down 1','up 6','forward 6','down 3','forward 6','forward 3','forward 5','forward 4','up 2','up 4','up 6','forward 1','forward 6','up 6','up 4','up 7','down 8','down 5','up 1','up 1','down 5','forward 5','down 9','forward 8','down 3','up 4','down 9','down 1','forward 2','forward 9','down 3','down 8','down 5','down 6','forward 7','forward 1','down 9','down 7','forward 8','forward 2','up 1','up 1','forward 7','up 1','forward 2','down 9','up 4','forward 5','down 1','up 1','down 8','down 3','up 1','down 8','down 7','down 2','forward 9','down 5','forward 2','up 2','up 6','up 4','forward 6','up 5','forward 5','forward 4','forward 8','down 8','down 6','down 1','down 3','down 6','forward 8','up 1','up 5','down 4','forward 4','down 9','forward 4','up 6','down 7','forward 4','down 3','down 4','forward 1','forward 3','down 1','down 7','up 8','down 3','down 4','down 3','forward 3','down 8','forward 8','down 3','down 7','forward 2','up 2','forward 7','down 9','up 7','forward 5','down 2','down 5','up 4','up 8','forward 8','forward 9','forward 8','down 8','forward 6','forward 9','forward 6','forward 8','forward 6','forward 8','forward 2','down 7','down 3','forward 7','down 4','down 5','up 1','forward 5','down 3','down 7','up 4','forward 9','down 2','down 3','forward 1','up 6','down 1','down 9','forward 8','forward 9','forward 2','down 6','down 4','up 3','up 8','forward 1','down 3','up 8','up 7','down 4','up 3','down 7','down 2','down 5','down 7','down 2','forward 2','down 3','up 2','forward 8','up 1','forward 2','up 4','forward 1','forward 8','forward 6','forward 2','down 2','forward 5','up 4','down 9','down 7','forward 2','down 9','down 9','forward 6','down 8','down 4','down 7','down 9','forward 7','forward 7','up 6','forward 3','forward 5','forward 6','down 8','up 1','forward 2','up 4','up 2','down 8','down 9','down 1','down 3','forward 7','forward 5','forward 6','up 6','down 7','up 8','up 1','forward 8','down 5','up 1','down 2','down 5','forward 6','down 4','forward 5','down 4','forward 3','down 5','up 4','up 7','forward 2','up 2','down 8','forward 6']

forward = []
down = []
up = []

for item in movements:
    if item.startswith('f'):
        forward.append(item)
    elif item.startswith('d'):
        down.append(item)
    elif item.startswith('u'):
        up.append(item)
    else:
        print(f'Unrecognized value: {item}')

moves = {'forward': forward,
         'down': down,
         'up': up
         }

results = {}
for n in moves.keys():
    res = get_value_from_list(moves[n])
    results[n] = res
    print(f'{n}: {res}')

depth = results['down'] - results['up']

print(f'Final value is: {depth * results["forward"]}')

# part 2

forward = 0
aim = 0
depth = 0

for item in movements:
    move_value = get_value_from_string(item)
    if item.startswith('f'):
        forward += move_value
        if aim != 0 or depth != 0:
            tmp_depth = aim * move_value
            depth += tmp_depth
    elif item.startswith('d'):
        aim += move_value
    elif item.startswith('u'):
        aim -= move_value
    else:
        print(f'Unrecognized value: {item}')

print(f'Final forward is {forward}')
print(f'Final depth is {depth}')
print(f'Requested value is {forward * depth}')

import math,re

def part1():
    with open('input') as f:
        steps = [x for x in f.readline().strip()]
        maps = f.read().strip('\n\n').split('\n')
        maps = [re.findall(r'\w{3}+', x) for x in maps]
        dict = {}
        for src, left, right in maps:
            dict[src] = (left,right)
        print(count_steps(steps, dict, 'AAA'))

def part2():
    with open('input') as f:
        steps = [x for x in f.readline().strip()]
        maps = f.read().strip('\n\n').split('\n')
        maps = [re.findall(r'\w{3}+', x) for x in maps]
        dict = {}
        for src, left, right in maps:
            dict[src] = (left,right)
        pos = [x for x in dict.keys() if x.endswith('A')]
        count = [count_steps(steps, dict, p) for p in pos]
        print(math.lcm(*count))

def count_steps(steps, dict, pos):
    count = 0
    while not pos.endswith('Z'):
        for step in steps:
            count += 1
            if step == 'L':
                pos = dict[pos][0]
            else:
                pos = dict[pos][1]
    return count

part1()
part2()
from functools import lru_cache
from typing import Tuple

def part1():
    total = 0
    with open('input') as f:
        for line in f:
            input, clue = line.strip().split()
            damaged = tuple([int(x) for x in clue.split(',')])

            arrangements = 0
            arrangements += solver(input, damaged)
            total += arrangements
        print(total)

def part2():
    total = 0
    with open('input') as f:
        for line in f:
            input, clue = line.strip().split()
            damaged = tuple([int(x) for x in clue.split(',')])

            input = '?'.join([input] * 5)
            damaged = damaged * 5

            arrangements = 0
            arrangements += solver(input, damaged)
            total += arrangements
        print(total)

@lru_cache
def solver(input: str, damaged: Tuple[int]):
    if len(input) == 0:
        return 1 if len(damaged) == 0 else 0
    if input.startswith('.'):
        return process_working(input, damaged)
    if input.startswith('?'):
        return process_unknown(input, damaged)
    if input.startswith('#'):
        return process_broken(input, damaged)

def process_working(input: str, damaged: Tuple[int]):
    return solver(input[1:], damaged)

def process_unknown(input: str, damaged: Tuple[int]):
    rest = input[1:]
    return solver('.' + rest, damaged) + solver('#' + rest, damaged)

def process_broken(input: str, damaged: Tuple[int]):
    if len(damaged) == 0:
        return 0
    if len(input) < damaged[0]:
        return 0
    if '.' in input[0:damaged[0]]:
        return 0
    if len(damaged) > 1:
        if len(input) < damaged[0] + 1 or input[damaged[0]] == '#':
            return 0
        return solver(input[damaged[0] + 1:], damaged[1:])
    else:
        return solver(input[damaged[0]:], damaged[1:])

part1()
part2()
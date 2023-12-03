import re

def part1():
    numbers = list()
    symbols = list()

    with open('input', 'r') as f:
        row = 0
        for line in f:
            nums = [(m.group(), (m.start(), row)) for m in re.finditer(r'\d+', line)]
            syms = [(m.start(), row) for m in re.finditer(r'[^0-9.\n]', line)]
            row += 1
            if len(nums) > 0:
                numbers.extend(nums)
            if len(syms) > 0:
                symbols.extend(syms)
        adjacent_nums = [num for num in numbers if is_adjacent(num, symbols)]
        total = sum([int(n) for (n,_) in adjacent_nums if len(n) > 0])
        print(total)

def is_adjacent(number, symbols):
    num, coords = number
    x, y = coords
    for u, v in symbols:
        for l in range(len(num)):
            if (x+l,y) == (u-1,v-1) or (x+l,y) == (u,v-1) or (x+l,y) == (u+1,v-1):
                return True
            if (x+l,y) == (u-1, v) or (x+l,y) == (u+1,v):
                return True
            if (x+l,y) == (u-1,v+1) or (x+l,y) == (u,v+1) or (x+l,y) == (u+1,v+1):
                return True
    return False

def get_adjacent_gear(number, symbols):
    num, coords = number
    x, y = coords
    out = []
    for u, v in symbols:
        for l in range(len(num)):
            if (x+l,y) == (u-1,v-1) or (x+l,y) == (u,v-1) or (x+l,y) == (u+1,v-1):
                out.append(((u,v), num))
                break
            if (x+l,y) == (u-1, v) or (x+l,y) == (u+1,v):
                out.append(((u,v), num))
                break
            if (x+l,y) == (u-1,v+1) or (x+l,y) == (u,v+1) or (x+l,y) == (u+1,v+1):
                out.append(((u,v), num))
                break
    return out

def part2():
    numbers = list()
    symbols = list()

    with open('input', 'r') as f:
        row = 0
        for line in f:
            nums = [(m.group(), (m.start(), row)) for m in re.finditer(r'\d+', line)]
            syms = [(m.start(), row) for m in re.finditer(r'\*', line)]
            row += 1
            if len(nums) > 0:
                numbers.extend(nums)
            if len(syms) > 0:
                symbols.extend(syms)
        
        adjacent_gears = {}
        for num in numbers:
            adjacent_coords = get_adjacent_gear(num, symbols)
            for (coord, num) in adjacent_coords:
                adjacent_gears.setdefault(coord, set()).add(int(num))

        paired_gears = {key:value for key, value in adjacent_gears.items() if len(value) == 2}

        print(sum(value.pop() * value.pop() for value in paired_gears.values()))

part1()
part2()
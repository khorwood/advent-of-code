def part1():
    height = 0
    rocks = []
    cubes = set()

    with open('input') as f:
        lines = f.read().strip().split('\n')
        height = len(lines)
        for y in range(height):
            line = lines[y].strip()
            for x in range(len(line)):
                c = line[x]
                if c == 'O':
                    rocks.append((x, y))
                elif c == '#':
                    cubes.add((x, y))
        tilt(rocks, cubes, height, (0, -1))
        load = calc_load(rocks, height)
        print(load)

def part2():
    height = 0
    rocks = []
    cubes = set()

    cache = {}
    with open('input') as f:
        lines = f.read().strip().split('\n')
        height = len(lines)
        for y in range(height):
            line = lines[y].strip()
            for x in range(len(line)):
                c = line[x]
                if c == 'O':
                    rocks.append((x, y))
                elif c == '#':
                    cubes.add((x, y))

        i = 0
        while i < 1_000_000_000:
            i += 1
            tilt(rocks, cubes, height, (0, -1))
            tilt(rocks, cubes, height, (-1, 0))
            tilt(rocks, cubes, height, (0, 1))
            tilt(rocks, cubes, height, (1, 0))
            board = get_board(rocks, cubes, height)
            if board in cache:
                cycle = i - cache[board]
                amount = (1_000_000_000 - i) // cycle
                i += amount * cycle
                print(cycle, amount, i)
            cache[board] = i

        load = calc_load(rocks, height)
        print(load)

def tilt(rocks, cubes, height, direction):

    def move(coords, direction=direction):
        x, y = coords
        dx, dy = direction

        if dx == 0:
            ny = y + dy
            if (x, ny) in cubes:
                return (x, y)
            if ny < 0:
                return (x, y)
            if ny >= height:
                return (x, y)
            if (x, ny) in rocks:
                return (x, y)
            return (x, ny)
        
        if dy == 0:
            nx = x + dx
            if (nx, y) in cubes:
                return (x, y)
            if nx < 0:
                return (x, y)
            if nx >= height:
                return (x, y)
            if (nx, y) in rocks:
                return (x, y)
            return (nx, y)
    
    moved = True
    while moved:
        moved = False
        for i in range(len(rocks)):
            pos = move(rocks[i], direction)
            if pos == rocks[i]:
                continue
            rocks[i] = pos
            moved = True

def get_board(rocks, cubes, height):
    lines = ''
    for y in range(height):
        line = ''
        for x in range(height):
            char = '.'
            if (x, y) in cubes:
                char = '#'
            if (x, y) in rocks:
                char = 'O'
            line += char
        lines += line + '\n'
    return lines

def calc_load(rocks, height):
    load = 0
    for rock in rocks:
        _, y = rock
        load += height - y
    return load

part1()
part2()
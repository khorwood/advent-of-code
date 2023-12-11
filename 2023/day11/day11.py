def part1():
    data = open('input').read().strip().split('\n')
    expanded = expand(data, 2)
    distance = shortest_paths_distance(expanded)
    print(distance)

def part2():
    data = open('input').read().strip().split('\n')
    expanded = expand(data, 1000000)
    distance = shortest_paths_distance(expanded)
    print(distance)

def shortest_paths_distance(data):
    distance = 0
    visited = []
    for y,x in data:
        visited.append((y,x))
        for v,u in data:
            if (v,u) in visited:
                continue
            dist = abs(v-y) + abs(u-x)
            distance += dist
    return distance

def expand(data, extra):
    galaxies = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                galaxies.append((y,x))

    rows = [y for y in range(len(data)) if y not in [x[0] for x in galaxies]]
    cols = [x for x in range(len(data[0])) if x not in [x[1] for x in galaxies]]

    expanded = []
    for y,x in galaxies:
        ny = y
        nx = x
        for v in rows:
            if v < y:
                ny += extra - 1
        for u in cols:
            if u < x:
                nx += extra - 1
        expanded.append((ny,nx))
    return expanded

part1()
part2()
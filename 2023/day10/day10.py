data = open('input').read().split('\n')
visited = set()

def part1():
    start = None
    for y in range(len(data)):
        if 'S' in data[y]:
            x = data[y].find('S')
            start = (y,x)
            break
    visited.add(start)
    if data[y][x + 1] in '-7J':
        current = (y, x + 1)
    if data[y][x - 1] in '-FL':
        current = (y, x - 1)
    if data[y - 1][x] in '|F7':
        current = (y - 1, x)
    if data[y + 1][x] in '|LJ':
        current = (y + 1, x)
    paths = {
        '-': [(0,1),(0,-1)],
        '|': [(1,0),(-1,0)],
        'L': [(0,1),(-1,0)],
        'F': [(0,1),(1,0)],
        '7': [(0,-1),(1,0)],
        'J': [(0,-1),(-1,0)]
    }
    prev = current
    while True:
        visited.add(current)
        (y,x) = current
        token = data[y][x]
        for v,u in paths[token]:
            next = (y + v, x + u)
            if next != prev:
                prev = current
                current = next
                break
        if current == start:
            break
    print(len(visited) // 2)

def part2():
    count = 0
    for y in range(len(data)):
        out = True
        for x in range(len(data[y])):
            c = data[y][x]
            if (y,x) in visited:
                if c == 'F':
                    ignore = '7'
                elif c == 'L':
                    ignore = 'J'
                elif c == '-':
                    continue
                else:
                    if c != ignore:
                        out = not out
                    seen = ''
            elif not out:
                count += 1      
    print(count)

part1()
part2()
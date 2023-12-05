import sys

def part1():
    with open('input') as f:
        data = f.read().strip()
        seeds, *others = data.split('\n\n')
        seeds = [int(x) for x in seeds.split(':')[1].split()]
        maps = [x.split(':')[1].strip() for x in others]
        maps = [[[int(n) for n in sm.split()] for sm in m.split('\n')] for m in maps]

        location = sys.maxsize
        for seed in seeds:
            a = get_val(maps[0], seed)
            b = get_val(maps[1], a)
            c = get_val(maps[2], b)
            d = get_val(maps[3], c)
            e = get_val(maps[4], d)
            f = get_val(maps[5], e)
            g = get_val(maps[6], f)
            if g < location:
                location = g
        
        print(location)

def part2():
    with open('input') as f:
        data = f.read().strip()
        seeds, *others = data.split('\n\n')
        seeds = [int(x) for x in seeds.split(':')[1].split()]
        seeds = [x for x in zip(seeds[0::2], seeds[1::2])]
        maps = [x.split(':')[1].strip() for x in others]
        maps = [[[int(n) for n in sm.split()] for sm in m.split('\n')] for m in maps]

        location = 0
        while True:
            f = get_key(maps[6], location)
            e = get_key(maps[5], f)
            d = get_key(maps[4], e)
            c = get_key(maps[3], d)
            b = get_key(maps[2], c)
            a = get_key(maps[1], b)
            seed = get_key(maps[0], a)

            for x,y in seeds:
                if seed >= x and seed < x+y:
                    print(location)
                    return
            
            location += 1

def get_val(map, item):
    d,s,r = 0,1,2
    for m in map:
        if item >= m[s] and item < m[s] + m[r]:
            return m[d] + (item - m[s])
    return item

def get_key(map, value):
    d,s,r = 0,1,2
    for m in map:
        if value >= m[d] and value < m[d]+m[r]:
            return m[s] + (value - m[d])
    return value

part1()
part2()
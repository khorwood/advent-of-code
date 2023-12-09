def part1():
    sum = 0
    with open('input') as f:
        oases = [[int(x) for x in l.split()] for l in f.read().strip().split('\n')]
        for oasis in oases:
            diffs = []
            item = oasis
            while any(x != 0 for x in item):
                diff = [y-x for x,y in zip(item[0::], item[1::])]
                diffs.append(diff)
                item = diff
            acc = 0
            for diff in diffs:
                acc += diff[-1]
            next_value = oasis[-1] + acc
            sum += next_value
    print(sum)

def part2():
    sum = 0
    with open('input') as f:
        oases = [[int(x) for x in l.split()] for l in f.read().strip().split('\n')]
        for oasis in oases:
            diffs = []
            item = oasis
            while any(x != 0 for x in item):
                diff = [y-x for x,y in zip(item[0::], item[1::])]
                diffs.append(diff)
                item = diff
            acc = 0
            for i in range(len(diffs)-1,-1,-1):
                diff = diffs[i]
                acc =  diff[0] - acc
            next_value = oasis[0] - acc
            sum += next_value
    print(sum)

part1()
part2()
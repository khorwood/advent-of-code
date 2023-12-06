import math

def part1():
    with open('input') as f:
        times, distance = f.read().strip().split('\n')
        times = [int(x) for x in times.split(':')[1].split()]
        distance = [int(x) for x in distance.split(':')[1].split()]
        pairs = zip(times, distance)

        ways_to_win = []
        for time, distance in pairs:
            winners = 0
            for v in range(time):
                if v * (time - v) > distance:
                    winners += 1
            ways_to_win.append(winners)
        
        print(math.prod(ways_to_win))

def part2():
    with open('input') as f:
        time, distance = f.read().strip().split('\n')
        time = int(time.split(':')[1].replace(' ',''))
        distance = int(distance.split(':')[1].replace(' ',''))

        winners = 0
        for v in range(time):
            if v * (time - v) > distance:
                winners += 1

        print(winners)        

part1()
part2()
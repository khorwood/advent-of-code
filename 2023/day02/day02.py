import re

LIMITS = { 'red': 12, 'green': 13, 'blue': 14 }

def part1():
    with open('input', 'r') as f:
        sum = 0
        for line in f:
            game = line.split(':')
            id = int(re.findall('\d+', game[0])[0])
            rounds = game[1].split(';')
            isPossible = True
            for r in rounds:
                red = int(next(iter(re.findall('(\d+) red', r)), '0'))
                green = int(next(iter(re.findall('(\d+) green', r)), '0'))
                blue = int(next(iter(re.findall('(\d+) blue', r)), '0'))
                if red > LIMITS['red'] or green > LIMITS['green'] or blue > LIMITS['blue']:
                    isPossible = False
            if isPossible:
                sum += id
        print(sum)

def part2():
    with open('input', 'r') as f:
        sum = 0
        for line in f:
            game = line.split(':')
            rounds = game[1].split(';')
            min = [0, 0, 0]
            for r in rounds:
                red = int(next(iter(re.findall('(\d+) red', r)), '0'))
                green = int(next(iter(re.findall('(\d+) green', r)), '0'))
                blue = int(next(iter(re.findall('(\d+) blue', r)), '0'))
                min[0] = max(min[0], red)
                min[1] = max(min[1], green)
                min[2] = max(min[2], blue)
            power = min[0] * min[1] * min[2]
            sum += power
        print(sum)

part1()
part2()
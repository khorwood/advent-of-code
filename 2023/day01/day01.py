import re

def part1():
    regex = re.compile('\d')
    sum = 0
    with open('input', 'r') as f:
        for line in f:
            numbers = regex.findall(line)
            first = int(numbers[0])
            last = int(numbers[-1])
            sum += first * 10 + last
    print(sum)

NUM_MAP = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }

def parseNum(input):
    if input.isdigit():
        return int(input)
    return int(NUM_MAP[input])

def part2():
    regex = re.compile('(?=(\d)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine))')
    sum = 0
    with open('input','r') as f:
        for line in f:
            numbers = regex.findall(line)
            first = parseNum(next(i for i in numbers[0] if i != ''))
            last = parseNum(next(i for i in numbers[-1] if i != ''))
            sum += first * 10 + last
    print(sum)

part1()
part2()
def part1():
    data = open('input').read().strip().split(',')
    checksum = sum([hash(x) for x in data])
    print(checksum)

def part2():
    boxes: dict[int, dict[str, int]] = { i: {} for i in range(256)}

    sequence = open('input').read().strip().split(',')
    for item in sequence:
        if '=' in item:
            label, number = item.split('=')
            boxes[hash(label)][label] = int(number)
        else:
            label = item.removesuffix('-')
            h = hash(label)
            if label in boxes[h]:
                del boxes[h][label]

    total = 0
    for b in range(256):
        box = boxes[b]
        s = 1
        for slot in box:
            power = (b + 1) * s * box[slot]
            total += power
            s += 1
    print(total)
  

def hash(input: str):
    value = 0
    for c in input:
        value += ord(c)
        value *= 17
        value %= 256
    return value

part1()
part2()
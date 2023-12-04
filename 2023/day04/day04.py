import re

def part1():
    total = 0
    with open('input') as f:
        for line in f:
            card = line.split(':')
            game = card[1].split('|')
            winners = re.findall(r'\d{1,2}', game[0])
            numbers = re.findall(r'\d{1,2}', game[1])
            score = 0
            for winner in winners:
                if winner in numbers:
                    if score == 0:
                        score = 1
                    else:
                        score = score * 2
            total += score
        print(total)

def part2():
    total = 0
    cards = []
    with open('input') as f:
        for line in f:
            card = line.split(':')
            id = int(re.findall(r'\d+', card[0])[0])
            game = card[1].split('|')
            winners = re.findall(r'\d{1,2}', game[0])
            numbers = re.findall(r'\d{1,2}', game[1])
            cards.append({'id': id, 'winners': winners, 'numbers': numbers, 'count': 1})
        
        for card in cards:
            score = 0
            for winner in card['winners']:
                if winner in card['numbers']: score += 1
            count = card['count']
            for x in range(score):
                cards[card['id'] + x]['count'] += 1 * count
            total += card['count']
    print(total)

part1()
part2()
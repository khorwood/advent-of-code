def poker(joker=False):
    order = 'J23456789TQKA' if joker else '123456789TJQKA'
    with open('input') as f:
        data = f.read().strip().split('\n')
        scored = []
        for line in data:
            hand, bid = line.split()
            counts = {}
            jokers = 0
            for card in hand:
                if card == 'J':
                    jokers += 1
                    continue
                if not card in counts:
                    counts[card] = 0
                counts[card] += 1
            counts = sorted(counts.values(), reverse=True)
            if len(counts) == 0:
                counts.append(0)
            counts[0] += jokers
            counts.extend([order.index(x) for x in hand])
            scored.append((counts, hand, int(bid)))
        scored.sort()
        total = 0
        multiplier = 1
        for _,_,bid in scored:
            total += bid * multiplier
            multiplier += 1
        print(total)

poker()
poker(joker=True)
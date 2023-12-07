from copy import deepcopy
data = open(__file__.replace('code.py', 'data.txt'), "r").read().splitlines()
cards = [s.split() for s in data]
cards = [(c[0], int(c[1])) for c in cards]

# Part 1 & 2
def winnings(cards, part=1):
    cards = deepcopy(cards)
    for i, (card, bid) in enumerate(cards):
        c = {x: card.count(x) for x in card}

        if part == 2: # Wild Jokers
            if ('J' in c) and len(c) > 1:
                add = c.pop('J')
                for k, v in c.items():
                    if v == max(c.values()):
                        c[k] += add
            
        # Hand score
        match sorted(c.values()):
            case [5]:
                score = 7
            case [1, 4]:
                score = 6
            case [2, 3]:
                score = 5
            case [1, 1, 3]:
                score = 4
            case [1, 2, 2]:
                score = 3
            case [1, 1, 1, 2]:
                score = 2
            case [1, 1, 1, 1, 1]:
                score = 1
    
        # Rank score
        if part == 1:
            rank = '23456789TJQKA'
        if part == 2:
            rank = 'J23456789TQKA'
        score = int(str(score) + ''.join([f"{rank.find(x):02d}" for x in card]))
        cards[i] = tuple(list(cards[i]) + [score])

    cards.sort(key=lambda x: x[2])
    print(f'Part {part}: {sum([(i+1)*c[1] for i, c in enumerate(cards)])}')

winnings(cards, part=1)
winnings(cards, part=2)

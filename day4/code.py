from collections import defaultdict
data = open("day4/data.txt", "r").read().splitlines()

# Part 1
card_matches = {}
for i, s in enumerate(data):
    a, b = s.split(': ')[1].split(' | ')
    a = [int(x) for x in a.split(' ') if x != '']
    b = [int(x) for x in b.split(' ') if x != '']
    n = len(set(a).intersection(set(b)))
    card_matches[i+1] = n

print(f'Part 1: {sum([2**(v-1) for v in card_matches.values() if v > 0])}')
       
# Part 2
total_cards = {k: 1 for k in range(1, len(data)+1)}
for i in range(1, len(data) + 1):
    for wins in range(1, card_matches[i] + 1):
        total_cards[i+wins] += total_cards[i]

print(f'Part 2: {sum(total_cards.values())}')

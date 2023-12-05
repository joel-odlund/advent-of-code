from dataclasses import dataclass

input = open("input.txt", "r").read().split("\n")


def part1():
    return sum([0 if hits == 0 else 2 ** (hits - 1) for hits in (hitzpercard())])

def hitzpercard():
    hits_per_card = []
    for card in input:
        card = card.split(":")[1]
        winners, haves = [s.split() for s in card.split("|")]
        hits_per_card.append(len(set(winners).intersection(set(haves))))
    return hits_per_card
print('part 1', part1())


def draw(hits_per_card, number_of_cards, total):
    if not hits_per_card:
        return total
    this_hits, this_number = hits_per_card.pop(0), number_of_cards.pop(0)
    for card in range(min(this_hits, len(number_of_cards))):
        number_of_cards[card] = number_of_cards[card] + this_number
    return draw(hits_per_card, number_of_cards, total + this_number)
def part_2():
    return draw(hitzpercard(), [1 for _ in input], 0)
print('part 2', part_2())

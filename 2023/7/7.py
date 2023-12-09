from copy import copy

input = open("input.txt", "r").read().split("\n")


def card_value(card):
    return int({"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}.get(card, card))
def card_value_2(card):
    return int({"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}.get(card, card))




def hand_value_1(hand):
    # represent the hand as ordered list of group sizes
    groups = {}
    for card in hand:
        groups[card] = groups.get(card,0) + 1
    groups = tuple(sorted(groups.values(), reverse=True))
    # determine hand value based on group configuration, 5 of a kind, 4 of a kind, etc
    order = [(5,), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1,1,1,1,1)]
    order.reverse()
    return order.index(groups)



def possible_hands(hand):
    # yield all hands that a hand with jokers can represent
    JOKER = 1
    if JOKER not in hand:

        yield hand
        return
    first_joker = hand.index(JOKER)
    for joker_value in range(2,15):
        possible_hand = copy(hand)
        possible_hand[first_joker] = joker_value
        yield from possible_hands(possible_hand)


def hand_value_2(hand):
    possible_handz = list(possible_hands(hand))

    return max(hand_value_1(h) for h in possible_handz)

def hand_order_1(hand):
    return [hand_value_1(hand)] + hand

def hand_order_2(hand):
    return [hand_value_2(hand)] + hand

def best_possible_hand_2(hand):
    return hand_order_2(list(possible_hands(hand))[-1])

def read1(row):
    hand, value = row.split()
    return [card_value(c) for c in hand], int(value)

def read2(row):
    hand, value = row.split()
    return [card_value_2(c) for c in hand], int(value)



hands = [read1(row) for row in input]
hands = sorted(hands, key=lambda x : hand_order_1(x[0]))

sum = 0
for rank,  (hand, value) in enumerate(hands, start=1):
    print (hand, hand_value_1(hand))
    sum += rank * value
print(sum)


hands2 = [read2(row) for row in input]
hands2 = sorted(hands2, key=lambda x : hand_order_2(x[0]))
sum = 0
for rank,  (hand, value) in enumerate(hands2, start=1):
    print ( hand, hand_value_2(hand), best_possible_hand_2(hand))
    sum += rank * value
print(sum)

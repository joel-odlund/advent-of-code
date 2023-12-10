input = open("input.txt", "r").read().split("\n")
numbers = [[int(n) for n in line.split()] for line in input]

def line_below(sequence):
    out = [b-a for a, b in zip(sequence[:-1], sequence[1:]) ]
    return out

def next_number(sequence):
    if done(sequence):
        return 0
    else:
        return sequence[-1] + next_number(line_below(sequence))

def previous_number(sequence):
    if done(sequence):
        return 0
    else:
        out = sequence[0] - previous_number(line_below(sequence))
    return out


def done(sequence):
    return all([number == 0 for number in sequence])


solution1 = sum(next_number(line) for line in numbers)
solution2 = sum(previous_number(line) for line in numbers)

print(solution1, solution2)


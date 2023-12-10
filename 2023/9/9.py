input = open("input.txt", "r").read().split("\n")
lines = [[int(n) for n in line.split()] for line in input]


def line_below(line):
    return [b - a for a, b in zip(line[:-1], line[1:])]


def next_number(line):
    if done(line):
        return 0
    else:
        return line[-1] + next_number(line_below(line))


def previous_number(line):
    if done(line):
        return 0
    else:
        out = line[0] - previous_number(line_below(line))
    return out


def done(sequence):
    return all([number == 0 for number in sequence])


solution1 = sum(next_number(line) for line in lines)
solution2 = sum(previous_number(line) for line in lines)

print(solution1, solution2)

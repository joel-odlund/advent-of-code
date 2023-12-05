input = open("input.txt", "r").read().split("\n")

lines = len(input)
columns = len(input[0])


def neighbors(line, col, matrix):
    """
    yield all neighbors of a cell in a matrix
    as tuples of

    """
    # loop through neighbouring coordinates
    for y in (-1, 0, 1):
        for x in (-1, 0, 1):
            if (x != 0 or y != 0):  # avoid myself as neighbor
                nx = col + x
                ny = line + y
                # avoid neigbors outside the matrix
                if nx >= 0 and ny >= 0 and nx < columns and ny < lines:
                    yield ny, nx, matrix[ny][nx]


sum = 0
asterisks = {}
for line_n, line in enumerate(input):
    digits = ""
    part_no = False
    asterisk_neighbors = set()
    for col_n, char in enumerate(line + "."):
        if char in "1234567890":
            digits += char
            for ny, nx, n in neighbors(line_n, col_n, input):
                if n not in "1234567890.":
                    part_no = True
                if n == '*':
                    asterisk_neighbors.add((ny, nx))

        else:
            if digits and part_no:
                sum += int(digits)
                xx = len(digits)
                input[line_n] = input[line_n][:col_n - xx] + "X" * xx + line[col_n:]
                for nx, ny in asterisk_neighbors:
                    if (ny, nx) not in asterisks:
                        asterisks[(ny, nx)] = set()
                    asterisks[(ny, nx)].add((line_n, col_n, int(digits)))

            digits = ""
            part_no = False
            asterisk_neighbors = set()

print(sum)

# gears are asterisks with exactly two part numbers
gears = {k: v for k, v in asterisks.items() if len(v) == 2}

sum2 = 0

for gear in gears.values():
    sum2 += list(gear)[0][2] * list(gear)[1][2]

print(sum2)

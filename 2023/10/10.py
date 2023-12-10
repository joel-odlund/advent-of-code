import copy
import math
from tqdm import tqdm

inpu = open("input.txt", "r").read().split("\n")
# inpu = open("example2.txt", "r").read().split("\n")
# inpu = open("example3.txt", "r").read().split("\n")

dirs = {}
dirs["-"] = [(0, -1), (0, 1)]
dirs["|"] = [(-1, 0), (1, 0)]
dirs["7"] = [(0, -1), (1, 0)]
dirs["L"] = [(-1, 0), (0, 1)]
dirs["J"] = [(-1, 0), (0, -1)]
dirs["F"] = [(1, 0), (0, 1)]
dirs["S"] = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dirs['.'] = []
dirs['X'] = []

views = {}
views["-"] = "─"
views["|"] = "│"
views["7"] = "┐"
views["L"] = "└"
views["J"] = "┘"
views["F"] = "┌"
views["S"] = "╳"
views['.'] = "."
views[','] = " "
views['X'] = "X"
views['O'] = "O"
views['i'] = "i"


def add_edge(input, edgechar='X'):
    out = []
    for i in input:
        out.append(edgechar + i + edgechar)
    edge = edgechar * len(out[0])
    return [edge, *out, edge]


def get_vertices(input):
    v = {}
    s = None

    for line_no, line in enumerate(input):
        for char_no, pipe in enumerate(line):
            if not pipe == '.':
                v[(line_no, char_no)] = ((line_no, char_no), pipe)
            if pipe == 'S':
                s = ((line_no, char_no), pipe)
    return v, s


vertices, s_vertex = get_vertices(add_edge(add_edge(inpu, ".")))


def neighbors(vertex):
    (line, char), pipe = vertex
    return [(line + dline, char + dchar) for dline, dchar in dirs[pipe]]


def next_node(vertex, coming_from):
    alternatives = [c for c in connections(vertex) if not c == coming_from]
    if not alternatives:
        return None
    assert len(alternatives) == 1 or not coming_from
    return alternatives[0]


def bad_pipe(vertex, coming_from):
    if vertex[1] == 'S':
        return False
    if not next_node(vertex):
        return True


memo = {}


def distance_to_s(vertex, coming_from=None):
    if (vertex, coming_from) in memo:
        return memo[(vertex, coming_from)]
    if vertex[1] == 'S':
        return 0
    if not coming_from:
        cs = connections(vertex)
        if not connections(vertex):
            return math.inf
        value = min(distance_to_s(vertex, coming_from=c) for c in cs)
        memo[(vertex, coming_from)] = value
        return value

    cursor1 = cursor2 = (vertex, coming_from)
    toggle = False

    def update(cursor):
        v, cf = cursor

        return (next_node(v, cf), v)

    steps = 0
    seen = [vertex]
    while True:
        cursor1 = update(cursor1)
        seen = [*seen, cursor1[0]]
        if cursor1 in memo:
            return memo[cursor1]
        if cursor1[0] in memo:
            return memo[cursor1[0]]
        steps += 1
        if toggle:
            cursor2 = update(cursor2)
        if cursor1 == cursor2:
            return math.inf
        if not cursor1[0]:
            return math.inf
        if cursor1[0][1] == 'S':
            return steps
        toggle = not toggle


def get_loop(s_vertex):
    in_loop = [s_vertex]
    prev = s_vertex
    v = connections(s_vertex)[0]
    while v != s_vertex:
        in_loop.append(v)
        old_v = v
        v = next_node(v, prev)
        prev = old_v
    return in_loop


def empty_grid(input):
    out = []
    for line in add_edge(input):
        out.append(['.' for c in line])

    return out


def connections(vertex):
    location, pipe = vertex
    c = []
    for n in neighbors(vertex):
        if n in vertices and location in neighbors(vertices[n]):
            c.append(vertices[n])
    return c


def solution1():
    distances = [distance_to_s(v) for v in tqdm(vertices.values())]
    return max(d for d in distances if not math.isinf(d))


def expand_loop(loop):
    def expand_vertex(vertex):
        (line, col), pipe = vertex
        return (line * 2, col * 2), pipe

    expanded = set()
    for vertex in loop:
        new_vertex = expand_vertex(vertex)
        expanded.add(new_vertex)
        conns = [expand_vertex(c) for c in connections(vertex)]
        (new_line, new_col), _ = new_vertex
        for (c_line, c_col), pipe in conns:
            link_line = int((c_line + new_line) / 2)
            link_col = int((c_col + new_col) / 2)
            if link_line == c_line:
                char = "-"
            elif link_col == c_col:
                char = "|"
            else:
                raise RuntimeError()

            expanded.add(((link_line, link_col), char))

    return expanded


def expanded_grid(input, transparent=False):
    out = []
    gap, empty = ',', '.'
    for line in input:
        out_line = []
        gap_line = []
        for elem in line:
            if elem == 'X':
                out_line = [*out_line, "X", "X"]
                gap_line = [*gap_line, "X", "X"]
            else:
                out_line = [*out_line, empty, gap]
                gap_line = [*gap_line, gap, gap]
        out.append(out_line)
        out.append(gap_line)

    return out


def nodes(grid):
    for line_no, line in enumerate(grid):
        for col_no, col in enumerate(line):
            yield (line_no, col_no), col


def fill_outside(start, grid):
    frontier = [start]
    while frontier:
        row, col = frontier.pop()
        pipe = grid[row][col]
        if pipe in ",.":
            grid[row][col] = 'O'
            for n in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                frontier.append(n)
    return grid


def fill_inside(grid):
    c = 0
    for line_no, line in enumerate(grid):
        for col_no, col in enumerate(line):
            if col == '.':
                c += 1
                grid[line_no][col_no] = "i"
    return grid, c


def display(grid):
    out = copy.deepcopy(grid)
    for line_no, line in enumerate(grid):
        for col_no, col in enumerate(line):
            out[line_no][col_no] = views[col]

    return out


def compress(grid):
    out = []
    for line_no, line in enumerate(grid):
        if line_no % 2 == 0:
            l = []
            for col_no, col in enumerate(line):
                if col_no % 2 == 0:
                    l.append(col)
            out.append(l)
    return out


def solution2():
    inputs = add_edge(inpu, ".")
    inputs = add_edge(inputs, 'X')
    loop = get_loop(s_vertex)
    grid = empty_grid(inputs)
    for (line, col), pipe in loop:
        grid[line][col] = pipe

    for line in grid:
        print("".join(line))

    exp_grid = expanded_grid(inputs, transparent=False)
    exp_loop = expand_loop(loop)
    for (line, col), pipe in exp_loop:
        exp_grid[line][col] = pipe
    known_nodes = {}
    for node in nodes(exp_grid):
        location, _ = node
        known_nodes[location] = node

    for node in exp_loop:
        location, _ = node
        known_nodes[location] = node

    for (line, col), pipe in known_nodes.values():
        exp_grid[line][col] = pipe

    corner = (4, 4)
    exp_grid = fill_outside(corner, exp_grid)
    exp_grid, insides = fill_inside(exp_grid)

    disp = display(exp_grid)
    for line in disp:
        print("".join(line))

    comp = compress(disp)
    for line in comp:
        print("".join(line))

    print(f"{insides=}")


solution2()

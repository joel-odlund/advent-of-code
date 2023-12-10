import math
input = open("input.txt", "r").read().split("\n")

path, nodes = input[0], input[2:]
nodes = [tuple(node.split(" = ")) for node in nodes]
nodes = [(vertex, edge.replace(' ',"").replace("(","").replace(')', "").split(",")) for vertex, edge in nodes]
graph = {vertex: edge for vertex, edge in nodes}
from itertools import islice


def solve1():
    return
    steps = 0
    location = 'AAA'
    while True:
        for direction in path:
            steps += 1
            direction = "LR".index(direction)
            location = graph[location][direction]
            if location == 'ZZZ':
                return steps

print(solve1())

#2
start_locations = [location for location in graph.keys() if location.endswith('A')]


#yield the ending steps for a start location
def zstates(location):
    steps = 0
    while True:
        for direction in path:
            steps +=1

            direction = "LR".index(direction)
            location = graph[location][direction]
            if location.endswith('Z'):
                    yield steps

# we notice that the ending locations all loop from the beginning of the path
# we can then find the loop length for each starting location
# and use the lowest common divisor as the first step where they are all on a
# ending location

loops = []
for l in start_locations:
    zs = list(islice(zstates(l),5))
    diffs  = [x-y for x,y in zip(zs,[0]+zs)]

    #assert that end locations occur at regular intervals from the start
    assert len(set(diffs)) == 1
    loops.append( diffs[0])

print(loops)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def lowest_common_divisor(numbers):
    product = math.prod(numbers)
    factors = prime_factors(product)
    lcd = math.prod(set(factors))
    return lcd

print(lowest_common_divisor(loops))
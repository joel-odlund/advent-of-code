import math
from math import sqrt

input = open("input.txt", "r").read().split("\n")

times = input[0].split(':')[1].split()
distances = input[1].split(':')[1].split()

races = [(int(t), int(d)) for t, d in zip(times, distances)]

def distance(button_time, race_time):
    return (race_time - button_time) * button_time

def winning_interval(race_time, max_distance):

    # max_distance = speed * drive_time
    # max_distance = button_time * (race_time - button_time)
    # solve for button_time
    # . The two solutions define the interval of winning button times.
    # we limit the interval to winning integers.


    solution1 = math.ceil((race_time / 2) - (math.sqrt(race_time ** 2 - 4 * max_distance) / 2))
    solution2 = math.floor((race_time / 2) + (math.sqrt(race_time ** 2 - 4 * max_distance) / 2))

    return solution1, solution2

def ways_to_win(race_time, max_distance):
    winning_times = winning_interval(race_time, max_distance)
    return winning_times[1] - winning_times[0] + 1

product = 1
for t, d in races:
    product *= ways_to_win(t, d)

print(product)


distance2 = int("".join(distances))
time2 = int("".join(times))
print(ways_to_win(time2, distance2))





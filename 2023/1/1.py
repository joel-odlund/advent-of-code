import re

input = open("input.txt", "r").read().split("\n")


def part1(input):
    sum = 0
    for line in input:
        digits = [digit for digit in line if digit.isdigit()]
        value = int(digits[0] + digits[-1])
        sum += value
    return sum


print('part 1', part1(input))


def part_2(input):
    digits = {"one": "1",
              "two": "2",
              "three": "3",
              "four": "4",
              "five": "5",
              "six": "6",
              "seven": "7",
              "eight": "8",
              "nine": "9"}

    digit_pattern = f"(?=([1-9]|{'|'.join(digits.keys())}))"

    sum = 0
    for line in input:
        matches = [digits.get(m, m) for m in (re.findall(digit_pattern, line))]
        calibration_value = int(matches[0] + matches[-1])
        sum += calibration_value
    return sum

print('part 2', part_2(input))

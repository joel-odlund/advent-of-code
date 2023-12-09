input = open("input.txt", "r").read().split("\n")

alpha= 'abcdefghijklmnopqrstuvwxyz'
alpha= " " + alpha + alpha.upper()
sum = 0

for line in input:
    middle = len(line)//2
    left, right = line[:middle], line[middle:]
    thing = set(left).intersection(set(right)).pop()
    score = alpha.index(thing)
    print(score)
    sum += score

print(sum)

groups= []
things = None
for i, line in enumerate(input):
    if i % 3 == 0:
        if things:
            thing = things.pop()
            groups.append(alpha.index(thing))
    else:





    things = set(lin).intersection(things).pop()
    score = alpha.index(thing)
    print(score)
    sum += score
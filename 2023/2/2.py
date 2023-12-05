input = open("input.txt", "r").read().split("\n")

maxi = {'red': 12, 'green':13 , 'blue': 14}

sum1 = 0
sum2 = 0
for game_number, game in enumerate(input, start=1):
    game = game.split(':')[1]
    ok = True
    mini = {'red': 0, 'green': 0, 'blue': 0}
    for round in game.split(';'):
        picks = round.split(',')
        for pick in picks:
            n, color = pick.split()
            n = int(n)
            if n > maxi[color]:
                ok = False

            mini[color] = max(mini[color], n)
    power = mini['red'] * mini['blue'] * mini['green']
    sum2 += power


    if ok:
        sum1 += game_number


print('sum 1', sum1)
print('sum 2', sum2)


input = open("input.txt", "r").read().split("\n")

elfs= []
elf = 0
for line in input:
    if line:
        elf += int(line)
    else:
        elfs.append(elf)
        elf=0

print(max(elfs))
print(sum(sorted(elfs, reverse=True )[:3]))

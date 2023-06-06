from collections import defaultdict

with open("input.in") as fin:
    content = fin.read().split("\n\n")

crates = content[0].splitlines()[:-1]
moves = content[1].splitlines()
stacks = defaultdict(list)

# Loop through crates to build our stacks, steps of 4 to obtain characters
for crate in crates[::-1]:
    for i, box in enumerate(crate[1::4]):
        if box != " ":
            stacks[i+1].append(box)

for line in moves: 
    broken = line.split()
    move, frm, to = int(broken[1]), int(broken[3]), int(broken[5])
    stacks[to] = stacks[to] + stacks[frm][-move:]
    stacks[frm] = stacks[frm][:-move]

res = ""
for stack in stacks:
    res += stacks[stack][-1]

print(res)
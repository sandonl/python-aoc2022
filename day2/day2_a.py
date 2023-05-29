with open("input.in") as fin:
    content = fin.read().strip().split("\n")

# Elf 
# A - Rock, B for Paper, C for Scissors

# Me 
# X - Rock, Y for Paper, Z for Scissors
# 1 for rock, 2 for paper, 3 for scissors

# 0 for a loss, 3 for a draw, 6 for a win

combos = { 
    "A X": 1 + 3, 
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3
}

curr_score = 0 

for line in content:
    curr_score += combos[line]

print(curr_score)

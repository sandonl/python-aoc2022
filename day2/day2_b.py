with open("input.in") as fin:
    content = fin.read().strip().split("\n")

# Elf 
# A - Rock, B for Paper, C for Scissors

# Me 
# X - lose (0), Y - draw (3), Z - (lose)

# 0 for a loss, 3 for a draw, 6 for a win

combos = { 
    "A X": 3 + 0, 
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6
}

curr_score = 0 

for line in content:
    curr_score += combos[line]

print(curr_score)

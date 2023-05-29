with open("input.in") as fin:
    content = fin.read().strip().split("\n")

curr_sum = 0 

for line in content:
    mid = len(line) // 2 
    sack_one = line[:mid]
    sack_two = line[mid:]

    common = set()
    for char in sack_one:
        if char in sack_two:
            common.add(char)
    
    for char in common:
        if char.islower(): 
            curr_sum += ord(char) - 96
        else:
            curr_sum += ord(char) - 38

print(curr_sum)

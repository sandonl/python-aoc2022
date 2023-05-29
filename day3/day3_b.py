with open("input.in") as fin:
    content = fin.read().strip().split("\n")

curr_sum = 0 

for i in range(0, len(content), 3):
    sack_one, sack_two, sack_three = set(content[i]), set(content[i+1]), set(content[i+2])
    common = sack_one.intersection(sack_two, sack_three)
    
    common_char = common.pop()
    if common_char.islower():
        curr_sum += ord(common_char) - 96
    else: 
        curr_sum += ord(common_char) - 38 

print(curr_sum)

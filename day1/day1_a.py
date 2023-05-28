with open("input.in") as fin:
    content = fin.read().strip().split("\n")

curr_sum = 0 
curr_max = 0

for line in content: 
    if line != "":
        curr_sum = curr_sum + int(line)
    else:
        curr_max = max(curr_max, curr_sum)
        curr_sum = 0 

print(curr_max)
        
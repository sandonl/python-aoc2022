input = open('input.txt', 'r')

content = []
for line in input.readlines():
    content.append(line.strip())

curr_sum = 0 
curr_max = 0

for line in content: 
    if line != "":
        curr_sum = curr_sum + int(line)
    else:
        curr_max = max(curr_max, curr_sum)
        curr_sum = 0 

print(curr_max)
        
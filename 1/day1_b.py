input = open('input.txt', 'r')

content = []
for line in input.readlines():
    content.append(line.strip())


curr_sum = 0 
elf_sacks = []

for line in content: 
    if line != "":
        curr_sum = curr_sum + int(line)
    else:
        elf_sacks.append(curr_sum)  
        curr_sum = 0 

elf_sacks.sort() 
print(sum(elf_sacks[-3:]))
with open("input.in") as fin:
    content = fin.read().strip().split("\n")

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
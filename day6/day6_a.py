with open("input.in") as fin:
    content = fin.read()

# Start at 4th char 
for i, char in enumerate(content[3:]): 
    curr = content[i-3: i+1]
    if len(set(curr)) == 4:
        print(i+1)
        break
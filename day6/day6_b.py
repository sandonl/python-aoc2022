with open("input.in") as fin:
    content = fin.read()

# Start at 14th char 
for i, char in enumerate(content[13:]): 
    curr = content[i-13: i+1]
    if len(set(curr)) == 14:
        print(i+1)
        break
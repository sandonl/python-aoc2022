with open("input.in") as fin:
    content = fin.read().strip().split("\n")

pairs = 0 
for line in content:
    pair_one, pair_two = line.split(",")
    range_one = pair_one.split("-")
    range_two = pair_two.split("-")

    one_lb, one_ub = int(range_one[0]), int(range_one[1])
    two_lb, two_ub = int(range_two[0]), int(range_two[1])

    if (one_lb >= two_lb and one_ub <= two_ub) or (two_lb >= one_lb and two_ub <= one_ub):
        pairs += 1 
    
print(pairs)
  
from itertools import combinations

symbs = "XYZ"

for i in range(1,4):
    combs = list(combinations(symbs,i))
    for comb in combs:
        print("".join(comb))
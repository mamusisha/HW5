from itertools import combinations

numbers = [1,2,3,4,5]
combs = list(combinations(numbers, 3))
for comb in combs:
    print(comb)
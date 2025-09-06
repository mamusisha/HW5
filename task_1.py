from itertools import permutations

word = "ABCD"
perms = list(permutations(word))

print("all permutations of 'ABCD':")
for perm in perms:
    print(''.join(perm), end=" ")
count = len(perms)
print(f"\nnumber of permutations: {count}")
import random
from itertools import product

rand_pass = "".join([str(random.randint(1,6)) for _ in  range(4)])
print(rand_pass)
for comb in product(range(1,7), repeat=4):
    comb = "".join(map(str, comb))
    print(comb, end=': ')
    if comb == rand_pass:
        print("congrats, its correct!")
        break
    else:
        print("it was wrong!")


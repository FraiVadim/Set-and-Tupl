import itertools
A = [1, 2, 3, 'A', 'B', 'C']
combinations = []
for r in range(len(A)+1):
    for combination in itertools.combinations(set(A), r):
        combinations.append(combination)
print(combinations)
with open("input.txt") as f:
    lines  = f.readlines()

expenses = list(map(int, lines))

# Brute-force solution
for i, num_1 in enumerate(expenses[:-2]):
    for j, num_2 in enumerate(expenses[i+1:]):
        target = 2020 - num_1 - num_2
        if target in expenses[j+1:]:
            print(f"Solution found: {num_1} {num_2} {target}")
            print(f"Answer = {num_1*num_2*target}")
            exit(0)

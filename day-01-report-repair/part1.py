with open("input.txt") as f:
    lines  = f.readlines()

expenses = list(map(int, lines))

for i, num_1 in enumerate(expenses):
    num_2 = 2020 - num_1
    if num_2 in expenses[i+1:]:
        print(f"Entries found: {num_1} {num_2}")
        print(f"Answer = {num_1*num_2}")
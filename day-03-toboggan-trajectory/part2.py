tree_map = []
with open("input.txt") as f:
    tree_map = f.readlines()
    tree_map = [l.strip() for l in tree_map]

height, width = len(tree_map), len(tree_map[0])
slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
total = 1

for new_row, new_column in slopes:
    column = 0
    trees = 0
    for row in range(0, height, new_row):
        if tree_map[row][column % width] == "#":
            trees += 1
        column += new_column
    total *= trees

print(f"Total: {total}")
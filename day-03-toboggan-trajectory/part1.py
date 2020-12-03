tree_map = []
with open("input.txt") as f:
    tree_map = f.readlines()
    tree_map = [l.strip() for l in tree_map]

trees = 0
height, width = len(tree_map), len(tree_map[0])
column = 0

for row in range(height):
    if tree_map[row][column % width] == "#":
        trees += 1
    column += 3

print(f"Number of trees: {trees}")
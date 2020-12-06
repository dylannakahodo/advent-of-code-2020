def parse_groups(group_file):
    return group_file.split("\n\n")


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read()

    groups = parse_groups(lines)
    groups = [l.replace("\n", "") for l in groups]

    answer = sum(len(set(group)) for group in groups)

    print(answer)
    # 6782
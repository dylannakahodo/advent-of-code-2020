from collections import Counter

def parse_groups(group_file):
    return group_file.split("\n\n")


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read()

    groups = parse_groups(lines)
    answer = 0
    for group in groups:
        total_people = group.count("\n") + 1 # account for second stripped new line character
        answers = group.replace("\n", "")
        c = Counter(answers)
        answer += len([k for k,v in c.items() if v==total_people])

    print(answer)
    # 3596

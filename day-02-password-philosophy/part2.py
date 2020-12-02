def parse_input(lines):
    output = []

    for line in lines:
        policy, password = line.split(":")
        output.append((policy, password.strip()))
    return output

def verify_policy(case):
    policy, password = case
    pos_1, pos_2 = policy.split()[0].split('-')
    char = policy.split()[1]
    pos_1, pos_2 = int(pos_1), int(pos_2)

    return (password[pos_1 - 1] == char) != (password[pos_2 - 1] == char)


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    lines = parse_input(lines)
    count = 0

    for line in lines:
        if verify_policy(line):
            count += 1
    print(count)

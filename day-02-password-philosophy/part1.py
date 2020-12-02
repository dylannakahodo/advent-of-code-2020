def parse_input(lines):
    output = []

    for line in lines:
        policy, password = line.split(":")
        output.append((policy, password.strip()))
    return output

def verify_policy(case):
    policy, password = case
    low, high = policy.split()[0].split('-')
    char = policy.split()[1]
    
    return int(low) <= password.count(char) <= int(high)


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    lines = parse_input(lines)
    count = 0

    for line in lines:
        if verify_policy(line):
            count += 1
    print(count)

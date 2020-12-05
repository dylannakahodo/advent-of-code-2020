required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def parse_batch_file(batch_file):
    return batch_file.split("\n\n")

def passport_is_valid(passport):
    return all(field in passport for field in required_fields)

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read()

    passports = parse_batch_file(lines)
    valid_passports = sum(1 for passport in passports if passport_is_valid(passport))


    print(valid_passports)
    # 210

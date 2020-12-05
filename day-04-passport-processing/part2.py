import re

required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def parse_batch_file(batch_file):
    return batch_file.split("\n\n")

def passport_is_valid(passport):
    return all(field in passport for field in required_fields)

def parse_raw_passport(raw_passport):
    passport = {field: None for field in required_fields}
    fields = raw_passport.split()
    for field in fields:
        key, value = field.split(":")
        passport[key] = value

    return passport 

def byr_valid(byr):
    try:
        return 1920 <= int(byr) <= 2002
    except:
        return False

def iyr_valid(iyr):
    try:
        return 2010 <= int(iyr) <= 2020
    except:
        return False

def eyr_valid(eyr):
    try:
        return 2020 <= int(eyr) <= 2030
    except:
        return False

def hgt_valid(hgt):
    try:
        if hgt.endswith("cm"):
            return 150 <= int(hgt[:-2]) <= 193
        elif hgt.endswith("in"):
            return 59 <= int(hgt[:-2]) <= 76
        return False
    except:
        return False

def hcl_valid(hcl):
    return re.match(r"#[a-f0-9]{6}", hcl)
 
def ecl_valid(ecl):
    valid_ecls = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    return ecl in valid_ecls

def pid_valid(pid):
    return re.match(r"[0-9]{9}", pid)

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read()

    raw_passports = parse_batch_file(lines)
    passports = [{}]

    for raw_passport in raw_passports:
        if passport_is_valid(raw_passport):
            passport = parse_raw_passport(raw_passport)
            passports.append(passport)
    
    

            
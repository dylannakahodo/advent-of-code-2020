with open("input.txt") as f:
    boarding_passes = f.readlines()
    boarding_passes = [l.strip() for l in boarding_passes]

def calculate_row(seat):
    row = [c for c in seat[:7]]
    lower = 0
    upper = 127

    while(row):
        c = row.pop(0)
        if c == "F":
            upper = (upper+lower) // 2
        elif c == "B":
            lower = (upper+lower+1) // 2

    return lower if c=="F" else upper

def calculate_col(seat):
    col = [c for c in seat[-3:]]
    lower = 0
    upper = 7

    while(col):
        c = col.pop(0)
        if c == "L":
            upper = (upper+lower) // 2
        if c == "R":
            lower = (upper+lower+1) // 2

    return lower if c=="L" else upper

def calculate_sid(row, col):
    return (row * 8) + col

if __name__ == "__main__":
    max_sid = 0

    for seat in boarding_passes:
        sid = calculate_sid(calculate_row(seat), calculate_col(seat))
        max_sid = max(max_sid, sid)
    
    print(max_sid)
    # 933
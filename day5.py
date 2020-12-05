# Recursivly performs binary space partitioning based on string input.
# lower_ch is that character that means take the lower half
# any other character means take the upper half
# str is the input string
# upper is the upper bound for the coded number.  The final value will be <= upper-1
# When the whole string has been decoded, lower will contain the decoded value
def binary_decode(lower_ch: str, str: str, upper: int, lower: int = 0) -> int:
    if not str: return lower

    if str[0] == lower_ch:
        return binary_decode(lower_ch, str[1:], upper - (upper - lower) // 2, lower)
    else:
        return binary_decode(lower_ch, str[1:], upper, lower + (upper - lower) // 2)

# Given a boarding pass line, returns the seat row
def decode_row(line: str) -> int:
    return binary_decode('F', line[:7], 128)

# Given a boarding pass line, returns the seat column
def decode_col(line: str) -> int:
    return binary_decode('L', line[7:], 8)

# Given a boarding pass line, returns the seat id
def seat_id(line: str) -> int:
    return decode_row(line)*8 + decode_col(line)

# Part 1 is to find the maximum seat if amongst the boarding passes
def solve_part1(filename: str) -> int:
    max_id = 0

    with open(filename) as f:
        for line in f:
            id = seat_id(line)

            if id > max_id:
                max_id = id

    return max_id

# Part 2 is to find the id of my seat
def solve_part2(filename: str) -> int:
    # all seats are open before any boarding passes have been examined
    open_seats = set()
    for row in range(128):
        for col in range(8):
            open_seats.add(row*8+col)

    with open(filename) as f:
        for line in f:
            id = seat_id(line)
            open_seats.remove(id)

    # The puzzle states that the seats with ids +1 and -1 from my seat's id are being used
    for my_seat in open_seats:
        if not (my_seat+1 in open_seats or my_seat-1 in open_seats):
            return my_seat

def main():
    print(solve_part1('input/input5.txt'))
    print(solve_part2('input/input5.txt'))

main()
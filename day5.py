# performs binary space partitioning based on string input
# lower_ch is that character that means take the lower half
# upper_ch is that character that means take the upper half
# str is the input string
# max_value is the upper end of the range
# lower end of the range is assumed to be 0
def binary_decode(lower_ch: str, upper_ch: str, str: str, max_value: int) -> int:
    lower = 0
    upper = max_value + 1

    for c in str:
        if c == lower_ch:
            upper = upper - (upper - lower) // 2
        elif c == upper_ch:
            lower = lower + (upper - lower) // 2

    return lower

# Given a boarding pass line, returns the seat row
def decode_row(line: str) -> int:
    return binary_decode('F', 'B', line[:7], 127)

# Given a boarding pass line, returns the seat column
def decode_col(line: str) -> int:
    return binary_decode('L', 'R', line[7:], 7)

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
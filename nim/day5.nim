import sets

# Recursivly performs binary space partitioning based on string input.
# lower_ch is that character that means take the lower half
# any other character means take the upper half
# str is the input string
# upper is the upper bound for the coded number.  The final value will be <= upper-1
# When the whole string has been decoded, lower will contain the decoded value
proc binary_decode(lower_ch: char, str: string, upper: int, lower: int = 0): int =
    if str == "": return lower

    if str[0] == lower_ch:
        return binary_decode(lower_ch, str[1..^1], upper - (upper - lower) div 2, lower)
    else:
        return binary_decode(lower_ch, str[1..^1], upper, lower + (upper - lower) div 2)

# Given a boarding pass line, returns the seat row
proc decode_row(line: string): int =
    return binary_decode('F', line[0..7], 128)

# Given a boarding pass line, returns the seat column
proc decode_col(line: string): int =
    return binary_decode('L', line[7..^1], 8)

# Given a boarding pass line, returns the seat id
proc seat_id(line: string): int =
    return decode_row(line)*8 + decode_col(line)


proc solve_p1(filename: string): int =
    for line in lines filename:
        let id = seat_id(line)

        if id > result:
            result = id


proc solve_p2(filename: string): int =
    var open_seats = initOrderedSet[int]()

    for row in 1..127:
        for col in 1..7:
            open_seats.incl(row*8+col)

    for line in lines filename:
        open_seats.excl(seat_id(line))

    for my_seat in open_seats:
        if my_seat+1 notin open_seats and my_seat-1 notin open_seats:
            return my_seat



echo solve_p1("../input/input5.txt")
echo solve_p2("../input/input5.txt")
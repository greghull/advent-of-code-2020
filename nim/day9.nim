import strutils, sequtils, sugar
# Given a series of numbers (series), and a preamble length (p_len):

# The first p_len numbers are the preamble

# A number is valid if it is a member or the preamble, or if it is the sum of two of the p_len numbers
# immediately preceeding it.

# The invalid number is the first number in the series that is not valid.

# The weakness is the sum of the min and max numbers of a subseries with length >= 2 
# that sum to the invalid number

# Returns true if there are 2 numbers in block that sum to x
proc is_valid(s: seq[int], x: int): bool =
    for i in 0 ..< s.len:
        if x-s[i] in s[i .. ^1]:
            return true
    return false

# Given a series of numbers, and a preamble length, finds the first invalid number in the series
proc find_invalid_num(s: seq[int], p_len: int): int = 
    for i in p_len ..< s.len:
        if not is_valid(s[i-p_len .. i], s[i]):
            result = s[i]

# Given a series of numbers, and the invalid number, finds the weakness
proc find_weakness(s: seq[int], invalid_num: int): int = 
    for i in 0 ..< s.len:
        var
            sum = 0
            j = i
        
        while sum < invalid_num:
            sum += s[j]
            j += 1

        if sum == invalid_num and i != j:
            result = s[i .. j].min() + s[i .. j].max()

# Returns the invalid number and weakness for the series of numbers in the specified file
proc xmas(filename: string, p_len: int): array[2, int] =
    let s = toSeq(lines filename).mapIt(it.parseInt())
    let invalid_num = find_invalid_num(s, p_len)
    let weakness = find_weakness(s, invalid_num)
    result = [invalid_num, weakness]

    
echo xmas("../input/input9.txt", 25)
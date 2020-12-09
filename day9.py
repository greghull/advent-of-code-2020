# Given a series of numbers (series), and a preamble length (p_len):

# The first p_len numbers are the preamble

# A number is valid if it is a member or the preamble, or if it is the sum of two of the p_len numbers
# immediately preceeding it.

# The invalid number is the first number in the series that is not valid.

# The weakness is the sum of the min and max numbers of a subseries of continuous numbers within
# the series that sum to the invalid number

# Returns true if there are 2 numbers in block that sum to x
def is_valid(block, x):
    for i in range(len(block)):
        if x-block[i] in block[i:]:
            return True
    
    return False

# Given a series of numbers, and a preamble length, finds the first invalid number in the series
def find_invalid_num(series, p_len):
    for i in range(p_len, len(series)):
        if not is_valid(series[i-p_len:i], series[i]):
            return series[i]
    return None

# Given a series of numbers, and the invalid number, finds the weakness
def find_weakness(series, invalid_num):
    for i in range(len(series)):
        sum = 0
        j = i

        while sum < invalid_num:
            sum += series[j]
            j += 1

        if sum == invalid_num:
            return min(series[i:j]) + max(series[i:j])

    return 0

# Returns the invalid number and weakness for the series of numbers in the specified file
def xmas(filename, p_len):
    with open(filename) as f:
        series = [int(line.rstrip('\n')) for line in f]

    invalid_num = find_invalid_num(series, p_len)
    weakness = find_weakness(series, invalid_num)
    
    return (invalid_num, weakness)

    
print(xmas('input/input9.txt', 25))

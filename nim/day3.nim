import sequtils, sugar

# Solve for how many trees we'll encounter when taking the path
# specified by down and right.
# The solver works by moving down, then to the right.
# The default path is move down 1, then move right 1.
proc solve(filename: string, down: int = 1, right: int = 1): int =
  var 
    x = 0
    y = 0

  for line in lines filename:
    # everytime we move down the appropriate number of lines, then we will move to the right
    # and check to see if we hit a tree
    if y > 0 and y mod down == 0:
      # Since the line repeats to the right infinitely, increment the x counter modulo the line length
      x = (x + right) mod line.len
      # Did we hit a tree??
      if line[x] == '#': 
          result += 1

    y += 1

  return result

const 
  DOWN = 0
  RIGHT = 1
  ROUTES = [[1,1], [1,3], [1,5], [1,7], [2,1]]

echo ROUTES.map(r => solve("../input/input3.txt", r[DOWN], r[RIGHT])).foldl(a * b)

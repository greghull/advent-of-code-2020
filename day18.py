from operator import add, mul

def read(line):
    expr = []

    while line:
        ch = line.pop(0)
        if ch == '+' or ch == '*':
            expr.append(ch)
        if ch.isdigit():
            expr.append(int(ch))
        if ch == '(':
            expr.append(read(line))
        if ch == ')':
            return expr

    return expr

def eval(expr):
    f = {"+": add, "*": mul}

    if type(expr) == int:
        return expr

    if len(expr) == 1:
        return eval(expr[0])

    a, op, b = eval(expr[0]), f[expr[1]], eval(expr[2])

    return eval([op(a,b)] + expr[3:])

def expand(expr):
    # don't try to expand an integer or an operator
    if type(expr) in [int, str]:
        return expr

    result = []
    while(expr):
        if expr[0] == '+':
            result[-1] = [result[-1], "+", expand(expr[1])]
            expr = expr[2:]
        else:
            result.append(expand(expr[0]))
            expr = expr[1:]

    return result

with open("input/input18.txt") as f:
    exprs = [read(list(line)) for line in f]

print(sum([eval(expr) for expr in exprs]))
print(sum([eval(expand(expr)) for expr in exprs]))
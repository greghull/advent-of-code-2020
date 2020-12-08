# Each command for the virtual machine is a tuple of the form (OP, ARG)
OP = 0
ARG = 1

# code is an array of commands of the form: [(op_1, arg_1), ..., (op_n, arg_n)]
# eval runs the given code and returns a tuple (acc, ip)
def eval(code):
    acc = 0             # the accumulator register
    ip = 0              # the instruction pointer
    history = set()     # keep a set of commands that have already been run

    while ip not in history:
        history.add(ip)

        if ip >= len(code):
            break

        cmd = code[ip]

        if cmd[OP] == 'nop':
            ip += 1
        elif cmd[OP] == 'acc':
            acc += cmd[ARG]
            ip += 1
        elif cmd[OP] == 'jmp':
            ip += cmd[ARG]

    return (acc, ip)

# Given a command, flips a nop -> jmp or jmp -> nop
def flip(cmd):
    if cmd[OP] == 'nop':
        cmd = ('jmp', cmd[ARG])
    elif cmd[OP] == 'jmp':
        cmd = ('nop', cmd[ARG])
    return cmd

# code is an array of commands of the form: [(op_1, arg_1), ..., (op_n, arg_n)]
# meta_eval makes a copy of the code, and modifies it before evaluating to solve part2 of the problem
# returns the same tuple as eval: (acc, ip)
def meta_eval(code):
    meta_ip = 0
    code2 = code.copy()

    while meta_ip < len(code2):
        # Try flipping the current instruction
        code2[meta_ip] = flip(code2[meta_ip])
        
        # Flip the previous instruction back if necessary
        if meta_ip > 0:
            code2[meta_ip-1] = flip(code2[meta_ip-1])

        meta_ip += 1

        ret = eval(code2)

        if ret[1] == len(code):
            return ret
# parses a line of code into a command tuple
# returns a tuple (op, arg)
def parse(line):
    tokens = line.split()
    return (tokens[0], int(tokens[1]))

def main():
    code = []
    with open('input/input8.txt') as f:
        for line in (line.rstrip('\n') for line in f):
            code.append(parse(line))

    # part 1
    print(eval(code))

    # part 2
    print(meta_eval(code))


main()
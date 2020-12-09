import sets, strutils, sequtils

type
    # A command for the virtal machines conists of an operand and an argument
    Command = tuple
        op: string
        arg: int

    # The virtual machine has 2 state registers, the accumulator and an instruction pointer
    State = tuple
        acc: int
        ip: int

# code is a sequence of commands of the form: [(op_1, arg_1), ..., (op_n, arg_n)]
# eval runs the given code and returns a state tuple (acc, ip)
proc eval(code: seq[Command]): State =
    var
        state: State
        visited = initOrderedSet[int]()

    # The program terminates once we reach any command that has already been run
    # or once the instruction pointer points past the end of the code
    while state.ip notin visited and state.ip < code.len:
        visited.incl(state.ip)

        let cmd = code[state.ip]

        case cmd.op
        of "nop": 
            state.ip += 1
        of "acc":
            state.acc += cmd.arg
            state.ip += 1
        of "jmp":
            state.ip += cmd.arg

    return state


# Given a command, flips a nop -> jmp or jmp -> nop
proc flip(cmd: Command): Command =
    case cmd.op 
    of "jmp": return ("nop", cmd.arg)
    of "nop": return ("jmp", cmd.arg)
    else: return cmd


# code is an array of commands of the form: [(op_1, arg_1), ..., (op_n, arg_n)]
# meta_eval makes a copy of the code, and modifies it before evaluating to solve part2 of the problem
# returns the same tuple as eval: (acc, ip)
proc meta_eval(code: seq[Command]): State =
    var code = code

    for meta_ip in 0 ..< code.len:
        # Try flipping the current instruction
        code[meta_ip] = flip(code[meta_ip])

        # Flip the previous instruction back if necessary
        if meta_ip > 0:
            code[meta_ip-1] = flip(code[meta_ip-1])

        result = eval(code)

        if result.ip == code.len:
            return result

# parses a line of code into a command tuple
# returns a Command tuple (op, arg)
proc parse(line: string): Command = 
    let tokens = line.split()
    return (tokens[0], tokens[1].parseInt())


proc main(filename: string) =
    let code = toSeq(lines filename).mapIt(parse(it))

    echo eval(code)
    echo meta_eval(code)

main("../input/input8.txt")
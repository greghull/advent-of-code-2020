def parse_rule(line, rules):
    parts = line.split(": ")
    rules[parts[0]] = [x.strip().split(' ') for x in parts[1].strip().replace('"', '').split("|")]

def match(rules, msg, rule_id='0', start=0):
    if rule_id in 'ab':
        return {start + 1} if start < len(msg) and rule_id == msg[start] else set()
    else:
        matches = set()
        for group in rules[rule_id]:
            buffer = {start}
            for part in group:
                temp = set()
                for loc in buffer:
                    temp |= match(rules, msg, rule_id=part, start=loc)
                buffer = temp
            matches |= buffer
        return matches
        
with open("input/input19.txt") as f:
    rules = {}
    line = f.readline().rstrip('\n')

    while line:
        parse_rule(line, rules)
        line = f.readline().rstrip('\n')

    messages = [line.rstrip('\n') for line in f]

# part 1
print([len(msg) in match(rules, msg) for msg in messages].count(True))

# part 2
rules['8'] = [['42'],['42','8']]
rules['11'] = [['42','31'],['42','11','31']]
print([len(msg) in match(rules, msg) for msg in messages].count(True))

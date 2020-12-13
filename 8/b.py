with open('input.txt', "r+") as file:
    contents = file.read()


def executeInstruction(line, instructions, accumulator, isOverride):
    instruction = instructions[line]
    candidateOp, arg = instruction

    if isOverride and candidateOp in ['nop', 'jmp']:
        op = 'jmp' if candidateOp == 'nop' else 'nop'
    else:
        op = candidateOp

    if (op == 'nop'):
        return [line + 1, accumulator]

    argValue = int(arg)
    if (op == 'acc'):
        return [line + 1, accumulator + argValue]

    if (op == 'jmp'):
        return [line + argValue, accumulator]


def find(x, xs):
    matches = list(filter(lambda e: e == x, xs))
    return None if len(matches) == 0 else matches[0]


def run(instructions, overriddenLine):
    if instructions[overriddenLine][0] == 'acc':
        return None

    line, accum, visited = [0, 0, []]

    lastLine = len(instructions) - 1
    while (find(line, visited) == None and line != lastLine):
        visited.append(line)
        line, accum = executeInstruction(
            line,
            instructions,
            accum,
            line == overriddenLine
        )

    return accum if line == lastLine else None


entries = list(filter(lambda x: x != '', contents.split('\n')))
instructions = list(map(lambda x: x.split(' '), entries))
overriddenLine = len(instructions) - 1
result = run(instructions, overriddenLine)
while result == None:
    overriddenLine -= 1
    result = run(instructions, overriddenLine)

print(result)

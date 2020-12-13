with open('input.txt', "r+") as file:
    contents = file.read()


def executeInstruction(instruction, instructions, accumulator):
    operator, arg = instructions[instruction]

    if (operator == 'nop'):
        return [instruction + 1, accumulator]

    argValue = int(arg)
    if (operator == 'acc'):
        return [instruction + 1, accumulator + argValue]

    if (operator == 'jmp'):
        return [instruction + argValue, accumulator]


def find(x, xs):
    matches = list(filter(lambda e: e == x, xs))
    return None if len(matches) == 0 else matches[0]


entries = list(filter(lambda x: x != '', contents.split('\n')))
instructions = list(map(lambda x: x.split(' '), entries))
nextInstruction, accum, visited = [0, 0, []]

# How to make it "declarative"?
while (find(nextInstruction, visited) == None):
    visited.append(nextInstruction)
    nextInstruction, accum = executeInstruction(
        nextInstruction,
        instructions,
        accum
    )

print(accum)

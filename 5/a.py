with open('input.txt', "r+") as file:
    contents = file.read()

entries = list(filter(lambda x: x != '', contents.split('\n')))


def restructure(entry):
    return [
        entry
        .replace('F', '0')
        .replace('B', '1')
        .rstrip('LR'),
        entry
        .replace('L', '0')
        .replace('R', '1')
        .lstrip('FB')
    ]


def getID(entry):
    row, column = entry
    return int(row, 2) * 8 + int(column, 2)


restructured = list(map(restructure, entries))
result = max(map(getID, restructured))

print(result)

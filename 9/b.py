from functools import reduce

with open('input.txt', "r+") as file:
    contents = file.read()

# Found in puzzle 9.a
target = 32321523
entries = list(filter(lambda x: x != '', contents.split('\n')))
numbers = list(map(int, entries))


# Using while, since making recursive calls exceeded the maximum depth
index, total, possibles = [0, 0, []]
while total < target:
    total = reduce(lambda acc, number: acc + number, possibles, 0)
    if total > target:
        # Try starting with +1 offset from previous starting index
        index = index - len(possibles) + 1
        possibles = []
        total = 0
        continue

    possibles.append(numbers[index])
    index += 1

weakness = min(possibles) + max(possibles)
print(weakness)

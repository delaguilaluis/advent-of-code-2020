from functools import reduce

with open('input.txt', "r+") as file:
    contents = file.read()


def reduz(numbers, accum, skip=True):
    print(numbers)
    if len(numbers) == 1:
        print(accum + 1, '\n')
        return 1

    if len(numbers) >= 4 and numbers[3] - numbers[0] == 3:
        print('first scenario')
        accum += reduz(numbers[2:], accum)

        copy = numbers[1:]
        copy.pop(1)
        accum += reduz(copy, accum)

        accum += reduz(numbers[3:], accum)

        print('base scenario without skipping')
        return reduz(numbers[1:], accum, skip=False)

    else:
        if skip and len(numbers) >= 3 and numbers[2] - numbers[0] <= 3:
            print('second scenario')
            accum += reduz(numbers[2:], accum)

    print('base scenario')
    return reduz(numbers[1:], accum)


entries = list(filter(lambda x: x != '', contents.split('\n')))
numbers = list(map(int, entries))
numbers.append(0)
numbers.append(max(numbers) + 3)

ways = reduz(sorted(numbers), 0)
print(ways)

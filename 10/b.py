from functools import reduce

with open('input.txt', "r+") as file:
    contents = file.read()


def reduz(numbers, accum):
    if len(numbers) == 1:
        print()
        return 1

    if len(numbers) >= 4 and numbers[3] - numbers[0] == 3:
        copy = numbers.copy()
        copy.pop(1)
        print(copy)
        accum += reduz(copy, accum)

        copyTwo = numbers.copy()
        copyTwo.pop(2)
        print(copyTwo)
        accum += reduz(copyTwo, accum)
    else:
        if len(numbers) >= 3 and numbers[2] - numbers[0] <= 3:
            copy = numbers.copy()
            copy.pop(1)
            print(copy)
            accum += reduz(copy, accum)

    print(numbers[1:])
    return reduz(
        numbers[1:],
        accum
    )


entries = list(filter(lambda x: x != '', contents.split('\n')))
numbers = list(map(int, entries))
numbers.append(0)
numbers.append(max(numbers) + 3)

ways = reduz(sorted(numbers), 0)
print(ways)

with open('input.txt', "r+") as file:
    contents = file.read()


def isValid(i, numbers, preambleLen):
    value = numbers[i]
    preamble = numbers[i - preambleLen:i]

    return any(map(
        lambda a: any(map(lambda b: a + b == value and a != b, preamble)),
        preamble
    ))


entries = list(filter(lambda x: x != '', contents.split('\n')))
numbers = list(map(int, entries))
preambleLen = 25

# TODO: make it "declarative" (?)
invalidNumbers = []
for i in range(preambleLen, len(numbers)):
    if not isValid(i, numbers, preambleLen):
        invalidNumbers.append(numbers[i])

print(invalidNumbers[0])

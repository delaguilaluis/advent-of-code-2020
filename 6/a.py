from functools import reduce

with open('input.txt', "r+") as file:
    contents = file.read()


def restructure(first, second):
    # Separator line
    if first.endswith(' ') and second == '\n':
        return first.rstrip(' ') + '|'

    # Simple line
    if second == '\n':
        return first + ' '

    return first + second


restructured = reduce(restructure, contents, '').rstrip()
split = restructured.split('|')


def addProps(details, char):
    if char == ' ':
        return details
    details.update({char: True})
    return details


def buildAnswers(entry):
    return reduce(addProps, entry, {})


listOfAnswers = list(map(buildAnswers, split))
answersCount = list(map(lambda x: len(x.values()), listOfAnswers))
sumOfCounts = reduce(lambda f, s: f + s, answersCount)
print(sumOfCounts)

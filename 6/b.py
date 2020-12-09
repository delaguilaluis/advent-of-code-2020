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


def addCount(details, char):
    if char == ' ':
        return details

    if (char in details):
        details.update({char: details[char] + 1})
    else:
        details.update({char: 1})

    return details


def aggregate(details, key):
    if key == "numberOfParticipants":
        return details
    if details[key] == details["numberOfParticipants"]:
        details.update({key: True})
    else:
        details.update({key: False})

    return details


def makeAggregate(details, key):
    details[key] = True
    return details


def buildAnswers(entry):
    answerDetails = reduce(addCount, entry, {})
    answerDetails.update({"numberOfParticipants": len(entry.split(' '))})
    answers = reduce(aggregate, answerDetails.keys(), answerDetails)
    answeredByEveryone = list(filter(lambda x: answers[x], answers.keys()))
    answeredByEveryone.remove("numberOfParticipants")
    return reduce(makeAggregate, answeredByEveryone, {})


listOfAnswers = list(map(buildAnswers, split))
answersCount = list(map(lambda x: len(x.values()), listOfAnswers))
sumOfCounts = reduce(lambda f, s: f + s, answersCount)
print(sumOfCounts)

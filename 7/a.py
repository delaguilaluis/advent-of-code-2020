import re

with open('input.txt', "r+") as file:
    contents = file.read()


def formatBag(bag):
    m = re.match(r"^\s?\d?(.*)(bag)s?$", bag)
    return m.group(1).strip()


def formatRule(entry):
    bag, contents = entry
    return [formatBag(bag), list(map(formatBag, contents.split(',')))]


def containsBag(color, rule):
    contents = rule[1]
    return any(map(lambda x: x == color, contents))


def getOutermostContainers(color, rules, accum):
    containers = list(filter(lambda x: containsBag(color, x), rules))

    # Exit when no more containers are found
    if len(containers) == 0:
        return accum

    for container in containers:
        color = container[0]
        if not color in accum:
            accum.append(color)

        getOutermostContainers(container[0], rules, accum)

    return accum


entries = list(filter(lambda x: x != '', contents.split('\n')))
withoutDot = list(map(lambda x: x.strip('.'), entries))
splitFromContents = list(map(lambda x: x.split(' contain '), withoutDot))
rules = list(map(formatRule, splitFromContents))
omc = getOutermostContainers('shiny gold', rules, [])

print(len(omc))

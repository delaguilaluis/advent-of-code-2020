from functools import reduce
import re

with open('input.txt', "r+") as file:
    contents = file.read()


def formatInnerBag(bag):
    m = re.match(r"^\s?(\d)?(.*)(bag)s?$", bag)

    if m.group(1):
        return [int(m.group(1)), m.group(2).strip()]
    else:
        return []


def formatOuterBag(bag):
    m = re.match(r"^\s?\d?(.*)(bag)s?$", bag)
    return m.group(1).strip()


def formatRule(entry):
    bag, contents = entry
    return [formatOuterBag(bag), list(map(formatInnerBag, contents.split(',')))]


def getTotalBags(color, rules):
    matchingRules = list(filter(lambda x: x[0] == color, rules))
    rule = matchingRules[0]
    color, contents = rule

    # Exit when current bag no longer has contents
    if len(contents[0]) == 0:
        return 0

    def accumulate(accum, detail):
        quantity, color = detail
        return accum + quantity + quantity * getTotalBags(color, rules)

    return reduce(accumulate, contents, 0)


entries = list(filter(lambda x: x != '', contents.split('\n')))
withoutDot = list(map(lambda x: x.strip('.'), entries))
splitFromContents = list(map(lambda x: x.split(' contain '), withoutDot))
rules = list(map(formatRule, splitFromContents))
totalBags = getTotalBags('shiny gold', rules)
print(totalBags)

from pprint import pprint
import re

with open('input.txt', "r+") as file:
    contents = file.read()


def formatBag(bag):
    m = re.match(r"^\s?\d?(.*)(bag)s?$", bag)
    return m.group(1).strip()


def formatRule(entry):
    bag, contents = entry
    return [formatBag(bag), list(map(formatBag, contents.split(',')))]


def containsShinyGoldBag(rule):
    contents = rule[1]
    return any(map(lambda x: x == 'shiny gold', contents))


def getContainers(color, rules):
    # improve to seek the outermost
    return list(filter(lambda x: x[0] == color, rules))


entries = list(filter(lambda x: x != '', contents.split('\n')))
withoutDot = list(map(lambda x: x.strip('.'), entries))
splitFromContents = list(map(lambda x: x.split(' contain '), withoutDot))
rules = list(map(formatRule, splitFromContents))
containersOfShineys = list(filter(containsShinyGoldBag, rules))
outerMostBags = list(
    map(lambda x: getContainers(x[0], rules), containersOfShineys))
pprint(outerMostBags)

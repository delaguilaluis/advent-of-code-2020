from pprint import pprint
from functools import reduce

with open('input.txt', "r+") as file:
    contents = file.read()

requiredFields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid', optional
]

def restructure(first, second):
    # Separator line
    if first.endswith(' ') and second == '\n':
      return first.rstrip(' ') + '|'

    # Simple line
    if second == '\n':
      return first + ' '

    return first + second

def addProps(first, second):
  key, value = second.split(':')
  first.update({ key: value })
  return first

def makeDictionary(propsList):
  return reduce(addProps, propsList, {})

def isValid(dict):
  return all(map(lambda x: x in dict, requiredFields))

restructured = reduce(restructure, contents, '').rstrip()
split = restructured.split('|')
setOfDetails = list(map(lambda x: x.split(' '), split))
dicts = list(map(makeDictionary, setOfDetails))
valid = list(filter(isValid, dicts))

pprint(len(valid))
from pprint import pprint
from functools import reduce
from re import match

with open("input.txt", "r+") as file:
    contents = file.read()


def makeRangeValidator(start, end):
    return lambda x: int(x) >= start and int(x) <= end


def isValidHeight(height):
    isMeasuredInCentimeters = height.endswith("cm")
    if isMeasuredInCentimeters:
        heightValue = int(height.rstrip("cm"))
        return heightValue >= 150 and heightValue <= 193

    isMeasuredInInches = height.endswith("in")
    if isMeasuredInInches:
        heightValue = int(height.rstrip("in"))
        return heightValue >= 59 and heightValue <= 76

    return False


def isValidColorHex(str):
    return len(str) == 7 and match(r"^#[a-f0-9]{6}$", str) != None


def isValidColorCode(str):
    codes = [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth"
    ]

    return any(map(lambda x: x == str, codes))


def isValidPassport(str):
    return match(r"^\d{9}$", str) != None


validators = {
    "byr": makeRangeValidator(1920, 2002),
    "iyr": makeRangeValidator(2010, 2020),
    "eyr": makeRangeValidator(2020, 2030),
    "hgt": isValidHeight,
    "hcl": isValidColorHex,
    "ecl": isValidColorCode,
    "pid": isValidPassport,
    "cid": lambda x: True  # Optional
}


def restructure(first, second):
    # Separator line
    if first.endswith(" ") and second == "\n":
        return first.rstrip(" ") + "|"

    # Simple line
    if second == "\n":
        return first + " "

    return first + second


def addProps(first, second):
    key, value = second.split(":")
    first.update({key: value})
    return first


def makeDictionary(propsList):
    return reduce(addProps, propsList, {})


def makeDictionaryChecker(dict, validators):
    return lambda key: validators[key](dict[key])


def hasValidKeys(dict):
    return all(map(lambda x: x in dict, list(validators.keys())))


def hasValidValues(dict):
    return all(map(makeDictionaryChecker(dict, validators), list(dict.keys())))


restructured = reduce(restructure, contents, "").rstrip()
split = restructured.split("|")
setOfDetails = list(map(lambda x: x.split(" "), split))
dicts = list(map(makeDictionary, setOfDetails))
dictsWithValidKeys = list(filter(hasValidKeys, dicts))
dictsWithValidValues = list(filter(hasValidValues, dicts))

pprint(len(dictsWithValidValues))

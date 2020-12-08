from functools import reduce
from re import match

with open("input.txt", "r+") as file:
    contents = file.read()


def makeRangeValidator(start, stop):
    # Force inclusive stop
    return lambda x: int(x) in range(start, stop + 1)


def isValidHeight(height):
    if height.endswith("cm"):
        heightValue = int(height.rstrip("cm"))
        return heightValue >= 150 and heightValue <= 193

    if height.endswith("in"):
        heightValue = int(height.rstrip("in"))
        return heightValue >= 59 and heightValue <= 76

    return False


def isValidColorHex(str):
    return match(r"^#[a-f0-9]{6}$", str) != None


def isValidColorCode(colorCode):
    validColorCodes = [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth"
    ]

    return any(map(lambda x: x == colorCode, validColorCodes))


def isValidPassport(passport):
    return match(r"^\d{9}$", passport) != None


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


def makeDictionaryChecker(dictionary, validators):
    return lambda key: validators[key](dictionary[key])


def hasRequiredFields(dictionary):
    requiredFields = list(validators.keys())
    # `cid` is optional
    requiredFields.remove('cid')
    return all(map(lambda x: x in dictionary, requiredFields))


def hasValidValues(dictionary):
    keys = list(dictionary.keys())
    return all(map(makeDictionaryChecker(dictionary, validators), keys))


restructured = reduce(restructure, contents, "").rstrip()
split = restructured.split("|")
setOfDetails = list(map(lambda x: x.split(" "), split))
dicts = list(map(makeDictionary, setOfDetails))
dictsWithRequiredFields = list(filter(hasRequiredFields, dicts))
dictsWithValidValues = list(filter(hasValidValues, dictsWithRequiredFields))

print(len(dictsWithValidValues))

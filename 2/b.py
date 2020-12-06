with open('input.txt', "r+") as file:
  contents = file.read()

def isValid(entry):
  password = entry['password']
  char = entry['char']
  firstIndex, secondIndex = entry['boundaries']
  hasFirstChar = password[firstIndex - 1] == char
  hasSecondChar = password[secondIndex - 1] == char
  isFirstScenario = hasFirstChar and not hasSecondChar
  isSecondScenario = hasSecondChar and not hasFirstChar
  return (isFirstScenario) or (isSecondScenario)

entries = list(filter(lambda x: x != '', contents.split('\n')))
rawDetails = list(map(lambda x: x.split(' '), entries))
details = list(map(lambda x: {
  'boundaries': list(map(lambda x: int(x), x[0].split('-'))),
  'char': x[1].replace(':', ''),
  'password': x[2]
}, rawDetails))

result = list(filter(isValid, details))
print(len(result))

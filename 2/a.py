with open('input.txt', "r+") as file:
  contents = file.read()

def isValid(entry):
  count = entry['password'].count(entry['char'])
  min, max = entry['boundaries']
  return count >= min and count <= max

entries = list(filter(lambda x: x != '', contents.split('\n')))
rawDetails = list(map(lambda x: x.split(' '), entries))
details = list(map(lambda x: {
  'boundaries': list(map(lambda x: int(x), x[0].split('-'))),
  'char': x[1].replace(':', ''),
  'password': x[2]
}, rawDetails))

result = list(filter(isValid, details))
print(len(result))

from functools import reduce

with open('input.txt', "r+") as file:
    contents = file.read()

def reduz(numbers, accum):
  if len(numbers) == 1:
    return accum
  
  accum.append(numbers[1] - numbers[0])

  return reduz(
    numbers[1:],
    accum  
  )

def countDifferences(diffs, n):
  return reduce(lambda a, b: a + 1 if b == n else a, diffs, 0)

entries = list(filter(lambda x: x != '', contents.split('\n')))
numbers = list(map(int, entries))
numbers.append(0)
numbers.append(max(numbers) + 3)

differences = reduz(sorted(numbers), [])
print(countDifferences(differences, 1) * countDifferences(differences, 3))

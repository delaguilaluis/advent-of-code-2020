with open('input.txt', "r+") as file:
    contents = file.read()

entries = list(filter(lambda x: x != '', contents.split('\n')))
spaceCount = len(entries[0])
tree = '#'

def countTrees(slopeRight, slopeDown):
  nextSpace = 0
  treeCount = 0

  for i in range(0, len(entries), slopeDown):
    currentSpace = entries[i][nextSpace % spaceCount]
    if currentSpace == tree:
        treeCount += 1
    nextSpace += slopeRight

  return treeCount

slopesOfInterest = [
  [1,1],
  [3, 1],
  [5, 1],
  [7, 1],
  [1, 2]
]

def reducer(first, second):
  return first * countTrees(second[0], second[1])

result = reduce(reducer, slopesOfInterest, 1)
print(result)

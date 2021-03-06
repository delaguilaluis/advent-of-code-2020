with open('input.txt', "r+") as file:
    contents = file.read()

entries = list(filter(lambda x: x != '', contents.split('\n')))
spaceCount = len(entries[0])
tree = '#'
nextSpace = 0
treeCount = 0

for entry in entries:
    currentSpace = entry[nextSpace % spaceCount]
    if currentSpace == tree:
        treeCount += 1
    nextSpace += 3

print(treeCount)

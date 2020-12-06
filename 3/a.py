with open('input.txt', "r+") as file:
    contents = file.read()

entries = list(filter(lambda x: x != '', contents.split('\n')))
tree = '#'
nextSpace = 0
treeCount = 0

for entry in entries:
    if entry[nextSpace % 3] == tree:
        treeCount += 1
    nextSpace += 3

print(treeCount)

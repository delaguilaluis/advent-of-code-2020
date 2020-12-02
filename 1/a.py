with open('input.txt', "r+") as file:
  contents = file.read()

entries = list(filter(lambda x: x != '', contents.split('\n')))
numbers = list(map(lambda x: int(x), entries))

shouldLeave = False
for i in numbers:
  for j in numbers:
    if (i + j) == 2020:
      print('Answer is:', i * j)
      shouldLeave = True
      break
  if shouldLeave == True: break

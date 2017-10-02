import os

with open('./filesList.txt') as f:
    lines = f.read().splitlines()

new = lines[1].split()
print type(new)
print new[0]
print new[1]

k = 0
for value in new:
    if k < 14:
        print value
        k += 1
# print line[0][0]

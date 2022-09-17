s = []
for i in range(10):
    s.append(input())


minRow = 0
maxRow = 0
first = True
i = 0
while i < 10:
    if s[i] != "..........":
        if first:
            minRow = i
            maxRow = i
            first = False
        else:
            maxRow = i
    i += 1

minCol = 0
maxCol = 0
first = True
for i in range(10):
    if s[minRow][i] == "#":
        if first:
            minCol = i
            maxCol = i
            first = False
        else:
            maxCol = i

print(minRow + 1, maxRow + 1)
print(minCol + 1, maxCol + 1)
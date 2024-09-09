numList = []
for i in range(5):
    numLine = list(input().split())
    numList.append(numLine)

for i in numList:
    letter = i
    print(' '.join(i).upper())
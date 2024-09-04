import sys
a = map(int, input().split())
minNum = sys.maxsize

for i in a :
    if i < minNum:
        minNum = i
print(minNum)
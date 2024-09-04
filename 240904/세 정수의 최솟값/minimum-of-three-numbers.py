import sys
a = map(int, sys.stdin.readline().split())
minNum = sys.maxsize

for i in a :
    if i < minNum:
        minNum = i
print(minNum)
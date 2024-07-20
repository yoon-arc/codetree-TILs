n, m = map(int, input().split());
numList = map(int, input().split());
count = 0

for i in numList:
    if i == 3:
        count += 1;

print(count)
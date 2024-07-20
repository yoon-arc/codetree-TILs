startNum = int(input());
numList = list(map(int, input().split()));
location = 0
count = 0

for i in range(len(numList)):
    if numList[i] == 2:
        location = i
        count += 1
    if count == 3:
        print(location+1);
        break;
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
maxNum = 0
for i in points:
    if i[1] > maxNum:
        maxNum = i[1]
pointCount = [0]*(maxNum+1)


for i in points:
   for j in range(i[0], i[1]+1):
       pointCount[j] += 1

print(max(pointCount))
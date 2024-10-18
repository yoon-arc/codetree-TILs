offset = 1000
total = 2001
checked = [[0]* total for _ in range(total)]
first = tuple(map(int, input().split()))
sec = tuple(map(int, input().split()))

for i in range(first[0], first[2]):
    for j in range(first[1], first[3]):
        checked[i][j] = 1
        
for i in range(sec[0]-first[0], sec[2]-first[2]):
    for j in range(sec[1]-first[1],sec[3]-first[3]):
        checked[i][j] = 0

sum = 0
for i in range(total):
    for j in range(total):
        if checked[i][j]:
            sum += 1
print(sum)
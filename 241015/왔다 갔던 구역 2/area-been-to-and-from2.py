n = int(input())
counts = [0]*111
moves = [input().split() for _ in range(n)]
location = 10

for i in moves:
    if i[1] == 'R':
        for j in range(location, location+int(i[0])):
            counts[j] += 1
        location += int(i[0])
        
    elif i[1] == 'L':
        for j in range(location-int(i[0]), location):
            counts[j] += 1
        location -= int(i[0])
        


total = 0
for i in range(len(counts)):
    if counts[i] >= 2:
        total += 1

print(total)
n = int(input())
total = 200
offset = 100
check = [['W']*total for _ in range(total)]

for i in range(1,n+1):
    now = tuple(map(lambda x : x+offset, map(int, input().split())))
    
    for h in range(now[0], now[2]):
        for v in range(now[1], now[3]):
            if i%2 == 1:
                check[h][v] = 'R'
            else:
                check[h][v] = 'B'

sum = 0
for i in range(total):
    for j in range(total):
        if check[i][j] == 'B':
            sum += 1

print(sum)
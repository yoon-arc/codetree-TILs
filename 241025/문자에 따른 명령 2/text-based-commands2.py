x = y = 0
d = 3
dx,dy = [1,0,-1,0],[0,-1,0,1]
commands = list(input())

for i in commands:
    if i == 'L':
        d = (d-1+4)%4
    if i == 'R':
        d = (d+1)%4
    if i == 'F':
        x, y = x+dx[d], y+dy[d]
print(x,y)
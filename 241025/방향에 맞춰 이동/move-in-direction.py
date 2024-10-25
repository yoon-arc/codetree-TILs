command = ['E','S','W','N']
dx, dy = [1,0,-1,0],[0,-1,0,1]
nx = ny = 0
N = int(input())

for i in range(N):
    d, move = input().split()
    move = int(move)   
    nx, ny = nx+(dx[command.index(d)] * move) ,ny+(dy[command.index(d)] * move)
    
print(nx, ny)
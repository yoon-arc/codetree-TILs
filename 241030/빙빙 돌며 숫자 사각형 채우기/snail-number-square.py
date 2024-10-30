h, y = map(int, input().split()) # h : 행 // y : 열
check = [ [0]* y for _ in range(h) ]

nhs, nys = [0,1,0,-1],[1,0,-1,0]
nh = ny = now_d = 0

check[nh][ny] = 1

def in_range(a,b):
    return 0<= a and a < h and 0<= b and b <y


for i in range(2, h*y+1):
    #범위 테스트용 변수
    hh, yy = nh+nhs[now_d], ny+nys[now_d]
    # print(nhs[now_d], nys[now_d])
    
    if not in_range(hh,yy) or check[hh][yy] != 0:
        now_d = (now_d+1)%4
        
    nh, ny = nh+nhs[now_d], ny+nys[now_d]
    check[nh][ny] = i

# print(check)  
for lines in check:
    print(*lines, sep=" ")
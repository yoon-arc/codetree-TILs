n, m = map(int, input().split())
A = []
B = []

def getP(n,w):
    now = 0
    for _ in range(n):
        t,d = input().split()
        t = int(t)
        for i in range(1,t+1):
            if d == 'R':
                now += 1
                w.append(now)
            else:
                now -= 1
                w.append(now)
                
                
getP(n,A)
getP(m,B)

i, j = 0,0
check = 0

while i < len(A) and j < len(B):
    if A[i] == B[j]:
        # print(A[i])
        check += 1
        i += 1
        j += 1
    elif A[i] > B[j]:
        j += 1
    else:
        i += 1

print(check)
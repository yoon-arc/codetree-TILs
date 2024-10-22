N, M = map(int, input().split())
A = []
B = []
def getA(n):
    now = 0
    for i in range(n):
        d,t = input().split()
        t = int(t)
        for j in range(t):
            if d == 'R':
                now += 1
                A.append(now)
            else:
                now -= 1
                A.append(now)

def getB(n):
    now = 0
    for i in range(n):
        d,t = input().split()
        t = int(t)
        for j in range(t):
            if d == 'R':
                now += 1
                B.append(now)
            else:
                now -= 1
                B.append(now)


getA(N)
getB(M)
# print(A, len(A))
# print(B, len(B))
ans = 0
for i in range(len(A)):
    if A[i] == B[i]:
        # print(i)
        ans = i+1
        break
    else:
        continue

if ans:
    print(ans)
else:
    print(-1)
N, M = map(int, input().split())
A = []
B = []
def getA(n):
    for i in range(n):
        now = 0
        v,t = map(int, input().split())
        for i in range(1,t+1):
            now += (v*i)
            A.append(now)
            
def getB(n):
    for i in range(n):
        now = 0
        v,t = map(int, input().split())
        for i in range(1,t+1):
            now += (v*i)
            B.append(now)


getA(N)
getB(M)
now = 0
change = -1
for i in range(len(A)):
    if A[i]>B[i] and now!= 'A':
        change += 1
        now = 'A'
    elif A[i]<B[i] and now!= 'B':
        change += 1
        now = 'B'
    else:
        continue
print(change)
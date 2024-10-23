N, M = map(int, input().split())
A = []
B = []

def getP(n,w):
    now = 0
    for _ in range(n):
        v,t = map(int, input().split())
        for i in range(t):
            now += v
            w.append(now)

getP(N,A)
getP(M,B)


winner = None
count = 0
for i in range(len(A)):
    if A[i] > B[i] and winner != 'A':
        count += 1
        winner = 'A'
    elif B[i] > A[i] and winner != 'B':
        count += 1
        winner = 'B'
    elif A[i] == B[i] and winner != 'AB':
        count +=1
        winner = 'AB'
print(count)
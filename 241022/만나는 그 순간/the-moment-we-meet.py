N, M = map(int, input().split())
A = []
B = []
def getA(n):
    now = 1
    for i in range(n):
        d,t = input().split()
        t = int(t)
        if d == 'R':
            now += t
        elif d == 'L':
            now -= t
        A.append(now)

def getB(n):
    now = 1
    for i in range(n):
        d,t = input().split()
        t = int(t)
        if d == 'R':
            now += t
        elif d == 'L':
            now -= t
        B.append(now)

# def compare (a,b):
#     if a>=b:
#         for i 
#     else:
getA(N)
getB(M)
# print(A)
# print(B)
answer = 0
for i in A:
    if i in B:
        answer = i
        break
    else:
        continue

if answer:
    print(answer)
else:
    print(-1)
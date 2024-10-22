N, M = map(int, input().split())
A = []
B = []

def get_P(n,w):
    for _ in range(n):
        v,t = map(int, input().split())  
        for i in range(t):
            w.append(v)

get_P(N, A)
get_P(M, B)


curP_A = 0
curP_B = 0

now = 0
change = -1

for i in range(len(A)):
    curP_A += A[i]
    curP_B += B[i]

    if curP_A > curP_B and now != 'A':
        change += 1
        now = 'A'
    elif curP_B > curP_A and now != 'B':
        change += 1
        now = 'B'
        
print(change)
n, m = map(int, input().split())
numList = list(map(int, input().split()))

def rep(M):
    sumUp = numList[M-1]
#     print(M)
    while M != 1:
        if M%2 == 1:
            M -= 1
            sumUp += numList[M-1]
        elif M%2 == 0:
            M //= 2
            sumUp += numList[M-1]
    return print(sumUp) 

rep(m)
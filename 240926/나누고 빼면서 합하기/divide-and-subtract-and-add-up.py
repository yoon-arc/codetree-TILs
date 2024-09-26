n, m = map(int, input().split())
numList = list(map(int, input().split()))

def rep(M):
    sum = M
    while M != 1:
        if M%2 == 1:
            M -= 1
            sum += numList[M]
        elif M%2 == 0:
            M //= 2
            sum += numList[M]
    return print(sum) 

rep(m)
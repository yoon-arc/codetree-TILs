M, D = map(int, input().split())
monthList = [31,28,31,30,31,30,31,31,30,31,30,31]

def get(M,D):
    if M < 13 and D <= monthList[M-1]:
        return print('Yes')
    else:
        return print('No')
get(M,D)
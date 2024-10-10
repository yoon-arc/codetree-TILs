N, B = map(int, input().split())

def getNum(n):
    num = []
    while n >= 4:
        num.append(n%4)
        n//=4
    num.append(n)
    return print(*num[::-1], sep="")
    
if B == 4:
    getNum(N)
else:
    print(oct(N))
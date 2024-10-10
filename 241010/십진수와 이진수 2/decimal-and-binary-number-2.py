N = input()

def getNum(n):
    length = len(n)
    num = 0
    for i in range(length):
        i = int(i)
        num += int(n[i])*(2**(length-i-1))
    return num

def getBinary(n):
    binary = []
    while n >= 2:
        now = n%2
        n = n//2
        binary.append(now)
        
    binary.append(n)
    return binary[::-1]


print(*getBinary(getNum(N)*17), sep='')
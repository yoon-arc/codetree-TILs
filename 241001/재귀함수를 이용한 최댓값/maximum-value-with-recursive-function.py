n = int(input())
nList = list(map(int, input().split()))
maxN = 0
def maxNum(n):
    global maxN
    
    if n == len(nList):
        return maxN
    if nList[n] > maxN:
        maxN = nList[n]
    return maxNum(n+1)

print(maxNum(0))
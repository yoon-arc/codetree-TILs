import math
N = int(input())
nList= list(map(int, input().split()))

def getLcm(n):
    total = math.lcm(*n)
    return total
print(getLcm(nList))
def gcd(a,b):
    if a%b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)
def lcm(a,b):
    return (a*b)//gcd(a,b)
# def lcm(a,b):

N = int(input())
nList= list(map(int, input().split()))
nList.sort()
now = lcm(nList[0],nList[1])

for i in range(2,len(nList)):
    now = lcm(now,nList[i])

print(now)
n, m = map(int, input().split())

def gcd(n,m):
    gcdList = []
    for i in range(1, n+1) :
        if n % i == 0 and m % i == 0:
            gcdList.append(i)
    return max(gcdList)

print(gcd(n,m))
n, m = map(int, input().split())

def gcd(n,m):
    gcdList = []
    for i in range(1, n+1) :
        if n % i == 0 and m % i == 0:
            gcdList.append(i)
    return max(gcdList)

gcd = gcd(n,m)
# 각 수를 최대공약수로 나눈 다음에, 2x3x6
def lcd(n,m):
    lcd = gcd * (n//gcd) * (m//gcd)
    return lcd

print(lcd(n,m))
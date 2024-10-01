def getSum(n):
    if n <= 0:
        return 0
    return n+getSum(n-2)
n = int(input())
print(getSum(n))
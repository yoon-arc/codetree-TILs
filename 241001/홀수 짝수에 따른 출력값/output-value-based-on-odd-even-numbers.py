total = 0
def getSum(n):
    global total 
    for i in range(n, 0, -2):
        total += i
    return total
n = int(input())
print(getSum(n))
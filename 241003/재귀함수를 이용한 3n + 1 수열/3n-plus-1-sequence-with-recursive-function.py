count = 0
def getNum(n):
    global count
    if n == 1:
        return
    count += 1
    if n%2==0:
        return getNum(n//2)
    if n%2==1:
        return getNum((3*n)+1)
N = int(input())
getNum(N)
print(count)
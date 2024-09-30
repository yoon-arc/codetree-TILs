n = int(input())
numList=[]
def recursive(n):
    if n == 0:
        return
    numList.append(n)
    recursive(n-1)
    numList.append(n)
recursive(n)
print(*numList, sep=' ')
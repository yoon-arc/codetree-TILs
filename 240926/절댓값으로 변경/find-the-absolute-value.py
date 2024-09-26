N = int(input())
arr = list(map(int, input().split()))

def setAbs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
        
setAbs(arr)
# print(arr)
print(*arr, sep=' ')
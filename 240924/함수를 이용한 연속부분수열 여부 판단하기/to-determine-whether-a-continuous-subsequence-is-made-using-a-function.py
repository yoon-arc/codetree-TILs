n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def getSlice(A,B):
    for i in range(len(A)):
        if A[i:i+n2] == B:
            return 'Yes'
            break

    else:
        return 'No'
print(getSlice(A,B))
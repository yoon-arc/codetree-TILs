n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(len(A)):
        if A[i] in B:
            if A[i:i+n2] == B:
                print('Yes')
                break
            else:
                print('No')
                break
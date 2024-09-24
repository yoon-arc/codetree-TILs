n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = 0
for i in range(len(A)):
    if A[i:i+n2] == B:
        print('Yes')
        break

else:
    print('No')
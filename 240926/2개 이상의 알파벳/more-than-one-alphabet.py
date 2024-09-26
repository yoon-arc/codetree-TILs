A = input()
B = set(A)

if len(B) == 1 or len(B) == len(A):
    print('No')
else:
    print('Yes')
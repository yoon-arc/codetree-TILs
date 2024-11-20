N = list(input())

if len(N) == 1:
    print(0)
elif '0' not in N:
    N[-1] = '0'
    print(int(''.join(N),2))
else:
    for i in range(len(N)):
        if N[i] != '1':
            N[i] = '1'
            break
    print(int(''.join(N),2))
        
N = list(input())

if len(N) == 1:
    print(N[0])
else:
    for i in range(len(N)):
        if N[i] != '1':
            N[i] = '1'
            break
    print(int(''.join(N),2))
        
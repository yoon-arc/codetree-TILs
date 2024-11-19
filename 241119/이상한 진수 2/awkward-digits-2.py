N = list(input())

if N[0] == '0' and len(N) == 1:
    print(0)
else:
    for i in range(len(N)):
        if N[i] != '1':
            N[i] = '1'
            break
    print(int(''.join(N),2))
        
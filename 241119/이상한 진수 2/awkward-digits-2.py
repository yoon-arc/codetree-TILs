N = list(input())

for i in range(len(N)):
    if N[i] != '1':
        N[i] = '1'
        break
print(int(''.join(N),2))
        